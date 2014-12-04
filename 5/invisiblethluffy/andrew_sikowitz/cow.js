var x, y;
var mouseX, mouseY, dist;
var audio1 = new Audio("http://www.wavlist.com/soundfx/003/cow-moo3.wav");
var audio2 = new Audio("http://www.wavlist.com/soundfx/003/cow-moo1.wav");
var audio3 = new Audio("http://www.wavlist.com/soundfx/003/cow-moo6.wav");
var audio4 = new Audio("ding.wav");
var cow = document.getElementById("cow");
var running;
var ev, sounds;
var cowsFound = 0;
console.log(cow);

var setcow = function() {
    cow.style.left = x + "px";
    cow.style.top = y + "px";
}

var playsounds = function() {
    if (dist > 500) {
	audio1.volume = .2;
	audio1.play();
    }
    else if (dist > 250) {
	audio2.volume = .5;
	audio2.play();
    }
    else if (dist > 100) {
	audio3.volume = 1;
	audio3.play();
    }
    else if (dist < 50) {
	stop();
	audio4.play();
    }
}

var start = function(e) {
    try { //For clicking new button
	window.removeEventListener("mousemove", run);
	window.clearTimeout(ev);
	window.clearTimeout(sounds);
    }
    catch (err) {}
    x = Math.floor(Math.random()*(window.innerWidth-100) + 50);
    y = Math.floor(Math.random()*(window.innerHeight-100) + 50);
    setcow();
    running = 1;
    ev = setInterval(move, 100);
    sounds = setInterval(playsounds, 800);
    window.addEventListener("mousemove", run);
    dist = 0;
    document.getElementById("body").style.cursor = "none";

    //Make random starting point for cow, away from edges
    //Start event listeners and intervals
};

var move = function() {
    if (x > 50 && x < (window.innerWidth - 50)) {
	x = x + Math.floor(Math.random()*6-3);
	if (x > mouseX)
	    x++;
	else
	    x--;
    }
    if (y > 50 && y < (window.innerHeight - 50)) {
	y = y + Math.floor(Math.random()*6-3);
	if (y > mouseY)
	    y++;
	else
	    y--;
    }
    setcow();
};

var run = function(e) {
    mouseX = e.pageX;
    mouseY = e.pageY;
    dist = Math.floor(Math.sqrt(Math.pow(x-mouseX, 2) + Math.pow(y-mouseY,2)));
};

var pause = function() {
    if (running != -1) { //Set to -1 after cow found
	if (running) {
	    window.clearTimeout(ev);
	    window.clearTimeout(sounds);
	    window.removeEventListener("mousemove", run);
	}
	else {
	    ev = setInterval(move, 100);
	    sounds = setInterval(playsounds, 800);
	    window.addEventListener("mousemove", run);
	}
	running = 1 - running;
    }
};

var stop = function() {
    window.removeEventListener("mousemove", run);
    window.clearTimeout(ev);
    window.clearTimeout(sounds);
    cowsFound++;
    document.getElementById("counter").innerHTML = "Cows found: " + cowsFound;
    document.getElementById("body").style.cursor = "default";
    running = -1;
}

start();
document.getElementById("pause").addEventListener("click", pause);
document.getElementById("new").addEventListener("click", start);
document.getElementById("header").style.cursor = "default";
document.getElementById("cheat").addEventListener("click", function() {
    document.getElementById("body").style.cursor = "default";
});
