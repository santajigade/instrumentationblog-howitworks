/**
 * IB Article Uploader (WPCode PHP snippet, Run Everywhere)
 *
 * Adds POST /wp-json/ib/v1/article
 * Creates (or updates) a post as an Elementor page with ONE HTML widget,
 * same structure as existing articles, and fills Rank Math fields.
 * Only logged in users (or Application Password) with unfiltered_html can use it.
 *
 * JSON body:
 *   title (required), html (required), slug, status (draft|publish|future, default draft),
 *   date (for future, "2026-11-20 09:00:00"), categories (array of names or ids),
 *   author (user login or nicename), featured_media (media id),
 *   rank_math_title, rank_math_description, rank_math_focus_keyword,
 *   template_post (existing Elementor article id to copy layout settings from, default 15955),
 *   update_id (existing post id to update instead of creating)
 */
add_action( 'rest_api_init', function () {
	register_rest_route( 'ib/v1', '/article', array(
		'methods'             => 'POST',
		'permission_callback' => function () {
			return current_user_can( 'publish_posts' ) && current_user_can( 'unfiltered_html' );
		},
		'callback'            => 'ib_article_upload',
	) );
} );

function ib_el_id() {
	return substr( md5( wp_generate_uuid4() ), 0, 7 );
}

function ib_article_upload( WP_REST_Request $r ) {
	$p     = $r->get_json_params();
	$title = isset( $p['title'] ) ? wp_strip_all_tags( $p['title'] ) : '';
	$html  = isset( $p['html'] ) ? (string) $p['html'] : '';
	if ( $title === '' || $html === '' ) {
		return new WP_Error( 'ib_missing', 'title and html are required', array( 'status' => 400 ) );
	}

	$status = isset( $p['status'] ) && in_array( $p['status'], array( 'draft', 'publish', 'future' ), true ) ? $p['status'] : 'draft';

	// Categories by name or id
	$cats = array();
	foreach ( (array) ( $p['categories'] ?? array() ) as $c ) {
		$t = is_numeric( $c ) ? get_term( (int) $c, 'category' ) : get_term_by( 'name', html_entity_decode( $c ), 'category' );
		if ( ! $t || is_wp_error( $t ) ) {
			return new WP_Error( 'ib_cat', 'Category not found: ' . $c, array( 'status' => 400 ) );
		}
		$cats[] = (int) $t->term_id;
	}

	// Author by login or nicename
	$author_id = get_current_user_id();
	if ( ! empty( $p['author'] ) ) {
		$u = get_user_by( 'login', $p['author'] );
		if ( ! $u ) { $u = get_user_by( 'slug', $p['author'] ); }
		if ( ! $u ) {
			return new WP_Error( 'ib_author', 'Author not found: ' . $p['author'], array( 'status' => 400 ) );
		}
		$author_id = $u->ID;
	}

	$post = array(
		'post_type'    => 'post',
		'post_title'   => $title,
		'post_content' => $html,
		'post_status'  => $status,
		'post_author'  => $author_id,
	);
	if ( ! empty( $p['slug'] ) ) { $post['post_name'] = sanitize_title( $p['slug'] ); }
	if ( $cats ) { $post['post_category'] = $cats; }
	if ( $status === 'future' && ! empty( $p['date'] ) ) { $post['post_date'] = $p['date']; }

	if ( ! empty( $p['update_id'] ) ) {
		$post['ID'] = (int) $p['update_id'];
		if ( get_post_type( $post['ID'] ) !== 'post' ) {
			return new WP_Error( 'ib_update', 'update_id is not a post', array( 'status' => 400 ) );
		}
		$id = wp_update_post( wp_slash( $post ), true );
	} else {
		$id = wp_insert_post( wp_slash( $post ), true );
	}
	if ( is_wp_error( $id ) ) { return $id; }

	// Elementor: one section > one column > one HTML widget (same as existing articles)
	$data = array( array(
		'id'       => ib_el_id(),
		'elType'   => 'section',
		'settings' => array(),
		'elements' => array( array(
			'id'       => ib_el_id(),
			'elType'   => 'column',
			'settings' => array( '_column_size' => 100, '_inline_size' => null ),
			'elements' => array( array(
				'id'         => ib_el_id(),
				'elType'     => 'widget',
				'settings'   => array( 'html' => $html ),
				'elements'   => array(),
				'widgetType' => 'html',
			) ),
			'isInner'  => false,
		) ),
		'isInner'  => false,
	) );
	update_post_meta( $id, '_elementor_edit_mode', 'builder' );
	update_post_meta( $id, '_elementor_template_type', 'wp-post' );
	update_post_meta( $id, '_elementor_data', wp_slash( wp_json_encode( $data ) ) );
	delete_post_meta( $id, '_elementor_css' );

	// Copy layout settings from an existing article
	$tpl = ! empty( $p['template_post'] ) ? (int) $p['template_post'] : 15955;
	foreach ( array( '_elementor_version', '_elementor_page_settings', '_wp_page_template' ) as $k ) {
		$v = get_post_meta( $tpl, $k, true );
		if ( $v !== '' ) { update_post_meta( $id, $k, $v ); }
	}

	// Featured image
	if ( ! empty( $p['featured_media'] ) ) { set_post_thumbnail( $id, (int) $p['featured_media'] ); }

	// Rank Math
	foreach ( array( 'rank_math_title', 'rank_math_description', 'rank_math_focus_keyword' ) as $k ) {
		if ( isset( $p[ $k ] ) && $p[ $k ] !== '' ) {
			update_post_meta( $id, $k, sanitize_text_field( $p[ $k ] ) );
		}
	}

	if ( class_exists( '\Elementor\Plugin' ) ) {
		\Elementor\Plugin::$instance->files_manager->clear_cache();
	}

	return array(
		'id'      => $id,
		'status'  => get_post_status( $id ),
		'link'    => get_permalink( $id ),
		'preview' => get_preview_post_link( $id ),
		'edit'    => admin_url( 'post.php?post=' . $id . '&action=elementor' ),
	);
}


