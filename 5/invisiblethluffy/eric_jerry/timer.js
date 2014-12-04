var eX, eY;
var wherehow = document.getElementById("wherehow");
var where = document.getElementById("where");
var whenhow = document.getElementById("whenhow");


window.addEventListener('mousemove', function(e) {
    eX = e.pageX;
    eY = e.pageY;
});

var sound = function(e){
    var x = wherehow.offsetLeft;
    var y = wherehow.offsetTop;
    var mouseX = Math.abs(eX-x);
    var mouseY = Math.abs(eY-y);
    var dist = Math.sqrt(mouseX*mouseX + mouseY*mouseY)/1000
    var readjustedDist = 1.0 - dist%1000.0

    where.volume = readjustedDist;    
    where.play();
    
}

var find = function(e){
    var x = wherehow.offsetLeft;
    var y = wherehow.offsetTop;
    var mouseX = Math.abs(eX-x);
    var mouseY = Math.abs(eY-y);
    if ( (mouseX < 10) && (mouseY < 10) ) {
	//fire
	document.body.style.background = "#FFFFFF";
	whenhow.volume = 1.0;
	whenhow.play();
	wherehow.style.visibility = "visible";
	window.alert("Where how? WHEN HOW!");	
    }
    else if ( (mouseX < 30) && (mouseY < 30) ) {
	//hot
	document.body.style.background = "#F0F0F0";
    }
    else if ( (mouseX < 50) && (mouseY < 50) ) {
	//very warm
	document.body.style.background = "#E0E0E0";
    }
    else if ( (mouseX < 100) && (mouseY < 100) ) {
	//warm
	document.body.style.background = "#D0D0D0";
    }
    else if ( (mouseX < 150) && (mouseY < 150) ) {
	//warm
	document.body.style.background = "#C0C0C0";
    }
    else if ( (mouseX < 200) && (mouseY < 200) ) {
	//warm
	document.body.style.background = "#B0B0B0";
    }
    else if ( (mouseX < 250) && (mouseY < 250) ) {
	//warm
	document.body.style.background = "#A0A0A0";
    }
    else if ( (mouseX < 300) && (mouseY < 300) ) {
	//warm
	document.body.style.background = "#909090";
    }
    else if ( (mouseX < 350) && (mouseY < 350) ) {
	//warm
	document.body.style.background = "#808080";
    }
    else if ( (mouseX < 400) && (mouseY < 400) ) {
	//cool
	document.body.style.background = "#707070";
    }
    else if ( (mouseX < 450) && (mouseY < 450) ) {
	//warm
	document.body.style.background = "#606060";
    }
    else if ( (mouseX < 500) && (mouseY < 500) ) {
	//cold
	document.body.style.background = "#505050";
    }
    else if ( (mouseX < 600) && (mouseY < 600) ) {
	//cold
	document.body.style.background = "#404040";
    }
    else if ( (mouseX < 700) && (mouseY < 700) ) {
	//cold
	document.body.style.background = "#303030";
    }
    else if ( (mouseX < 800) && (mouseY < 800) ) {
	//cold
	document.body.style.background = "#202020";
    }
    else if ( (mouseX < 900) && (mouseY < 900) ) {
	//cold
	document.body.style.background = "#101010";
    }
    else {
	//frozen
	document.body.style.background = "#000000";
    }
}

var myevent;

var startt = function(){
    document.body.style.background = "#000000";
}

var startit = function(){ 
    wherehow.setAttribute('height', '50px');
    wherehow.setAttribute('width', '100px');
    wherehow.style.position = 'absolute';
    wherehow.style.visibility = 'hidden';
    wherehow.style.left = 50 + Math.random()*1000 +'px';
    wherehow.style.top = 50 + Math.random()*500 + 'px';

    myevent = setInterval(find, 100);
    myevent = setInterval(sound, 100);


}

var stopit = function(){
    document.body.style.background = "#FFFFFF"
    window.clearTimeout(myevent);
}

document.getElementById("start").addEventListener('click', startit);
document.getElementById("stop").addEventListener('click', stopit);
wherehow.addEventListener('click', done);
