var mouseX, mouseY;
var tX, tY;
var thluffy = document.getElementById("thluffy");
var XY = document.getElementById("coords");

//MATH
var sq = function(x) {
    return (x * x);
}

var dist = function(x1, y1, x2, y2){
    return Math.sqrt(sq(x1 - x2) + sq(y1 - y2));
}

//SETXY
var placeThluffy = function(){
    tX = Math.floor(Math.random() * screen.width);
    tY = Math.floor(Math.random() * screen.height);
    thluffy.left = (tX + "px");
    thluffy.top = (tY + "px");
}

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

placeThluffy();

//THIS PART ISN'T WORKING
var myEvent;
var startit = function() {
    placeThluffy();
    if (document.body.style.background == "red"){
	stopit();
    }
    else{
	myEvent = setInterval(setBackgroundColor, 100);
    }
}

var stopit = function() {
    window.clearTimeout(myEvent);
}

//document.getElementById("start").addEventListener('click',startit);
//document.getElementById("stop").addEventListener('click',stopit);
window.addEventListener('mousemove', setXY);
//window.addEventListener('mousemove', setBackgroundColor);

//THIS NEEDS TO BE IN HTML, BUT IT BREAKS THE CODE
