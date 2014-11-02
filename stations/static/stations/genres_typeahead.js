// Bloodhound variable
var engine;

function runTypeAhead(address, templateDef) {
	// constructs the suggestion engine
	engine = new Bloodhound({
        datumTokenizer: Bloodhound.tokenizers.obj.whitespace('genre'),
        queryTokenizer: Bloodhound.tokenizers.whitespace,
        // `states` is an array of state names defined in "The Basics"
		limit: 10,
		prefetch: {
			url: address,
			filter: function(data) {
				return $.map(data.genres, function(val, i) {
					return {
						genre: val.name,
						color: val.color,
						id: val.pk
					};
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
	    source: engine.ttAdapter(),
		templates: {
			suggestion: templateDef
		}
	});
}

function appendData(templateAdd) {
	$(".typeahead").blur(function() {
		// get val
		var value = $(".typeahead").typeahead("val");

		// corresponding entry from bloodhound
		$.each(engine.index.datums, function(i, val) {
			if (val.genre == value) {
				// add data to .typeahead
				$(this).data("genreID", val.id);

				// change content of #copy_of_selected
				var data = {
					genre: val.genre,
					color: val.color,
					id: val.id
				};
				$("#copy_of_selected").html(templateAdd(data));

				// toggle .copy_of
				$(".copyOf_toggle").toggle();
			}
		});
	});
}

function unselect() {
	$('#copy_of_selected').on("click", '.remove', function() {
		// toggle .copy_of
		$(".copyOf_toggle").toggle();
	});
}

$(document).ready(function() {
	var address = "/stations/genres_json/";

	// Handlebars template
	var sourceDef = $("#genre_def_template").html();
	var sourceAdd = $("#genre_add_template").html();

	var templateDef = Handlebars.compile(sourceDef);
	var templateAdd = Handlebars.compile(sourceAdd);

	runTypeAhead(address, templateDef);

	// append data
	appendData(templateAdd);

	// re-enable typeahead input
	unselect();
})