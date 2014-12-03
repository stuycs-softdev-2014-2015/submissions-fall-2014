var mouseX;
var mouseY;
var distance;

//setting the dog to a random position
var dog = document.getElementById("dog");
dog.style.display = "none";
dog.style.position = "absolute";
var dogLeft = Math.floor(Math.random()*parseInt(screen.width));
dog.style.left = "" + dogLeft+"px";
var dogTop = Math.floor(Math.random()*parseInt(screen.height));
dog.style.top = "" + dogTop +"px";
//to make the dog pic visible or invisible, use block or none

window.addEventListener('mousemove',function(e){
    mouseX = parseInt(e.pageX);
    mouseY = parseInt(e.pageY);
});

window.addEventListener('click',function(e){
    if (distance < 5){
	stopIt();
	var display = document.getElementById("distance").innerHTML = "YAY!";
	dog.style.display = "block";
    }
});

var checkMouse = function(){
    var dX = mouseX - dogLeft;
    var dY = mouseY - dogTop;
    distance = Math.sqrt( Math.pow(dX,2) + Math.pow(dY,2) );
    console.log("distance from dog: " + distance);
    var display = document.getElementById("distance").innerHTML = "Distance: " + distance;
};

var myevent;
var startIt = function(){
    myevent = setInterval(checkMouse,100);
};
var stopIt = function(){
    window.clearTimeout(myevent);
};

document.getElementById("start").addEventListener('click',startIt);
document.getElementById("stop").addEventListener('click',stopIt);
