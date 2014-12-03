//CTRL-SHIFT-J TO OPEN CONSOLE (in chrome, on linux)

var mouseX, mouseY;

var mouseCoord = function(e){
    mouseX = e.pageX;
    mouseY = e.pageY;
    console.log("x: " + mouseX);
    console.log("y: " + mouseY);
}


window.addEventListener('mousemove', mouseCoord);
