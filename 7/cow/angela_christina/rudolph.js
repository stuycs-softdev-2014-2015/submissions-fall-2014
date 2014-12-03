//CTRL-SHIFT-J TO OPEN CONSOLE (in chrome, on linux)

var mouseX, mouseY;

//sets our variables mouseX and mouseY to current mouse's x and y
var mouseCoord = function(e){
    mouseX = e.pageX;
    mouseY = e.pageY;
    console.log("x: " + mouseX);
    console.log("y: " + mouseY);
}

//returns a random integer from min to max inclusive
var rand = function(min, max) {
    return Math.floor(Math.random() * (max - min)) + min;
}

window.addEventListener('mousemove', mouseCoord);
