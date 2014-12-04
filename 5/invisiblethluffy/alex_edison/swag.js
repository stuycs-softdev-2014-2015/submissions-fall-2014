var mousex;
var mousey;
var swagX;
var swagY;
var swag = document.getElementById("swag");
var swag1 = document.getElementById("one");
var swag2 = document.getElementById("two");
var swag3 = document.getElementById("three");
var swag4 = document.getElementById("four");
var swag5 = document.getElementById("five");

swag.style.position="absolute";

swagX=Math.random()*(window.innerWidth-100);
swagY=Math.random()*(window.innerHeight-150);
swag.style.left=swagX+"px";
swag.style.top=(50+swagY)+"px";

document.addEventListener("mousemove", function(e) {
    var distance = Math.sqrt(Math.pow((e.clientX-swagX-50),2)+Math.pow((e.clientY-swagY-100),2));
    if (distance > 600) {
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
    }});

var swagger=function(e){
    var distance=Math.sqrt(Math.pow(mousex-(swagX+50),2)+Math.pow(mousey-(swagY+50),2));
}


var complete=function(e){
    swag.style.visibility="visible";
}

swag.addEventListener("click",complete(e));
var swagevent;
swagevent=setTimeout(swagger,300);
