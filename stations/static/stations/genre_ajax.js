$(document).ready(function() {
	$('#genre_form').submit(function() {
		var curForm = $(this);
		var btn = $("#submit_btn");

		btn.button('loading');

		$.ajax({
			type: $(this).attr("method"),
			url: $(this).attr("action"),
			data: $(this).serialize(),
			success: function() {
				btn.button('reset');
//				curForm.replace(data);
			},
			error: function() {
				btn.button('reset');
			}
		})

		return false;
	})
})