/* ---------- v2: read and patch existing Elementor articles ---------- */
add_action( 'rest_api_init', function () {
	$perm = function () { return current_user_can( 'edit_others_posts' ) && current_user_can( 'unfiltered_html' ); };
	register_rest_route( 'ib/v1', '/widgets/(?P<id>\d+)', array( 'methods' => 'GET', 'permission_callback' => $perm, 'callback' => 'ib_widgets_get' ) );
	register_rest_route( 'ib/v1', '/patch', array( 'methods' => 'POST', 'permission_callback' => $perm, 'callback' => 'ib_patch' ) );
} );

function ib_walk( &$els, $cb, $path = '' ) {
	foreach ( $els as $i => &$el ) {
		$p = $path === '' ? (string) $i : $path . '.' . $i;
		$cb( $el, $p );
		if ( ! empty( $el['elements'] ) ) { ib_walk( $el['elements'], $cb, $p ); }
	}
}

function ib_widgets_get( WP_REST_Request $r ) {
	$id   = (int) $r['id'];
	$data = json_decode( get_post_meta( $id, '_elementor_data', true ), true );
	if ( ! is_array( $data ) ) { return new WP_Error( 'ib_no_el', 'No Elementor data', array( 'status' => 404 ) ); }
	$out = array();
	ib_walk( $data, function ( $el, $p ) use ( &$out ) {
		if ( ( $el['elType'] ?? '' ) !== 'widget' ) { return; }
		$s = $el['settings'] ?? array();
		$c = $s['html'] ?? ( $s['editor'] ?? ( $s['title'] ?? '' ) );
		$out[] = array( 'path' => $p, 'type' => $el['widgetType'] ?? '', 'content' => $c );
	} );
	return array( 'id' => $id, 'sections' => count( $data ), 'widgets' => $out );
}

/**
 * Body: id, ops: [ {find, mode: after|before|replace, html} ... ]  (find = exact text, first match, html/text-editor widgets only)
 *       new_section: {index, html}  (optional: insert a new section with one HTML widget at top level index)
 *       rank_math_title, rank_math_description (optional)
 * A backup of the previous _elementor_data is stored in meta _ib_backup_<timestamp>.
 */
function ib_patch( WP_REST_Request $r ) {
	$p   = $r->get_json_params();
	$id  = (int) ( $p['id'] ?? 0 );
	$raw = get_post_meta( $id, '_elementor_data', true );
	$data = json_decode( $raw, true );
	if ( ! $id || ! is_array( $data ) ) { return new WP_Error( 'ib_no_el', 'No Elementor data', array( 'status' => 404 ) ); }
	update_post_meta( $id, '_ib_backup_' . time(), wp_slash( $raw ) );

	$report = array();
	foreach ( (array) ( $p['ops'] ?? array() ) as $k => $op ) {
		$done = false;
		ib_walk( $data, function ( &$el, $path ) use ( $op, &$done ) {
			if ( $done || ( $el['elType'] ?? '' ) !== 'widget' ) { return; }
			foreach ( array( 'html', 'editor' ) as $key ) {
				if ( ! isset( $el['settings'][ $key ] ) ) { continue; }
				$pos = strpos( $el['settings'][ $key ], $op['find'] );
				if ( $pos === false ) { continue; }
				$len = strlen( $op['find'] );
				$mode = $op['mode'] ?? 'after';
				$new = $mode === 'before' ? $op['html'] . $op['find'] : ( $mode === 'replace' ? $op['html'] : $op['find'] . $op['html'] );
				$el['settings'][ $key ] = substr_replace( $el['settings'][ $key ], $new, $pos, $len );
				$done = true; return;
			}
		} );
		$report[] = array( 'op' => $k, 'applied' => $done );
	}

	if ( ! empty( $p['new_section']['html'] ) ) {
		$sec = array( 'id' => ib_el_id(), 'elType' => 'section', 'settings' => array(), 'isInner' => false, 'elements' => array( array(
			'id' => ib_el_id(), 'elType' => 'column', 'settings' => array( '_column_size' => 100, '_inline_size' => null ), 'isInner' => false,
			'elements' => array( array( 'id' => ib_el_id(), 'elType' => 'widget', 'widgetType' => 'html', 'elements' => array(), 'settings' => array( 'html' => $p['new_section']['html'] ) ) ) ) ) );
		$idx = max( 0, min( count( $data ), (int) ( $p['new_section']['index'] ?? 0 ) ) );
		array_splice( $data, $idx, 0, array( $sec ) );
		$report[] = array( 'new_section' => $idx );
	}

	update_post_meta( $id, '_elementor_data', wp_slash( wp_json_encode( $data ) ) );
	delete_post_meta( $id, '_elementor_css' );
	foreach ( array( 'rank_math_title', 'rank_math_description' ) as $k ) {
		if ( ! empty( $p[ $k ] ) ) { update_post_meta( $id, $k, sanitize_text_field( $p[ $k ] ) ); }
	}
	wp_update_post( array( 'ID' => $id ) ); // bump modified date, keeps status/author
	if ( class_exists( '\Elementor\Plugin' ) ) { \Elementor\Plugin::$instance->files_manager->clear_cache(); }
	return array( 'id' => $id, 'report' => $report, 'link' => get_permalink( $id ) );
}
