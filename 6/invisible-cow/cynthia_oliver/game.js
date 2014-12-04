var mouseX;
var mouseY;
var distance;
var dogLeft;
var dogTop;
//hint shows up when the mouse is really close to the dog
var hint = document.getElementById("hint");
hint.style.display = "none";
//to make the dog pic visible or invisible, use 'block' or 'none'
hint.style.position = "absolute";

//setting the dog to a random position:
var initialize = function(){
    var dog = document.getElementById("dog");
    dog.style.display = "none";
    dog.style.position = "absolute";
    dogLeft = Math.floor(Math.random()*parseInt(screen.width));
    dogTop = Math.floor(Math.random()*parseInt(screen.height));
    dog.style.left = "" + (dogLeft - 55) +"px"; 
    dog.style.top = "" + (dogTop - 90) +"px";
    hint.style.left = "" + (dogLeft - 5) +"px"; 
    hint.style.top = "" + (dogTop - 5) +"px";
    //subtract half the width and height of image to center it

};

initialize();  
document.getElementById("distance").style.display = "none";

//use this function while testing if you want to see the numerical distance between mouse and dog
var toggleDisplayDistance = function(){
    if (document.getElementById("distance").style.display == "none"){
	document.getElementById("distance").style.display = "block";
    }else if (document.getElementById("distance").style.display == "block"){
	document.getElementById("distance").style.display = "none";
    }
};

//use this function while testing if you want to see the image of dog
var toggleDisplayDog = function(){
    if (dog.style.display == "block"){
	dog.style.display = "none";
    }else if (dog.style.display == "none"){
	dog.style.display = "block";
    }
};

var audio = document.getElementById("bark");
audio.pause();
audio.volume = 0.1; //the starting volume

window.addEventListener('mousemove',function(e){
    mouseX = parseInt(e.pageX);
    mouseY = parseInt(e.pageY);
});

var screenDiag = Math.sqrt( Math.pow(screen.width,2) + Math.pow(screen.height,2) ); //length of diagonal of screen; used to determine how loud audio should be

window.addEventListener('click',function(e){
    if (distance < screenDiag*0.01){
	stopIt();
	var display = document.getElementById("distance").innerHTML = "YAY!";
	dog.style.display = "block";
    }
});

var checkMouse = function(){
    var dX = mouseX - dogLeft;
    var dY = mouseY - dogTop;
    distance = Math.sqrt( Math.pow(dX,2) + Math.pow(dY,2) );
    var display = document.getElementById("distance").innerHTML = "Distance: " + distance;
    if (distance < screenDiag*0.01){
	audio.volume = 1;
    }else if (distance < screenDiag*0.03){
	audio.volume = 0.9;
    }else if (distance < screenDiag*0.07){
	audio.volume = 0.8;
    }else if (distance < screenDiag*0.13){
	audio.volume = 0.7;
    }else if (distance < screenDiag*0.21){
	audio.volume = 0.6;
    }else if (distance < screenDiag*0.31){
	audio.volume = 0.5;
    }else if (distance < screenDiag*0.45){
	audio.volume = 0.4;
    }else if (distance < screenDiag*0.60){
	audio.volume = 0.3;
    }else if (distance < screenDiag*0.73){
	audio.volume = 0.2;
    }else if (distance < screenDiag){
	audio.volume = 0.1;
    }
    if (distance < 5){
	console.log("hint");
	if (hint.style.display == "none"){
	    hint.style.display = "block";
	}
    }
};

var myevent;
var startIt = function(){
    //initialize();
    audio.play();
    myevent = setInterval(checkMouse,100);
};
var stopIt = function(){
    audio.pause();
    window.clearTimeout(myevent);
};
var reset = function(){
    initialize();
    var newevent;
    audio.play();
    newevent = setInterval(checkMouse,100);
};

document.getElementById("start").addEventListener('click',startIt);
document.getElementById("stop").addEventListener('click',stopIt);
document.getElementById("reset").addEventListener('click',reset);