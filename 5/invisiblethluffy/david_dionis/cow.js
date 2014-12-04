var mouseX, mouseY;
var x,y;
var thluffy = document.getElementById("cow");

var placethluffy = function(e){
    var i = Math.floor(Math.random()*8)+1;
    thluffy.src = "static/Cow1.gif";
    x = Math.floor(Math.random()*window.innerWidth);
    y = Math.floor(Math.random()*window.innerHeight);
    thluffy.style.left = x;
    thluffy.style.top = y;
    thluffy.style.visibility = "visible";
    thluffy.addEventListener('click',show);
}

var show= function(e){
    thluffy.style.visibility = "visible";
}

var audioplay = function (e) {
    if (thluffy.style.visibility == "visible") {
	stopit;
    }
    else{
	var audio = document.getElementById("audio");
	var distance = Math.sqrt(Math.pow((mouseX - x), 2) + Math.pow((mouseY - y), 2));
	audio.volume = 5000/(distance + 20);
	audio.play();
    }
}

var loc = function(e){
    var text;
    if((mouseX-x+mouseY-y)<100){
	text = "Getting really Close!";
    }else if ((mouseX-x+mouseY-y)<500){
	text = "Close";
    }
    var place = document.getElementById("h3");
    place.innerHTML=text;
};


window.addEventListener('mousemove', function(e) {
    mouseX = e.pageX;
    mouseY = e.pageY;
});

var myevent;
var startit = function (e) {
    placethluffy;
    if (thluffy.style.visibility == "visible") {
	stopit;
    }
    else{
	myevent = setInterval(audioplay,100);
    }
}

var stopit = function(e) {
    window.clearTimeout(myevent);
}

document.getElementById("start").addEventListener('click',startit);
document.getElementById("stop").addEventListener('click',stopit);

