/*require('mapbox.js');*/

var map;
function init() {
	L.mapbox.accessToken = 'pk.eyJ1IjoibWN0aG9tcHMiLCJhIjoidGNJUUVsVSJ9.U6CffdhpOp3l1i2CWPp5ag';
	map = L.mapbbox.map('map', 'examples.map-i86nkdio')
		.setView([40, -74.50], 9);
}