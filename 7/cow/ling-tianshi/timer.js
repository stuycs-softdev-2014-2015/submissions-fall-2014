var myevent;

var stopTimer = function(e){
    window.clearInterval(e);
};

var mouseX, mouseY;

window.addEventListener('mousemove', function(e){
    mouseX=e.pageX;
    mouseY=e.pageY;
});

function calcDist(xcoord, ycoord) {
    var ret = Math.sqrt(Math.pow((xcoord-mouseX),2)+Math.pow((ycoord-mouseY),2));
    return ret;
}

function move(e) {
   var thluffy =document.getElementById("thluffy");
   var moveelt=document.querySelector('.move');
   var x = (moveelt.style.left);
   var y = (moveelt.style.top);
   x=x.substring(0,x.length-2);
   x=parseInt(x);
   y=y.substring(0,y.length-2);
   y=parseInt(y);
   
   if (isNaN(x)) x=200;
   if (isNaN(y)) y=200;
    
  if calcDist(x, y) < 50 {
      if (mouseX<x) {
	  x=x+3;
      } else {
	  x=x-3;
      }
      if (mouseY<y) {
	  y=y+3;
      } else {
	  y=y-3;
      }
  }
  else {
      if (x > 500){
	  x = x-3; }
      else { x = x+3; }
      if (y > 500){
	  y = y-3; }
      else { y = y+3; }
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
window.addEventListener('click', startit)
document.getElementById("stop").addEventListener('click',stopit);
