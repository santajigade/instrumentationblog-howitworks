<?php
/**
 * Plugin Name: IB hide unfilled ads
 * Description: Collapses ad boxes (and their Advertisement label) when AdSense leaves them unfilled. Added 25 Nov 2026. Delete this file to undo.
 */
add_action( 'wp_head', function () {
	echo '<style id="ib-ad-unfilled">.ibsb-ad:has(ins[data-ad-status="unfilled"]),.whc-ad:has(ins[data-ad-status="unfilled"]){display:none !important}</style>' . "\n";
}, 99 );
