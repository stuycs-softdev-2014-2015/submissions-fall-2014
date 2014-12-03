var mouseX, mouseY;
var tX, tY;
var thluffy = "http://cestlaz.github.io/assets/images/thluffy.jpg";
var XY = document.getElementById("coords");

//MATH
var sq = function(x) {
    return (x * x);
}

var dist = function(x1, y1, x2, y2){
    return Math.sqrt(sq(x1 - x2) + sq(y1 - y2));
}

//SETXY
tX = Math.random() * screen.width;
tY = Math.random() * screen.height;
thluffy.style.left = (tX + "px");
thluffy.style.top = (tY + "px");

var setXY = function(e) {
    mouseX = e.pageX;
    mouseY = e.pageY;
    //XY.innerHTML = "MouseX: " + mouseX + " MouseY: " + mouseY;
}

var setBackgroundColor = function() {
    var distance = dist(mouseX, mouseY, tX, tY);
    console.log("distance: " + distance);
    if (distance < 10){
	document.body.style.backgroundColor="red";
    }
    else if (distance < 100) {
	document.body.style.backgroundColor="orange";
    }
    else if (distance < 300) {
	document.body.style.backgroundColor="yellow";
    }
    else if (distance < 600) {
	document.body.style.backgroundColor="green";
    }
    else if (distance < 1000) {
	document.body.style.backgroundColor="blue";
    }
    else {
	document.body.style.backgroundColor="purple";
    }
}

window.addEventListener('mousemove', setXY);
window.addEventListener('mousemove', setBackgroundColor);
