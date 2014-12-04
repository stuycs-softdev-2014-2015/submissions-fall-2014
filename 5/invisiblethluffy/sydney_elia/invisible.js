var beg = false;
var mouseX = -1;
var mouseY = -1;
var objx = -1;
var objy = -1;
var d = 1000;

var computedist = function(){
    return Math.round(Math.sqrt(Math.pow(objx-mouseX,2)+Math.pow(objy-mouseY,2)));
}

var checkfound = function(d){
	if (d < 30){
		obj.style.visibility = "visible";
	}
}

var setcoor = function(e){
	mouseX = e.pageX;
	mouseY = e.pageY;
	d = computedist();
	distsh.innerHTML = d;
	checkfound(d);
}

var distsh = document.getElementById("dist");

var setInitial = function(){
    objx=10+Math.random()*((window.innerWidth-20));
    objy=10+Math.random()*((window.innerHeight-20));

    obj.style.left=objx+"px";
    obj.style.top=objy+"px";
}

var move = function(e){
	if(beg){
		audio.volume = 2/(0.05*d+1);
		audio.play();
		console.log(audio.volume);
		console.log('sound here');
	}
}
var audio = new Audio('soundeffect.mp3');
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
