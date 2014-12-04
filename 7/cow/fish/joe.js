var mouseX;
var mouseY;

window.addEventListener('mousemove',function(e){
    mouseX=e.pageX;
    mouseY=e.pageY;
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
	joe.src="static/joe_left.png";
    } else {
	x=x+3;
	joe.src="static/joe_right.png";
    }
    if (mouseY<y) {
	y=y-3;
    } else {
	y=y+3;
    }
    console.log((((Math.abs(mouseX-x))<=20)&&((Math.abs(mouseY-y))<=20)));
    if (((Math.abs(mouseX-x))<=20)&&((Math.abs(mouseY-y))<=20)){
	play_joeMP3();
    }
    moveelt.style.left=x+"px";
    moveelt.style.top=y+"px";
}

var myevent;

function startit() {
    myevent = setInterval(move,30);
    var beg_prompt = document.getElementById("beg_prompt");
    beg_prompt.parentNode.removeChild(beg_prompt);
    play_computeMP3();
    window.removeEventListener('click',startit);
}

function play_computeMP3(){
    document.getElementById("compute_mp3").play();
}

function play_joeMP3(){
    document.getElementById("joe_mp3").play();
}
