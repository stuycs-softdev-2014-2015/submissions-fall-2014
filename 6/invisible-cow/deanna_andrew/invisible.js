var mouseX;
var mouseY;

var screen = document.getElementById("screen");
//var this_screen = screen.getBoundingClientRect();

var minX = screen.left;
var minY = screen.top;
var maxX = screen.right;
var maxY = screen.bottom;

var goalX, goalY;

var calcDistance=function(){
    var distX = mouseX-goalX;
    var distY = mouseY-goalY;
    var squares = distX*distX+distY*distY;
    var dist = Math.sqrt(squares);
};

var changeCursor=function(){
    if (dist<300){ //Gotta check how much this even is
	canvas.style.cursor = "pointer";
    }
    else{
	canvas.style.cursor = "crosshair";
    }
};

img = document.createElement("img");
img.src="christmas.png";

var start= function(e){
    goalX = Math.random()*(maxX-minX)+minX;
    goalY = Math.random()*(maxY-minY)+minY;
    changeCursor; //don't know why this doesn't work
};

/* function win(){
    } */


button = document.getElementById("button");
button.addEventListener('click', start);
