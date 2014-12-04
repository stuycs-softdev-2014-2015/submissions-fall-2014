var mouseX;
var mouseY;

window.addEventListener('click', function(e) {
	mouseX=e.pageX;
	mouseY=e.pageY;
});

back = function(e) {
	var car = document.getElementById("car");
	var mover=document.querySelector('.move');
	var x = (mover.style.left);
	console.log(x);
	x = x.substring(0,x.length-2);
	console.log(x);
	x = parseInt(x);

	//console.log(x)

	if (x >= 100) {
		x = x-5;
	}
	
	//console.log	
	
	mover.style.left=x+"px";
}

var event;
function startit() {
event = setInterval(back,100);}

startit()
