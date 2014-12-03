
//mouse tracking
var mouseX, mouseY; 
window.addEventListener('mousemove', function(e) {
		mouseX = e.pageX;
		mouseY = e.pageY;
});
window.addEventListener("mousemove", changeBackground)


//randomize pic location
//pic must be within a div (just go with it)
var pX = Math.random() * screen.width;
var pY = Math.random() * screen.height;
document.getElementById("image").style.marginLeft = pX;
document.getElementById("image").style.marginTop = pY;
var audio = new Audio("03bison.mp3");
var sound = false;

var square = function(x){
    return x * x;
}

var absDist = function(x1, y1, x2, y2){
    return Math.sqrt(square(x1-x2)+square(y1-y2));
}

var changeBackground = function(e){
    if (absDist(mouseX, mouseY, pX, pY) <= 15){
	//change background to pure black
	return;
    }
    return
}



setInterval(function(){sound = true;}, 7000);
setInterval(function(){if(sound){audio.play();}}, 2500);
