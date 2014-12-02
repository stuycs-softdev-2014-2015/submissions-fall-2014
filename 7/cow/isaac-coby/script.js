var mouseX, mouseY, myevent;
var curposX, curposY = 5, 200;

var move = function(e){
    var topher = document.getElementById("topher");
    if (mouseX > curposX){
	curposX += 5;
    }
    else{
	curposX -=5;
    }
    if (mouseY > curposY){
	curposY += 5;
    }
    else{
	curposY -=5;
    }
    if ((curposX == 300) && (curposY = 200)){
	alert("You won");
    }
}

window.addEventListener('mousemove',function(e){
		mouseX = e.pageX;
		mouseY = e.pageY;
});

function startit() {
    myevent = setInterval(move,100);
}
 
document.getElementById("start").addEventListener('click',startit);
