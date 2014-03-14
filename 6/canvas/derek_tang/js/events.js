var mx, my, mdown, ak = [false,false,false,false];

$(function() {
	
	$(window).keydown(function(e) {
		if (e.keyCode == 65) e.keyCode = 37;
		if (e.keyCode == 87) e.keyCode = 38;
		if (e.keyCode == 68) e.keyCode = 39;
		if (e.keyCode == 83) e.keyCode = 40;
		if (e.keyCode >= 37 && e.keyCode <= 40) ak[e.keyCode-37] = true;
	});
	$(window).keyup(function(e) {
		if (e.keyCode == 65) e.keyCode = 37;
		if (e.keyCode == 87) e.keyCode = 38;
		if (e.keyCode == 68) e.keyCode = 39;
		if (e.keyCode == 83) e.keyCode = 40;
		if (e.keyCode >= 37 && e.keyCode <= 40) ak[e.keyCode-37] = false;
	});
	
	
});




