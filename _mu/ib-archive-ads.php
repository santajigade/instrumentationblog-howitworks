<?php
/**
 * Plugin Name: IB archive ads
 * Description: Manual AdSense units between posts on category, tag, author, search and blog list pages.
 */
if ( ! defined( 'ABSPATH' ) ) { exit; }

add_action( 'the_post', function ( $post, $q ) {
	if ( is_admin() || ! $q->is_main_query() || ! in_the_loop() ) { return; }
	if ( ! ( is_archive() || is_search() || is_home() ) ) { return; }
	// Ad before post index 2, 5, 8 (after the 2nd, 5th and 8th post).
	$slots = array( 2 => '7215194230', 5 => '6552849252', 8 => '7839764783' );
	$i = (int) $q->current_post;
	if ( ! isset( $slots[ $i ] ) ) { return; }
	echo '<div class="ibar-ad"><div class="ibar-l">Advertisement</div>'
		. '<ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-3931314195561246" data-ad-slot="' . esc_attr( $slots[ $i ] ) . '" data-ad-format="auto" data-full-width-responsive="true"></ins>'
		. '<script>(adsbygoogle = window.adsbygoogle || []).push({});</script></div>';
}, 10, 2 );

add_action( 'wp_head', function () {
	if ( ! ( is_archive() || is_search() || is_home() ) || is_front_page() ) { return; }
	echo '<style id="ibar-css">.ibar-ad{margin:10px 0 34px;text-align:center;min-height:100px;clear:both}.ibar-l{font-size:12px;color:#9ca3af;text-transform:uppercase;letter-spacing:1px;margin-bottom:6px}.ibar-ad:has(ins[data-ad-status="unfilled"]){display:none}</style>' . "\n";
} );
