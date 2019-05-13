$( document ).ready(function() {
	var x = document.getElementById( "places-list" );

	$( 'button' ).click(function() {
		getLocation();
	});

	function getLocation() {
		x.innerHTML = "Searching your location..";

		if (navigator.geolocation) {
			navigator.geolocation.getCurrentPosition(fetchPlaces);
		} else {
			x.innerHTML = "Geolocation is not supported by this browser.";
		}
	}

	function fetchPlaces(position) {
		x.innerHTML = position.coords.latitude + "|" + position.coords.longitude;
	}
});
