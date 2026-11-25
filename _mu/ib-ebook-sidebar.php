<?php
/**
 * Plugin Name: IB eBook shop sidebar
 * Description: Loads the shared static-section sidebar (/assets/ib-sidebar.js) on the eBook shop and eBook pages. Added 25 Nov 2026. Delete this file to undo.
 */
function ib_ebook_sidebar_wanted() {
	$uri = isset( $_SERVER['REQUEST_URI'] ) ? (string) $_SERVER['REQUEST_URI'] : '';
	return 0 === strpos( $uri, '/instrumentation-ebooks/' );
}
add_action( 'wp_head', function () {
	if ( ib_ebook_sidebar_wanted() ) {
		echo '<script src="/assets/ib-sidebar.js?v=2" defer></script>' . "\n";
	}
}, 99 );
add_action( 'send_headers', function () {
	header( 'X-IB-Ebook-Sidebar: ' . ( ib_ebook_sidebar_wanted() ? 'on' : 'off' ) );
} );
