var img = document.getElementById("img");
var imgX = document.getElementById("img").x;
var imgY = document.getElementById("img").y;
var mouseX = 0;
var mouseY = 0;

var distance = function(e) {
    mouseX = e.pageX;
    mouseY = e.pageY;
    //console.log(mouseX);
    //console.log(mouseY);
    dist = Math.sqrt(((imgX-mouseX)^2)+((imgY-mouseY)^2));
    console.log(dist);
}

document.addEventListener("mousemove", distance);


