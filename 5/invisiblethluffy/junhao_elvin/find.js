var mouseX, mouseY;
var hiddenImg = document.getElementById("hiddenImg");
var findMe = document.querySelector('.findMe');
var imgX, imgY;
var distance, inRange = false;
var reqDistance = 15; // pixels, find a suitable number

var audio = document.getElementById("audio");
var event;

// TODO: need to find a sound file

function init(){
    window.addEventListener('mousemove', update);
    window.addEventListener('click', click);

    // uncomment after done debugging
    //hiddenImg.style.opacity = 0;
    hiddenImg.draggable = false;
    // Set random x,y coords for img (incomplete)
    // parseInt, Math.floor, Math.random

    event = setInterval(audio.play(), 250);
};

function update(e){
    mouseX = e.pageX;
    mouseY = e.pageY;
    distance = calcDistance();
    // not sure if cursor part works
    // separate sound file for while `inRange`?
    if (distance < reqDistance){
	inRange = true;
	document.body.style.cursor = 'pointer';
    }
    else{
	inRange = false;
	document.body.style.cursor = 'default';
    }
    incVolume();
};

function click(e){
    if (inRange){
	hiddenImg.style.opacity = 100;
	window.clearInterval(event);
    }
};

function calcDistance(){
    var distance = parseInt(Math.sqrt(
	Math.pow(mouseX - imgX, 2) + 
	Math.pow(mouseY - imgY, 2)))
    return distance;
};

function incVolume(){
    //audio.volume = 
    // can be from 0 to 1 (percentage of maximum volume)
    // should be inverse proportional to distance
};

init();
