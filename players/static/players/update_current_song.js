$(document).ready(function() {
	function updateEvery() {
		$(".currently-playing").load("currentsong.html");
	};

	setInterval(updateEvery, 3000);
});