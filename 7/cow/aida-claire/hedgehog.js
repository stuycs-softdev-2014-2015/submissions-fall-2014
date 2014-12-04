var mouseX, mouseY, hedgehogX, hedgehogY;
var hedgehog = document.getElementById("hedgehog");
var jingle = document.getElementById("jingle");
var timer = document.getElementById("timer");
var maxDist = Math.sqrt(Math.pow(window.innerHeight,2) + Math.pow(window.innerWidth,2));
//Setting coordinates of hedgehog at random
hedgehogY = Math.random() * window.innerHeight * .9;
hedgehogX = Math.random() * window.innerWidth * .9;
hedgehog.style.top = hedgehogY + "px";
hedgehog.style.left = hedgehogX + "px";

var time, endtime;
var timeevent;
time = 0;

//Hiding hedgehog
hedgehog.style.visibility = "hidden";

///Adding event listener to hedgehog. Will become visible once clicked. 
//Removes eventListeners from the window. Mutes jingle. 
var reveal = function(e) {
    if (mouseOnImg()) {
	hedgehog.style.visibility = "visible";
	jingle.volume = 0;
	var text = document.createElement("h1");
	text.innerHTML = "You Found Him! Reload page to play again!"
	document.getElementById("heading").appendChild(text);
	window.removeEventListener('mousemove',find);
	window.removeEventListener('click', reveal);
	timeevent.stopPropagation()
    }
}

//determines if the mouse is on the hedgehog 
var mouseOnImg = function() {
	if (mouseX > hedgehogX && mouseX < 225 + hedgehogX) {
		if (mouseY > hedgehogY && mouseY < 150 + hedgehogY) {
			return true;
		};
	};
	return false;
};

var tick = function() {
    time = time + 1;
    timer.innerHTML = time;
};

var reset = function() {
    var endtime = time;
    time = 0;
    timer.innerHTML = time;
};


//Runs every time mouse is moved. Calculates distance from hedgehog, adjusts volume of
//jingle accordingly. 
var find = function(e) {
    mouseX = e.pageX;
    mouseY = e.pageY;
    var dist;
    dist = Math.sqrt(Math.pow((mouseX - hedgehogX),2) + Math.pow((mouseY - hedgehogY),2));
    var vol = maxDist / (90 * dist);
    if (vol > 1) {
   	vol = 1;
    }
    jingle.volume = vol;
};

timeevent = setInterval(tick,1000);

window.addEventListener('mousemove', find);

//Adds event listener to window. Every time user clicks, program checks
//to see if the mouse is on the image. If so, reveal! 
window.addEventListener('click', reveal);
	
