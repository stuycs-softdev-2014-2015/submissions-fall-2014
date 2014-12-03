var myevent;

var stopTimer = function(e){
    window.clearInterval(e);
};

var mouseX, mouseY;

window.addEventListener('mousemove', function(e){
    mouseX=e.pageX;
    mouseY=e.pageY;
});

var changecolor = function(e){
    var title = document.getElementById("title");
    if (mouseX<500){
	title.class = "blue";
    } else{
	title.class = "red";
    }
}

myevent = setInterval(changecolor, 500);

window.addEventListener('mousemove',function(e){
    mouseX = e.pageX;
    mouseY = e.pageY;
});
