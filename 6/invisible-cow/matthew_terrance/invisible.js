window.onload = function(){
    move.style.top = h + "px";
    move.style.left= w + "px";
};
var w = window.innerWidth *.89 - (window.innerWidth*.89 * Math.random())
var h = window.innerHeight * .89- (window.innerHeight*.89 * Math.random())
var mouseX;
var mouseY;
var button = document.getElementById("visible")
window.addEventListener('mousemove',function(e){
    mouseX=e.pageX;
    mouseY=e.pageY;
    button.value="" +distance();
});

var dist;
function distance(){
    dist=Math.sqrt(Math.pow(mouseX-(w+40),2) + Math.pow(mouseY-(h+40),2));
    console.log(dist);
};
var move = document.getElementById("move")
var picture=document.getElementById("picture");

function togglev(){
    if (picture.className == "img visible"){
	picture.className = "img hidden";
    }
    else{
	picture.className ="img visible";
    }
    
};

document.getElementById("visible").addEventListener('click',togglev);
picture.addEventListener('click',togglev);
