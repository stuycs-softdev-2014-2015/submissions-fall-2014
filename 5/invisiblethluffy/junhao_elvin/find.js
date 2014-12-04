var mouseX, mouseY;
var hiddenImg = document.getElementById("hiddenImg");
var imgX, imgY;
var distance = 0, found = false;
var audio = document.getElementById("audio");

function init(){
    window.addEventListener('mousemove', update());
    window.addEventListener('click', click());

    hiddenImg.style.opacity = 0;
    hiddenImg.draggable = false;
    // Set random x,y coords for img
    
    audio.play();
};

function update(){
    
};

function click(){
    // check to see if found = true (distance in range)

    if (found){
	hiddenImg.style.opacity = 100;
    }
};

function calcDistance(){
    var distance = parseInt(Math.sqrt(
	Math.pow(mouseX - pokemonX, 2) + 
	Math.pow(mouseY - pokemonY, 2)))
    return distance;
};

init();
