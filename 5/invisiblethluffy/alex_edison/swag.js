var mousex;
var mousey;
var swagX;
var swagY;
var swagevent;
var swag = document.getElementById("swag");
var swag1 = document.getElementById("one");
var swag2 = document.getElementById("two");
var swag3 = document.getElementById("three");
var swag4 = document.getElementById("four");
var swag5 = document.getElementById("five");

swag.style.position="absolute";

document.getElementById("begin").addEventListener("click", function(e) {
    swagX=Math.random()*(window.innerWidth-100);
    swagY=Math.random()*(window.innerHeight-150);
    swag.style.left=swagX+"px";
    swag.style.top=(50+swagY)+"px";
    if (swag.style.opacity == 1.0) {
	swag.style.opacity = 0.0;
    }
    swagevent = window.setInterval(function(){
	playSwag();
    }, 100);
});

document.addEventListener('mousemove', function(e) {
    mouseX = e.clientX;
    mouseY = e.clientY;
    //console.log("x: "+mouseX+" y: "+mouseY);
});

var playSwag = function() {
    if(swag.style.opacity==0.0){
	var distance = Math.sqrt(Math.pow((mouseX-swagX-50),2)+Math.pow((mouseY-swagY-100),2));
	console.log(distance);
	if (distance > 500) {
	    swag1.play();
	    swag2.pause();
	    swag3.pause();
	    swag4.pause();
	    swag5.pause();
	} else if ( distance > 350 ) { 
	    swag1.pause();
	    swag2.play();
	    swag3.pause();
	    swag4.pause();
	    swag5.pause();
	} else if ( distance > 150 ) { 
	    swag1.pause();
	    swag2.pause();
	    swag3.play();
	    swag4.pause();
	    swag5.pause();
	} else if ( distance > 50 ) { 
	    swag1.pause();
	    swag2.pause();
	    swag3.pause();
	    swag4.play();
	    swag5.pause();
	} else { 
	    swag1.pause();
	    swag2.pause();
	    swag3.pause();
	    swag4.pause();
	    swag5.play();
	}}};


swag.addEventListener("click",function(e){
    swag.style.opacity=1.0;
    window.clearInterval(swagevent);
    swag4.pause();
    swag5.pause();
    console.log("found");
});
