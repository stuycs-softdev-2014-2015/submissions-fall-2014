var img = document.getElementById("img");
var imgX = document.getElementById("img").x + document.getElementById("img").width/2;
var imgY = document.getElementById("img").y + document.getElementById("img").height/2;
var mouseX = 0;
var mouseY = 0;
var body;

var distance = function(e) {
    //var body = document.getElementById("body");
    body = document.getElementsByTagName("body")[0].style
    mouseX = e.pageX;
    mouseY = e.pageY;
    //console.log(mouseX);
    //console.log(mouseY);
    dist = Math.sqrt(
	Math.pow(mouseX - imgX, 2) +
	    Math.pow(mouseY - imgY, 2)
    )
    console.log(dist);
}
var changeBackground = function() {
    if (dist < 5){
	body.backgroundImage = 'url("2048.png")';
    }
    else if (dist < 20){
	body.backgroundImage = 'url("1024.png")';
    }
    else if (dist < 40){
	body.backgroundImage = 'url("512.png")';
    }
    else if (dist < 80){
	body.backgroundImage = 'url("256.png")';
    }
    else if (dist < 160){
	body.backgroundImage = 'url("128.png")';
    }
    else if (dist < 300){
	body.backgroundImage = 'url("64.png")';
    }
    else if (dist < 400){
	body.backgroundImage = 'url("32.png")';
    }
    else if (dist < 500){
	body.backgroundImage = 'url("16.png")';
    }
    else if (dist < 600){
	body.backgroundImage = 'url("8.png")';
    }
    else if (dist < 700){
	body.backgroundImage = 'url("4.png")';
    }
    else {
	body.backgroundImage = 'url("2.png")';
    }
}

document.addEventListener("mousemove", distance);

var event;
var mystart = function() {
	event = setInterval(changeBackground, 20);
}

var mystop = function() {
	window.clearTimeout(event);
}

document.getElementById("start").addEventListener('click', mystart);
document.getElementById("stop").addEventListener('click', mystop);
