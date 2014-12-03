var mouseX;
var mouseY;
window.addEventListener('mousemove',function(e){
mouseX=e.pageX;
mouseY=e.pageY;
}); 

function found() {
var list = document.getElementsByTagName('h1')[0];
var newitem = document.createElement('h1');
newitem.innerHTML="You Found Thluffy";
list.appendChild(newitem);
}

function distance(x1,y1, x2, y2){
    return Math.sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1));
}


function random() {
var thluffy=document.getElementById("thluffy");
thluffy.style.left= Math.floor((Math.random() * 1300) + 1) + "px"; 
thluffy.style.top= Math.floor((Math.random() * 200) + 300) + "px"; 
}

function resize() {
var thluffy = document.getElementById("thluffy");
var left = thluffy.style.left;
var top = thluffy.style.top;
left = parseInt(left.substring(0, left.length-2));
top = parseInt(top.substring(0, top.length-2));

var eyes = document.getElementById("eyes");
var width = eyes.style.width;

var dist = distance(left+210, top+220, mouseX, mouseY);
console.log(dist);
console.log(width);
eyes.style.width = (700-dist) + "px";

return dist;
}

var myevent;
function startit() {
myevent = setInterval(resize,100);
}

function stopit() {
window.clearTimeout(myevent);
}


random();
document.getElementById("thluffy").addEventListener('click',found,random);
document.getElementById("start").addEventListener('click',startit);
document.getElementById("stop").addEventListener('click',stopit);