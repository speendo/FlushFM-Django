function toggleCopy() {
	$(".genre_property").find(":input").prop("disabled", $("#is_copy").prop("checked"));
	$(".copy_input").prop("disabled", !($("#is_copy").prop("checked")));

	// #example
	if ($("#is_copy").prop("checked")) {
		$("#example").css("display", "none");
	} else {
		$("#example").css("display", "initial");
	}
}

$(document).ready(function() {
	toggleCopy();

	$("#is_copy").change(function() {
		toggleCopy();
	})
});