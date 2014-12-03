var pic = document.getElementById("batman");

var X;
var Y;
var d;

var picX;
var picY;

var randomLoc = function(){
	var width = parseInt(pic.getAttribute("width"));
	var height = parseInt(pic.getAttribute("height"));
	var a  = Math.floor(Math.random() * (window.innerWidth - width));
	var b  = Math.floor(Math.random() * (window.innerHeight - height));
	picX = a + Math.ceil(width / 2);
	picY = b + Math.ceil(height / 2);
	pic.style.left = a + "px";
	pic.style.top = b + "px";
};

randomLoc();

var getMouseCor = function(e){
	X = e.pageX;
	Y = e.pageY;
	console.log("x: " + X + " y: " + Y);
	dist(e);
};

var dist = function(e){
	d = Math.sqrt(Math.pow(X - picX,2) + Math.pow(Y - picY,2));
	console.log("d: " + d);
};

window.addEventListener("mousemove",getMouseCor);
