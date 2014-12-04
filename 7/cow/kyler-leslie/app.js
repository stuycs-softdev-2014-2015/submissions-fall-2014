var w = true;



var mouseX;
var mouseY;


process = function(e) {
	if (w) {
    mouseX=e.pageX;
    mouseY=e.pageY;
    var sign = document.getElementById("sign");
    var type = sign.getAttribute("src");
    var style = window.getComputedStyle(sign);
    var signX = style.getPropertyValue('left');
    signX = parseInt( signX.substring(0, signX.length -2));
    var signY = style.getPropertyValue('top');
    signY = parseInt( signY.substring(0, signY.length -2));

    if ( mouseX > signX && mouseX < signX + 100 && mouseY > signY && mouseY < signY + 100 ) {
	var mover=document.querySelector('.move');
	var x = (mover.style.left);
	x = x.substring(0,x.length-2);
	x = parseInt(x);

	if (type == "img/575px-Go_sign.svg.png" ) {
	    	mover.style.left=x+50+"px";
		if (x>=1000) {youwin();}
		console.log(x);
		
	}
	else {
	    mover.style.left=x-50+"px";
	}
    }
}    
    
}
    

change = function(e) {
	if (w) {
   if (Math.floor( Math.random() * 6 ) < 5 ) {
       document.getElementById("sign").setAttribute("src", "img/575px-Go_sign.svg.png");
       }
    else {
	document.getElementById("sign").setAttribute("src", "img/stop_sign_clip_art.png");
    }
    document.getElementById("sign").style.left= Math.floor( Math.random() * 800 ).toString() + "px";
    document.getElementById("sign").style.top= Math.floor( Math.random() * 400 ).toString() + "px";
}
}


back = function(e) {
if (w) {
	var car = document.getElementById("car");
	var mover=document.querySelector('.move');
	var x = (mover.style.left);
	//console.log(x);
	x = x.substring(0,x.length-2);
	x = parseInt(x);

	//console.log(x)

	if (x >= 100) {
		x = x-1;
	}
	
	//console.log	
	
	mover.style.left=x+"px";
}
}

forward = function(e) {
	var mover=document.querySelector('.move');
	var x = (mover.style.left);
	x = x.substring(0,x.length-2);
	x = parseInt(x);

	if (x < 980) {
		x = x + 10;
	}

	mover.style.left = x+"px";
}


window.addEventListener('click', process);

myevent = setInterval(back, 100);
myevent2 = setInterval(change, 1000);


function youwin() {
var win = document.createElement("center");
win.innerHTML = "<br><br><br><br><h1>Stop! You Won!</h1>";
winner = document.getElementById("winner");
winner.appendChild(win);
w = false;
}


