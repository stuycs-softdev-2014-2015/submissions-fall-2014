var xCor = Math.floor((Math.random()*window.innerWidth)+1);
var yCor = Math.floor((Math.random()*window.innerHeight)+1);
console.log(xCor);
console.log(yCor);
var mouseX;
var mouseY;
var dist;

var display = document.getElementById("display");

var omg = document.getElementById("omg");


var playAgain = function(e) {
    omg.play();
}

var getCoords = function (e) {
    mouseX = e.pageX;
    mouseY = e.pageY;
    display.innerHTML  = "x: " + mouseX;
    display.innerHTML += "     ";
    display.innerHTML += "y: " + mouseY;
    dist = Math.sqrt(Math.pow(mouseX-xCor,2) + (Math.pow(mouseY-yCor,2)));
    display.innerHTML += "     ";
    display.innerHTML += "dist: " + dist;
    
}


var sound = setInterval(playAgain, 1000);

window.addEventListener("mousemove", getCoords);

