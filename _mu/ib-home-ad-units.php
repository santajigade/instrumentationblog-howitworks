<?php
/**
 * Plugin Name: IB home page ad units
 * Description: Home page [ib_home] ads: position units (IB_Top, IB_Mid1, IB_End) and horizontal format. Added 24 Nov 2026. Delete this file to undo.
 */
add_filter( 'do_shortcode_tag', function ( $out, $tag ) {
	if ( 'ib_home' !== $tag || false === strpos( $out, '5950781970' ) ) {
		return $out;
	}
	$units = array( '7215194230', '6552849252', '5046401284' );
	$i     = 0;
	$out   = preg_replace_callback( '/data-ad-slot="5950781970"/', function () use ( &$i, $units ) {
		$s = $units[ min( $i, count( $units ) - 1 ) ];
		$i++;
		return 'data-ad-slot="' . $s . '"';
	}, $out );
	return str_replace( 'data-ad-format="auto"', 'data-ad-format="horizontal"', $out );
}, 10, 2 );
