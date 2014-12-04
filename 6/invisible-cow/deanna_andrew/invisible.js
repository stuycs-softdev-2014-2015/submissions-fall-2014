var mouseX;
var mouseY;

var screen = document.getElementById("screen");
//var this_screen = screen.getBoundingClientRect();

var minX = 0;
var minY = 0;
var maxX = window.innerWidth;
var maxY = window.innerHeight;

var goalX, goalY, dist;

var calcDistance=function(){
    var distX = mouseX-goalX;
    var distY = mouseY-goalY;
    var squares = (distX*distX)+(distY*distY);
    dist = Math.sqrt(squares);
};

var audio = document.getElementById("music");

function playAudio() {
    audio.play();
}

function pauseAudio() {
    audio.pause();
}


var changeCursor=function(){
    if (dist<300){ //Gotta check how much this even is
	canvas.style.cursor = "pointer";
    }
    else{
	canvas.style.cursor = "crosshair";
    }
};

window.addEventListener('mousemove',function(e){
    mouseX=e.pageX;
    mouseY=e.pageY;
    console.log(mouseX+ ", "+ mouseY)
    console.log("Dist: "+ dist)
    // changeCursor();
    calcDistance();

});


img = document.createElement("img");
img.src="christmas.png";

var starter;
var start= function(e){
    goalX = Math.random()*(maxX-minX)+minX;
    goalX = parseInt(goalX)
    goalY = Math.random()*(maxY-minY)+minY;
    goalY = parseInt(goalY)
    console.log("GOAL YO: " + goalX + ", " + goalY)
    changeCursor; //don't know why this doesn't work
    console.log("Dist: "+ dist)
    playAudio()

    //starter = setInterval(start,100);
};




/* function win(){
    } */


button = document.getElementById("button");
button.addEventListener('click', start);
