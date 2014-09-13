function replaceValue(val, bgcol) {
	retElement = genreElement.replace("%BGCOL%", bgcol);
	return retElement.replace("%VALUE%", val);
}

function getCol(val) {
	// to be done
	return "5882FA";
}

function appendList() {
	if ($('.genre_name_input').val() != '') {
		$('ul#selected_genres').append(
			replaceValue($('.genre_name_input').val(), getCol($('.genre_name_input').val()))
		);
		$('.genre_name_input').val('');
	}
}

function addItems() {
	$('.genre_add').click(function() {
		appendList();
	});
	$('.genre_name_input').keyup(function(event){
		if(event.keyCode == 13) {
			appendList();
		}
	});
}

function removeItem() {
	$('ul#selected_genres').on("click", 'li.genre .remove', function() {
		console.log("now");
		$(this).closest('li.genre').remove();
	});
}

function noEnterSubmit() {
	$('.noEnterSubmit').keypress(function(event) {
		if (event.which == 13) {
			event.preventDefault();
		}
	});
}

function autoComplete() {
	var genres = new Bloodhound({
		datumTokenizer: Bloodhound.tokenizers.obj.whitespace('name'),
		queryTokenizer: Bloodhound.tokenizers.whitespace,
		limit: 10,
		prefetch: {
			// url points to a json file that contains an array of country names, see
			// https://github.com/twitter/typeahead.js/blob/gh-pages/data/countries.json
			url: '../data/countries.json',
			// the json file contains an array of strings, but the Bloodhound
			// suggestion engine expects JavaScript objects so this converts all of
			// those strings
			filter: function(list) {
				return $.map(list, function(country) { return { name: country }; });
			}
		}
	});

	// kicks off the loading/processing of `local` and `prefetch`
	countries.initialize();

	// passing in `null` for the `options` arguments will result in the default
	// options being used
	$('.typeahead').typeahead(null, {
		name: 'genres',
		displayKey: 'name',
		// `ttAdapter` wraps the suggestion engine in an adapter that
		// is compatible with the typeahead jQuery plugin
		source: countries.ttAdapter()
	});
}

$(document).ready(function() {
	//autoComplete();
	
	addItems();
	
	removeItem();
	
	// prevent submit on Enter Key
	noEnterSubmit();
});