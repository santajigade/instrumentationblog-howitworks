<?php
/**
 * Plugin Name: IB eBook shop sidebar
 * Description: Loads the shared static-section sidebar (/assets/ib-sidebar.js) on the eBook shop and eBook pages. Added 25 Nov 2026. Delete this file to undo.
 */
add_action( 'wp_footer', function () {
	if ( ! is_page() ) {
		return;
	}
	$p    = get_queried_object();
	$shop = get_page_by_path( 'instrumentation-ebooks' );
	if ( ! $p || ! $shop || ( (int) $p->ID !== (int) $shop->ID && (int) $p->post_parent !== (int) $shop->ID ) ) {
		return;
	}
	echo '<script src="/assets/ib-sidebar.js?v=2" defer></script>' . "\n";
}, 99 );
