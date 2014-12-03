

var beg = false;
var mouseX = -1;
var mouseY = -1;

var setcoor = function(e){
	mouseX = e.pageX;
	mouseY = e.pageY;
}

var move = function(e){
	if(beg){
		var x = (obj.style.left);
		var y = (obj.style.top);
		x=x.substring(0,x.length-2);
		x=parseInt(x);
		y=y.substring(0,y.length-2);
		y=parseInt(y);
		   
		if (isNaN(x)) x=200;
		if (isNaN(y)) y=200;
		if (mouseX<x) {
		 x=x-3;
		}else {
		 x=x+3;
		}if (mouseY<y) {
			 y=y-3;
		} else {
			 y=y+3;
		}
		obj.style.left=x+"px";
		obj.style.top=y+"px";
		
		console.log(x);
		}
}

var obj = document.querySelector(".mv");

var myevent;
function startit() {
	beg = true;
    myevent = setInterval(move,100);
}
function stopit() {
	beg = false;
	window.clearTimeout(myevent);
}
document.getElementById("strt").addEventListener('click', startit);
document.getElementById("stp").addEventListener('click', stopit);

window.addEventListener('mousemove', setcoor);