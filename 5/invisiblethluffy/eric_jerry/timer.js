var mouseX, mouseY;

var find = function(e){
    var wherehow = document.getElementById("wherehow");
    if ( (mouseX < 10) && (mouseY < 10) ) {
	//fire
    }
    else if ( (mouseX < 50) && (mouseY < 50) ) {
	//hot
    }
    else if ( (mouseX < 100) && (mouseY < 100) ) {
	//very warm
    }
    else if ( (mouseX < 300) && (mouseY < 300) ) {
	//warm
    }
    else if ( (mouseX < 500) && (mouseY < 500) ) {
	//cool
    }
    else if ( (mouseX < 1000) && (mouseY < 1000) ) {
	//cold
    }
    else {
	//frozen
    }
}
window.addEventListener("mousemove", function(e) {
    mouseX = e.pageX;
    mouseY = e.pageY;
});

var myevent;

myevent = setTimeout(find,100)
