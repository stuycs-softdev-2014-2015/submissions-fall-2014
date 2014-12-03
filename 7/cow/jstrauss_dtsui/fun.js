// Justin Strauss and Derek Tsui
// Software Development Period 7
// Invisible Cow

var mouseX;
var mouseY;
var targetX;
var targetY;
var dist;

var updateCoords = function(e) {
	mouseX=e.pageX;
    mouseY=e.pageY;
	console.log("X:" + mouseX + ", Y:" + mouseY)
};

var currentDist = function(e) {
	dist = Math.sqrt(Math.pow(mouseX-targetX,2)+Math.pow(mouseY-targetY,2))
};

window.addEventListener('mousemove',updateCoords);