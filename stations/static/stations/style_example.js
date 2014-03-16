function changeExampleText(initValue) {
	var actName = $("#id_name").val();
	
	if (actName == "") {
		$("#example").text(initValue);
	} else {
		$("#example").text(actName);
	}
}

function setExampleBackColor(bcol) {
	$('#example').css('background-color', bcol);
}

function setExampleTextColor(bcol){
	colorcode = bcol.toString().substr(1,7);
	var r = parseInt(colorcode.substr(0,2),16);
	var g = parseInt(colorcode.substr(2,2),16);
	var b = parseInt(colorcode.substr(4,2),16);
	var yiq = ((r*299)+(g*587)+(b*114))/1000;
	
	if (yiq >= 128) {
		$('#example').css({
				'color': 'black',
				'text-shadow': '0 1px 0 #F3F3F3'
		});
	} else {
		$('#example').css({
			'color': 'white',
			'text-shadow': '0 1px 0 #0C0C0C'
		});
	}
}

function setExampleBackTextColor(bcol) {
	// set background color
	setExampleBackColor(bcol);
	// set text color
	setExampleTextColor(bcol);
	// background color is updated by the script for #id_color
}

$(document).ready(function() {
	// get background color
	initCol = $("#id_color").val();
	
	// if initColor == "", set random color
	if (initCol == "") {
		initCol = '#'+Math.floor(Math.random()*16777215).toString(16);
		$("#id_color").val(initCol);
	}
	
	
	setExampleBackTextColor(initCol);
	
	// text
	var initName = $("#example").text();
	changeExampleText(initName);
	
	$("#id_name").on('input', function() {
		changeExampleText(initName);
	});
});