var width = window.innerWidth;
var height = window.innerHeight;
var maxDist = Math.sqrt(Math.pow(width,2) + (Math.pow(height,2)));


var xCor = Math.floor((Math.random()*width)+1);
var yCor = Math.floor((Math.random()*height)+1);

//console.log(xCor);
//console.log(yCor);

var mouseX;
var mouseY;
var dist;

var vol = 0.1;

//var display = document.getElementById("display");

var omg = document.getElementById("omg");

var playing = true;

var playAgain = function(e) {
    if (playing) {
	omg.play();
	setTimeout(playAgain, 3000);
    }
}

var sound = setTimeout(playAgain, 1000);

var getCoords = function (e) {
    mouseX = e.pageX;
    mouseY = e.pageY;
    /*
    display.innerHTML  = "x: " + mouseX;
    display.innerHTML += "     ";
    display.innerHTML += "y: " + mouseY;
    */
    
}

var getDist = function (e) {
    dist = Math.sqrt(Math.pow(mouseX-xCor,2) + (Math.pow(mouseY-yCor,2)));
    /*
    display.innerHTML += "     ";
    display.innerHTML += "dist: " + dist;
    */
}

var win = function (e) {
    playing = false;
    window.removeEventListener("mousemove", mouseCallback);
    //console.log("you win");
    var d2 = document.getElementById("d2");
    d2.innerHTML = "You found Becky!"
    var but = document.getElementById("but");
    but.play();
}

var mouseCallback = function(e) {
    getCoords(e);
    getDist(e);
    vol = (10 - Math.floor(dist/maxDist * 10)) / 10;
    //console.log(vol);
    omg.volume = vol;
    
}

var clickCallback = function (e) {
    if (vol == 1) {
	win(e);
    }
}

window.addEventListener("mousemove", mouseCallback);
window.addEventListener("click", clickCallback)

