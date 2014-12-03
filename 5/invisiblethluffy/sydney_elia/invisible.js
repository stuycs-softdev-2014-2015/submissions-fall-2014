

var beg = false;
var mouseX = -1;
var mouseY = -1;
var objx = -1;
var objy = -1;

var computedist(){
    return Math.sqrt(Math.pow(objx-mouseX,2)+Math.pow(objy-mouseY,2));
}

var setcoor = function(e){
	mouseX = e.pageX;
	mouseY = e.pageY;
}

var setInitial = function(){
    objx=10+Math.random()*((window.innerWidth-20));
    objy=10+Math.random()*((window.innerHeight-20));

    obj.style.left=objx+"px";
    obj.style.top=objy+"px";		
    console.log(x);
}
var move = function(e){
	if(beg){
	
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
		
		}
}

var obj = document.querySelector(".mv");

var myevent;
function startit() {
    beg = true;
    setInitial();
    myevent = setInterval(move,100);
}
function stopit() {
	beg = false;
	window.clearTimeout(myevent);
}
document.getElementById("strt").addEventListener('click', startit);
document.getElementById("stp").addEventListener('click', stopit);

window.addEventListener('mousemove', setcoor);
