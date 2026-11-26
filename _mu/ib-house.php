<?php
/**
 * Plugin Name: IB house promo for unfilled ads
 * Description: Loads /assets/ib-house.js, which shows an eBook card in manual ad boxes that AdSense leaves unfilled. Added 26 Nov 2026. Delete this file to undo.
 */
add_action( 'wp_footer', function () {
	if ( is_admin() ) {
		return;
	}
	echo '<script id="ibh-js" src="/assets/ib-house.js?h=' . esc_attr( gmdate( 'YmdH' ) ) . '" defer></script>' . "\n";
}, 99 );
