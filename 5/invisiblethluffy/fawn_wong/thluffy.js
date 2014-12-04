var mouseX, mouseY;
var tX, tY;
var XY = document.getElementById("coords");
var body = document.body;
var thluffy = document.getElementById("thluffy");

var changeBackground = function() {
    var distance = Math.sqrt(Math.pow(mouseX - tX, 2) + Math.pow(mouseY - tY, 2));
    //console.log("distance: " + distance);
    var newBGOpacity;
    if (distance >= 1000)
	newBGOpacity = 0;
    else if (distance < 10) {
	newBGOpacity = 1;
    }
    else {
	newBGOpacity = 1 - (distance / 990);
    }
    body.style.backgroundColor = "rgba(0,255,0," + newBGOpacity + ")";
}

var setXY = function(e) {
    mouseX = e.pageX;
    mouseY = e.pageY;
    XY.innerHTML = "mouseX: " + mouseX + ", mouseY: " + mouseY;
}

//setup page
tX = Math.random() * (screen.width - 200);
tY = Math.random() * (screen.height - 200);
console.log(tX);
console.log(tY);
thluffy.style.left = tX + "px";
thluffy.style.top = tY + "px";

window.addEventListener('mousemove', setXY);
window.addEventListener('mousemove', changeBackground);
setup;
thluffy.addEventListener('click', showThluffy);
