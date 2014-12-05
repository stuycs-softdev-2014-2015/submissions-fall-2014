var myevent;
var w = window.innerWidth;
var h = window.innerHeight;

var stopTimer = function(e){
    window.clearInterval(e);
};

var mouseX, mouseY;

window.addEventListener('mousemove', function(e){
    mouseX=e.pageX;
    mouseY=e.pageY;
});

function start() {
    myevent = setInterval(move,50);
}
function stop() {
    window.clearTimeout(myevent);
}
function away() {
    var moveelt=document.querySelector('.move');
    moveelt.style.left=1000+"px";
    moveelt.style.top=1000+"px";
    alert("You killed the fly!");
}

function detectLeftButton(evt){
    evt = evt || window.event;
    var button = evt.which || evt.button;
    return button == 1;
}

function move(e) {
    var fly =document.getElementById("fly");
    var moveelt=document.querySelector('.move');
    var x = (moveelt.style.left);
    var y = (moveelt.style.top);
    x=x.substring(0,x.length-2);
    x=parseInt(x);
    y=y.substring(0,y.length-2);
    y=parseInt(y);
    
    console.log(mouseX);
    console.log(mouseY);

    if (isNaN(x) || x > 1200 || x < -100) x=1000;
    if (isNaN(y) || y < -100 || y > 1200 ) y=1000;

    var deltaX = mouseX-x;
    var deltaY = mouseY-y;

	if (deltaX >0) {
	    if (deltaX<100)
		x=x-20;
	    else if (deltaX<300)
		x=x-10;
	    else if (deltaX<500)
		x=x-2;
	} else{
	    if (deltaX>-100)
		x=x+20;
	    else if (deltaX>-300)
		x=x+10;
	    else if (deltaX>-500)
		x=x+2;
	}

	if (deltaY>0) {
	    if (deltaY<100)
		y=y-20;
	    else if (deltaY<200)
		y=y-10;
	    else if (deltaY<400)
		y=y-2;
	} else{
	    if (deltaY>-100)
		y=y+20;
	    else if (deltaY>-200)
		y=y+10;
	    else if (deltaY>-400)
		y=y+2;
	}
    

    if (x<50)
	x=Math.floor((Math.random() * 50));
    if (y<50)
	y=Math.floor((Math.random() * 50));
    if (y>h)
	y=Math.floor((Math.random() * 50)+750);
    if (x>w)
	x=Math.floor((Math.random() * 50)+1000);	
    
    moveelt.style.left=x+"px";
    moveelt.style.top=y+"px";
    var degs=Math.atan2(deltaY,deltaX) *90 / 3.14159;
    fly.style.webkitTransform = "rotate("+degs+"deg)";
}

//document.getElementById("start").addEventListener('click',startit);
document.getElementById("fly").addEventListener('click', away);
document.addEventListener('click', start());
