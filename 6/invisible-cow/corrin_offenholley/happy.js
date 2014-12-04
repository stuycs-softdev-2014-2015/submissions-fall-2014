//MAX X: 1500
//MAX Y: 500

var mouseX;
var mouseY;
var movedirx, movediry;
var locx, locy;
var win = false;
locx=Math.random()*1000 + 50
locy=Math.random()*400 + 50

console.log(locx + ' ' + locy);

window.addEventListener('mousemove',function(e){
	//console.log(e.pageX+" "+e.pageY);
	mouseX=e.pageX;
	mouseY=e.pageY;
}); 

//console.log(math.random(-10,10);
var thluffy=document.getElementById("thluffy");
var xdir = document.createElement('li');
var ydir = document.createElement('li');
var bunn = document.createElement('li');
var wins=0;
bunn.innerHTML=wins;

var mylist=document.getElementById('list')
function move(e) {
  
  var moveelt=document.querySelector('.move');
  var x;// = (moveelt.style.left);
  var y;// = (moveelt.style.top);
  //x=x.substring(0,x.length-2);
  //x=parseInt(x);
  //y=y.substring(0,y.length-2);
  //y=parseInt(y);
   
  if (isNaN(x)) x=locx;
  if (isNaN(y)) y=locy;

  if (mouseX<x) {
     movedirx='right'
     
  } else {
     movedirx='left'
     
  }

  if (mouseY<y) {
     movediry='down'
  } else {
     movediry='up'
  }
  //console.log(win);
  win=(mouseY-y)*(mouseY-y)+(mouseX-x)*(mouseX-x)<2000
  xdir.innerHTML=movedirx;
  ydir.innerHTML=movediry;
  //moveelt.style.left=x+"px";
  //moveelt.style.top=y+"px";
}
mylist.appendChild(xdir);
mylist.appendChild(ydir);




var clickscare = function(e){
	if (win) {
		console.log('yay');
		wins++;
		bunn.innerHTML=wins;
		locx=Math.random()*1000 + 50
		locy=Math.random()*400 + 50
		if (wins>2 && Math.random()>.5){
			console.log('SCARY!');
			console.log(Math.random());
			document.body.style.background = "#f3f3f3 url('bunny.jpeg') no-repeat left top";
			document.getElementById('audiotag1').play();
		}
	}
};
mylist.appendChild(bunn);
document.addEventListener('click',clickscare);



var myevent;
myevent = setInterval(move,100);
