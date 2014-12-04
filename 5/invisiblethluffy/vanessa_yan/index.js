var mouseX, mouseY;
var canvas=document.getElementById("canvas");
var context=canvas.getContext("2d");
var particles = [];
var ind = 0;
var grav = 1;
var hole;

function init(){
    context.fillRect(0, 0, canvas.width, canvas.height);
    hole = false;
}

var mouseUpdate = function mouseUpdate(e){
    mouseX = e.pageX;
    mouseY = e.pageY;
}

var random = function random(max, min){
    return (Math.random()*(max-min)) + min;
}

var updatePart = function updatePart(){
    this.xCor+= this.vX;
    this.yCor+= this.vY;
    if (this.yCor > 550){
	this.yCor = 550
	this.vY = this.vY * (-0.7) + 2*Math.random();
	this.vX = this.vX * (0.7 + 0.3*(Math.random()));
    }
    if (this.yCor < 50){
	this.yCor = 50;
	this.vY = this.vY * (-0.7) + 2*Math.random();
	this.vX = this.vX * (0.7 + 0.3*(Math.random()));
    }
    if (this.xCor > 750){
	this.xCor = 750
	this.vX = this.vX * (-0.7) + 2*Math.random();
	this.vY = this.vY * (0.7 + 0.3*(Math.random()));
    }
    if (this.xCor < 50){
	this.xCor = 50
	this.vX = this.vX * (-0.7) + 2*Math.random();
	this.vY = this.vY * (0.7 + 0.3*(Math.random()));
    }
    this.vY+= grav;
}

var blackHole = function blackHole(){
    hole = true;
    if (this.xCor < mouseX){
	this.vX = this.vX + 5;
    }
    else if (this.xCor > mouseX){
	this.vX = this.vX - 5;
    }
    if (this.yCor < mouseY){
	this.vY = this.vY + 5;
    }
    else if (this.yCor > mouseY){
	this.vY = this.vY - 5;
    }
}

function part(x, y, i, vx, vy, color, rad){
    this.xCor=x;
    this.yCor=y;
    this.index=i;
    this.vX=vx;
    this.vY=vy;
    this.color=color;
    this.rad=rad
    this.updatePart = updatePart;
    this.blackHole = blackHole;
}

var drawPart = function drawPart(){
    for (var i = 0; i<particles.length; i++){
	context.fillStyle=particles[i].color;
	context.beginPath();
	context.arc(particles[i].xCor, particles[i].yCor, particles[i].rad, 0, 2*Math.PI);
	context.fill();
	context.closePath();
    }
}    

var updateAll = function updateAll(){
    for (var i = 0; i<particles.length; i++){
	particles[i].updatePart();
    }
}

var newPart = function newPart(){
    var newP = new part(mouseX, mouseY, ind, random(3, -3), random(-7, -12), "white", random(10, 5));
    particles[ind] = newP;
    ind++;
}

var reset = function reset(){
    context.fillStyle="black";
    context.fillRect(0, 0, canvas.width, canvas.height);
}

var eachFrame = function eachFrame(){
    reset();
    drawPart();
}

var keyDown = function keyDown(){
    for (var i = 0; i<particles.length; i++){
	particles[i].blackHole();
    }
}

var keyUp = function keyUp(){
    hole = false;
}

window.onLoad = init();
window.addEventListener("mousemove", mouseUpdate);
window.addEventListener("click", newPart);
window.addEventListener("keydown", keyDown);
window.addEventListener("keyup", keyUp);
window.setInterval(function(e){
    reset();
    updateAll();
    drawPart();
}, 50);
