//MAX X: 1500
//MAX Y: 500

var mouseX;
var mouseY;

var locx, locy;
locx=Math.random()*1400 + 50
locy=Math.random()*400 + 50

console.log(locx + ' ' + locy);

window.addEventListener('mousemove',function(e){
	//console.log(e.pageX+" "+e.pageY);
	mouseX=e.pageX;
	mouseY=e.pageY;
}); 

//console.log(math.random(-10,10);
var thluffy=document.getElementById("thluffy");

function move(e) {
  
  var moveelt=document.querySelector('.move');
  var x = (moveelt.style.left);
  var y = (moveelt.style.top);
  x=x.substring(0,x.length-2);
  x=parseInt(x);
  y=y.substring(0,y.length-2);
  y=parseInt(y);
   
  if (isNaN(x)) x=locx;
  if (isNaN(y)) y=locy;

  if (mouseX<x) {
     x=x-3;
     
  } else {
     x=x+3;
     
  }

  if (mouseY<y) {
     y=y-3;
  } else {
     y=y+3;
  }
  moveelt.style.left=x+"px";
  moveelt.style.top=y+"px";
}
var myevent;
myevent = setInterval(move,100);
