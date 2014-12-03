var mouseX;
var mouseY;

window.addEventListener('mousemove',function(e){
    mouseX=e.pageX;
    mouseY=e.pageY;
}); 

var picture=document.getElementById("picture");

function togglev(){
    picture.visibility="hidden";
};

document.getElementById("visible").addEventListener('click',togglev);
