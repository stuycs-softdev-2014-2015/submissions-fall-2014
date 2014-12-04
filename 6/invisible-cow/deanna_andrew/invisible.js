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

function getVolume() {
    console.log("Volume: " + audio.volume);
}

function setVolume() {
    audio.volume = 1 - Math.round((dist/maxX)*100)/100
}


var changeCursor=function(){
    if (dist<100){
        document.body.style.cursor = "crosshair";
    }
    else{
        document.body.style.cursor = "pointer";
    }
};

window.addEventListener('mousemove',function(e){
    mouseX=e.pageX;
    mouseY=e.pageY;
    console.log(mouseX+ ", "+ mouseY)
    console.log("Dist: "+ dist)
    changeCursor();
    calcDistance();
    setVolume();
    getVolume();
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
    playAudio()

    //starter = setInterval(start,100);
};




/* function win(){
    } */


button = document.getElementById("button");
button.addEventListener('click', start);
