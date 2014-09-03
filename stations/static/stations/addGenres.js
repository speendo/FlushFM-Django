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
		console.log("appending");
		$('ul#selected_genres').append(
			replaceValue($('.genre_name_input').val(), getCol($('.genre_name_input').val()))
		);
		$('.genre_name_input').val('');
	}
}

function addItems() {
	$('.genre_add').click(function() {
		alert("value <" + $('.genre_name_input').val() + ">");
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

$(document).ready(function() {
	addItems();
	
	removeItem();
	
	// prevent submit on Enter Key
	noEnterSubmit();
});