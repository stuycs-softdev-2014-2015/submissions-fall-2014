
//mouse tracking
var mouseX, mouseY; 
window.addEventListener('mousemove', function(e){
    mouseX = e.pageX;
    mouseY = e.pageY;
    changeBackground()
});


//randomize pic location
//pic must be within a div (just go with it)
var pX = Math.random() * screen.width;
var pY = Math.random() * screen.height;
var image = document.getElementById("image");
image.style.marginLeft = pX;
image.style.marginTop = pY;
var audio = new Audio("03bison.mp3");
var sound = false;
var square = function(x){
    return x * x;
}

var absDist = function(x1, y1, x2, y2){
    return Math.sqrt(square(x1-x2)+square(y1-y2));
}

var changeBackground = function(e){
    var d = absDist(mouseX, mouseY, pX+75, pY+62);
    if (d >= 510){
	document.body.style.backgroundColor="white";
    }
    else{
	console.log(""+pX+" "+pY);
	document.body.style.backgroundColor = 'rgb(' + Math.floor(d/2) + ',' + Math.floor(d/2) + ',' + Math.floor(d/2) + ')';
    }
	
}



setInterval(function(){sound = true;}, 7000);
setInterval(function(){if(sound){audio.play();}}, 2500);

window.addEventListener("click", function(e){
    if(absDist(mouseX, mouseY, pX+75, pY+62) <= 50){
	image.style.visibility = "visible";
    }
}
);			
