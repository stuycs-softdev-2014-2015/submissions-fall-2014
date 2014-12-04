var mouseX, mouseY;
var tX, tY;
var XY = document.getElementById("coords");
var body = document.body;
var thluffy = document.getElementById("thluffy");
var distance;
var newBGOpacity; //pure color based on difference
var op = 1; //current opacity
var fade = 0.005; //how quickly the background fades away
var rate = 1500;

var resetFlash = function() {
    op = newBGOpacity;
    clearInterval(flash);
    flash = setInterval(resetFlash, rate);
}

var calcBackground = function() {
	distance = Math.sqrt(Math.pow(mouseX - tX, 2) + Math.pow(mouseY - tY, 2));
    //console.log("distance: " + distance);
    if (distance >= 1500)
    	newBGOpacity = 0;
    else if (distance < 25) {
    	newBGOpacity = 1;
    }
    else {
    	newBGOpacity = 1 - (distance / 1500);
    }
    rate = distance * 4;
    console.log(distance);
    //body.style.backgroundColor = "rgba(0,255,0," + newBGOpacity + ")";
}

var fadeBackground = function() {
	op = op - fade;
	body.style.backgroundColor = "rgba(0,255,0," + op + ")";
}

var setXY = function(e) {
	mouseX = e.pageX;
	mouseY = e.pageY;
	//XY.innerHTML = "mouseX: " + mouseX + ", mouseY: " + mouseY + " " + tX + " " + tY +" " + rate;
}

var showThluffy = function() {
	var distance = Math.sqrt(Math.pow(mouseX - tX + 12.5, 2) + Math.pow(mouseY - tY + 12.5, 2));
	if (distance < 25) {
		thluffy.style.visibility = "visible";
		setTimeout(setup, 5000);
	}
}

//setup page
var setup = function() {
	tX = Math.random() * (screen.width - 500);
	tY = Math.random() * (screen.height - 500);
	console.log(tX);
	console.log(tY);
	thluffy.style.left = tX + "px";
	thluffy.style.top = tY + "px";
	thluffy.style.visibility = "hidden";
}

tX = Math.random() * (screen.width - 200);
tY = Math.random() * (screen.height - 200);
console.log(tX);
console.log(tY);
thluffy.style.left = tX + "px";
thluffy.style.top = tY + "px";	
window.addEventListener('mousemove', setXY);
window.addEventListener('mousemove', calcBackground);
window.addEventListener('click', showThluffy);

setInterval(fadeBackground, 10);
var flash = setInterval(resetFlash, rate);
