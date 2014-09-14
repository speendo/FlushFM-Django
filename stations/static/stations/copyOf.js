$(document).ready(function() {
	$(".genre_property").find(":input").prop("disabled", $("#is_copy").prop("checked"));

	$("#is_copy").change(function() {
		$(".genre_property").find(":input").prop("disabled", $("#is_copy").prop("checked"));
	})
});