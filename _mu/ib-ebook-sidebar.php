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
		echo '<style id="ibsx-pre">@media(min-width:1100px){main.ibs-main,.entry-content:has(>.ibe),.entry-content:has(>.ibsx){display:grid;grid-template-columns:minmax(0,1fr) 300px;column-gap:30px;row-gap:0;max-width:1200px;margin-left:auto;margin-right:auto;box-sizing:border-box;align-items:start}main.ibs-main>*,.entry-content:has(>.ibe)>*{grid-column:1;min-width:0;max-width:none !important}main.ibs-main>.ibsx,.entry-content>.ibsx{grid-column:2;grid-row:1/span 40}}.ibuc-ad,.whc-ad,.ibsx-ad{max-width:100%;overflow:hidden}</style><script src="/assets/ib-sidebar.js?v=3" defer></script>' . "\n";
	}
}, 99 );
add_action( 'send_headers', function () {
	header( 'X-IB-Ebook-Sidebar: ' . ( ib_ebook_sidebar_wanted() ? 'on' : 'off' ) );
} );
