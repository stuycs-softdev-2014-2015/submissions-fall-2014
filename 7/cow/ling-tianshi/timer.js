var myevent;

var stopTimer = function(e){
    window.clearInterval(e);
};

var mouseX, mouseY;

window.addEventListener('mousemove', function(e){
    mouseX=e.pageX;
    mouseY=e.pageY;
});

function move(e) {
   var thluffy =document.getElementById("thluffy");
   var moveelt=document.querySelector('.move');
   var x = (moveelt.style.left);
   var y = (moveelt.style.top);
   x=x.substring(0,x.length-2);
   x=parseInt(x);
   y=y.substring(0,y.length-2);
   y=parseInt(y);
   
   if (isNaN(x) || x > 1200 || x < -100) x=200;
   if (isNaN(y) || y < -100 || y > 1200 ) y=200;
  if (800<x) {
     x=x-3;
  } else if (x<590){
     x=x+3;
   }
  if (600<y) {
     y=y-3;
  } else if (y<500){
     y=y+3;
   }
   moveelt.style.left=x+"px";
   moveelt.style.top=y+"px";
  var deltaY = mouseY-y;
  var deltaX = mouseX-x;
  var degs=Math.atan2(deltaY,deltaX) *360 / 3.14159;
  thluffy.style.webkitTransform = "rotate("+degs+"deg)";
}

var changecolor = function(e){
    var title = document.getElementById("title");
    if (mouseX<500){
	title.class = "blue";
    } else{
	title.class = "red";
    }
}

function startit() {
 myevent = setInterval(move,100);
}
function stopit() {
	window.clearTimeout(myevent);
}
 //document.getElementById("start").addEventListener('click',startit);
document.addEventListener('click', startit())
document.getElementById("stop").addEventListener('click',stopit);
