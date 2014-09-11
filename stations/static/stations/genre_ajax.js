$(document).ready(function() {
	$('#genre_form').submit(function() {
		var curForm = $(this);

		$.ajax({
			type: $(this).attr("method"),
			url: $(this).attr("action"),
			data: $(this).serialize(),
			success: function(data) {
//				curForm.replace(data);
			}
		})

		return false;
	})
})