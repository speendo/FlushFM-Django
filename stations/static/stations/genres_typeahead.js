function runTypeAhead(address) {

		// constructs the suggestion engine
		var engine = new Bloodhound({
	        datumTokenizer: Bloodhound.tokenizers.obj.whitespace('genre'),
	        queryTokenizer: Bloodhound.tokenizers.whitespace,
	        // `states` is an array of state names defined in "The Basics"
			limit: 10,
			prefetch: {
				url: address,
				filter: function(data) {
					return $.map(data.genres, function(val, i) {
						return {genre: val.name};
					});
				}
			}
		});

	// kicks off the loading/processing of `local` and `prefetch`
	engine.initialize();

	// typeahead.js
	$(".typeahead").typeahead({
	    hint: true,
	    highlight: true,
	    minLength: 1
	}, {
	    name: 'genres',
	    displayKey: 'genre',
	    source: engine.ttAdapter()
	});
}

$(document).ready(function() {
	var address = "/stations/genres_json/";

	runTypeAhead(address);
})