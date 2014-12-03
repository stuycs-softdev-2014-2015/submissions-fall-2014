var mouseX, mouseY
var findX, findY;
var dist;

window.addEventListener('mousemove', function(e) {
    mouseX = e.pageX;
    mouseY = e.pageY;
});

var play = function() {

    findX = 400;
    findY = 400;

    dist = Math.sqrt( Math.pow(findX-mouseX,2) + Math.pow(findY-mouseY,2) )

    console.log(dist);
    console.log(mouseX + ", " + mouseY);

}

window.addEventListener('mousedown', function() { 
    if ( dist < 100 ) 
	window.alert("Yay!");
} );

event = setInterval(play,100);

