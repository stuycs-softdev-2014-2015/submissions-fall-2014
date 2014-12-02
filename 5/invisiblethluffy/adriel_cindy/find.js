var mouseX, mouseY;

window.addEventListener('mousemove', function(e) {
    mouseX = e.pageX;
    mouseY = e.pageY;
});

var play = function() {
    var findX, findY;
    findX = 400;
    findY = 400;

    var dist = Math.sqrt( Math.pow(findX-mouseX,2) + Math.pow(findY-mouseY,2) )

    console.log(dist);
    console.log(mouseX + ", " + mouseY);
}

event = setInterval(play,100);

