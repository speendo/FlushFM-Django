function getLastFields() {
	return $("#addresses .addresses_set").last();
}

function getLastUrlField() {
	return getLastFields().find(".address_url");
}

function getTotal() {
	return $('.addresses_set').length;
}

function setTotal(value) {
	if (value <= 1) {
		$('#addresses #id_address_set-TOTAL_FORMS').val(value);
	} else {
		$('#addresses #id_address_set-TOTAL_FORMS').val(value - 1);
	}
}

function addFields() {
	var newFields = $(addressTemplate);
	var total = getTotal();
	
	// set data
	newFields.data("address_index", total);

	// replace index in fields
	newFields.find(':input:not(.delete_button)').each(function() {
		var name = $(this).attr('name').replace('-0-', '-' + total + '-');
		var id = 'id_' + name;
		$(this).attr({'name': name, 'id': id}).val('').removeAttr('checked');
	});
	
	// replace index in "for elements"
	newFields.find('label').each(function() {
		var newFor = $(this).attr('for').replace('-0-', '-' + total + '-');
		$(this).attr('for', newFor);
	});
	
	// preparate animation
	if (total > 0) {
		newFields.hide();
	}
	
	// finally add it
	$("#addresses #id_address_set-TOTAL_FORMS").before(newFields);
	$("#addresses .addresses_set").trigger("create");
	
	// animate
	newFields.animate({
//		'height': 'show',
		'opacity': 'show'
	});
	
	total++;
	setTotal(total);
}

function deleteFields(curFields) {
	if (getTotal() > 1) {
		var curIndex = $(curFields).data("address_index");
		$(".addresses_set").each(function() {
			var otherIndex = $(this).data("address_index");
			if (otherIndex > curIndex) {
				var lowerIndex = $(this).data("address_index") - 1;
				// set data to lower index
				$(this).data("address_index", lowerIndex);
				// set rest
				$(this).find(':input').each(function() {
					var name = $(this).attr('name').replace('-' + otherIndex + '-','-' + lowerIndex + '-');
					var id = 'id_' + name;
			        $(this).attr({'name': name, 'id': id})
				});
				$(this).find('label').each(function() {
					var newFor = $(this).attr('for').replace('-' + otherIndex + '-','-' + lowerIndex + '-');
					$(this).attr('for', newFor);
				});
			}
		});
		// animate
		$(curFields).animate({
//			'height': 'hide',
			'opacity': 'hide'
		},
			function() {
				$(this).remove();
			}
		);
		
		// remove
//		$(curFields).remove();
		
		// finally lower total (no need to reduce by one because if necessary this is done in setTotal()
		setTotal(getTotal());
	}
}

$(document).ready(function() {
	// init
	addFields();
	$("#addresses .addresses_set").each(function(index) {
		$(this).data("address_index", index);
	});
	
	// add new field
	$("#addresses").on("input", getLastUrlField(), function() {
		if (getLastUrlField().val() != "") {
			addFields();
		}
	});
	
	// delete empty fields
	$("#addresses").on("input change", ".address_url", function() {
		if ($(this).val() == "") {
			deleteFields($(this).closest(".addresses_set"));
		}
	});
});