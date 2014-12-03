var 
var mouseX;
var mouseY;

window.addEventListener('mousemove',function(e){
    mouseX=e.pageX;
    mouseY=e.pageY;
    console.log(mouseX);
});

window.addEventListener('click',startit);

function move(e) {
    var joe=document.getElementById("joe");
    var moveelt=document.querySelector('.move');
    var x = (moveelt.style.left);
    var y = (moveelt.style.top);
    x=x.substring(0,x.length-2);
    x=parseInt(x);
    y=y.substring(0,y.length-2);
    y=parseInt(y);
    if (isNaN(x)) x=200;
    if (isNaN(y)) y=200;
    if (mouseX<x) {
	x=x-3;
	joe.src="static/joe.png";
    } else {
	x=x+3;
	joe.src="static/joe.png";
    }
    if (mouseY<y) {
	y=y-3;
    } else {
	y=y+3;
    }
    moveelt.style.left=x+"px";
    moveelt.style.top=y+"px";
}

var myevent;

function startit() {
    myevent = setInterval(move,100);
}

function stopit() {
    window.clearTimeout(myevent);
}
