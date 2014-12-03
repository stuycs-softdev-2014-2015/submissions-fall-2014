var mouseX, mouseY
var canvas = document.getElementById("canvas");
var dostuff = function(){
    var circle = canvas.getContext("2d");
    circle.beginPath();
    circle.arc(mouseX, mouseY, 20, 0, 2*Math.PI);
    circle.stroke();
}
var event;
event = setInterval(dostuff, 100);
