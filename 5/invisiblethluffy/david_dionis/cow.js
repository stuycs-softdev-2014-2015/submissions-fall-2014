var mouseX, mouseY;
var x,y;
var thluffy = document.getElementById("cow");


var show= function(e){
    thluffy.style.left = (window.innerWidth/2)-50;
    thluffy.style.top = (window.innerHeight/2)-50;
    thluffy.hidden=false;
    thluffy.style.height=100;
    thluffy.style.width=100;
    clearTimeout(myevent);
    document.getElementById("hint").innerHTML="You Win!";
    console.log("ran");
};


window.addEventListener('mousemove', function(e) {
    mouseX = e.pageX;
    mouseY = e.pageY;
});


window.addEventListener('click',function(e){
    if(Math.abs(e.pageX-x-25)<25 && Math.abs(e.pageY-y-25)<25){
	show();
    }
});


var placethluffy = function(e){
    i = Math.floor(Math.random()*7)+1;
    thluffy.src = "Cow/Cow"+i+".gif";
    thluffy.style.position = "absolute";
    x = Math.floor(Math.random()*(window.innerWidth-50))+25;
    y = Math.floor(Math.random()*(window.innerHeight-50))+25;
    thluffy.style.left = x;
    thluffy.style.top = y;
    thluffy.style.height=50;
    thluffy.style.width=50;
    thluffy.hidden=true;
    console.log(x+25);
    console.log(y+25);
    console.log("placed");
};
var audioplay = function (e) {
    var text;
    if(Math.abs(mouseX-x-25)<25 && Math.abs(mouseY-y-25)<25){
	text = "There!!!";
    }else if(Math.abs(mouseX-x-25)<100 && Math.abs(mouseY-y-25)<100){
	text = "Getting Really Close";
    }else if(Math.abs(mouseX-x-25)<200 && Math.abs(mouseY-y-25)<250){
	text = "Close";
    }else if(Math.abs(mouseX-x-25)<300 && Math.abs(mouseY-y-25)<400){
	text = "Far Away";
    }else if(Math.abs(mouseX-x-25)<400 && Math.abs(mouseY-y-25)<600){
	text = "Really Far Away";
    }else {
	text = "In the middle of no where!";
    }
    var place = document.getElementById("hint");
    var position = document.getElementById("xy");
    position.innerHTML="x:"+mouseX+"<br>"+"y:"+mouseY;
    place.innerHTML=text;
    if (!thluffy.hidden) {
	stopit;
    }else{
	var audio = document.getElementById("audio");
	var distance = Math.sqrt(Math.pow((mouseX - x), 2) + Math.pow((mouseY - y), 2));
	audio.volume = 50/(distance + 20);
	audio.play();
    }
}

var myevent;
var startit = function (e) {
    placethluffy();
    if (!thluffy.hidden) {
	stopit;
    }else{
	myevent = setInterval(audioplay,100);
    }
}

var stopit = function(e) {
    window.clearTimeout(myevent);
}

document.getElementById("start").addEventListener('click',startit);
document.getElementById("stop").addEventListener('click',stopit);
