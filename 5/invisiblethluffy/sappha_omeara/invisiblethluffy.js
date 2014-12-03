var mouseX, mouseY;
var tX, tY;
var thluffy = "http://cestlaz.github.io/assets/images/thluffy.jpg";

var distFromThluffy = dist(mouseX, mouseY, tX, tY);

var setXY = function() {
    mouseX = e.pageX;
    mouseY = e.pageY;
}

var sq = function(x) {
    return (x * x);
}

var dist = function(x1, y1, x2, y2){
    return Math.sqrt(sq(x1 - x2) + sq(y1 - y2));
}

window.addEventListener("mousemove", setXY);

var getRandomXY() {
    tX = Math.random() * screen.width;
    tY = Math.random() * screen.height;
}
