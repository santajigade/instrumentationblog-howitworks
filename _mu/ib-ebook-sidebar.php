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
		echo '<style id="ibsx-pre">@media(min-width:1100px){main.ibs-main,.entry-content:has(>.ibsx){display:grid;grid-template-columns:minmax(0,1fr) 300px;column-gap:30px;row-gap:0;max-width:1200px;margin-left:auto;margin-right:auto;box-sizing:border-box;align-items:start}main.ibs-main>*,.entry-content:has(>.ibsx)>*{grid-column:1;min-width:0;max-width:none !important;margin-left:0 !important;margin-right:0 !important}main.ibs-main .ibuc-card{overflow-x:auto}main.ibs-main>.ibsx,.entry-content>.ibsx{grid-column:2;grid-row:1/span 40}.entry-content:has(>.ibsx)>.ibe:not(.ibsx-top) .ibe-band{width:auto !important;max-width:none !important;margin-left:0 !important;margin-right:0 !important;border-radius:16px;overflow:hidden}.entry-content:has(>.ibsx)>.ibsx-top{grid-column:1/-1 !important;grid-row:1}.entry-content:has(>.ibsx-top)>.ibe:not(.ibsx-top){grid-row:2}.entry-content>.ibsx-top~.ibsx{grid-row:2/span 40}}.ibuc-ad,.whc-ad,.ibsx-ad{max-width:100%;overflow:hidden}.ibsx-ad:has(ins[data-ad-status=\'unfilled\']),.ibsb-ad:has(ins[data-ad-status=\'unfilled\']),.whc-ad:has(ins[data-ad-status=\'unfilled\']),.ibuc-ad:has(ins[data-ad-status=\'unfilled\']){display:none !important}</style><script src="/assets/ib-sidebar-loader.js?v=1" defer></script>' . "\n";
	}
}, 99 );
add_action( 'send_headers', function () {
	header( 'X-IB-Ebook-Sidebar: ' . ( ib_ebook_sidebar_wanted() ? 'on' : 'off' ) );
} );
