var cow = document.getElementById("cow");
var button1 = document.getElementById("start");
var button2 = document.getElementById("stop");
var moo1player = document.getElementById('audiotag1');
var moo2player = document.getElementById('audiotag2');
var moo3player = document.getElementById('audiotag3');
var tempX;
var tempY;
var pos_x = 300;
var pos_y = 100;

window.addEventListener('mousemove',function(e){
    tempX = e.pageX;
    tempY = e.pageY;
});

var cowmoo = function(e){ 
    document.getElementById("display").innerHTML = tempX.toString() + "," + tempY.toString()
    if(Math.pow(pos_x - tempX, 2) + Math.pow(pos_y - tempY, 2) <= 100){
	moo3player.play();
	document.getElementById("display").innerHTML += ",c";
	cow.style.visibility = "visible";
	cow.style.display = "block";
	stopmoo();
    } else if (Math.pow(pos_x - tempX, 2) + Math.pow(pos_y - tempY, 2) <= 400){
	moo2player.play();
	 document.getElementById("display").innerHTML += ",b"
    } else {
	moo1player.play();
	 document.getElementById("display").innerHTML += ",a"
    }
}

var nothing = function(e){}

var refreshInterval = setInterval(nothing, 0);

var startmoo = function(e){
    refreshInterval = setInterval(cowmoo, 300);
}

var stopmoo = function(e){
    document.getElementById("display").innerHTML = ""
    clearInterval(refreshInterval);
    moo1player.pause();
    moo2player.pause();
    moo3player.pause();
}

pos_x = cow.offsetLeft;
pos_y = cow.offsetTop;
cow.style.visibility = "hidden";
cow.style.display = "none";
button1.addEventListener('click', startmoo);
button2.addEventListener('click', stopmoo);
