var mouseX;
var mouseY;

window.addEventListener('mousemove',function(e){
    mouseX=e.pageX;
    mouseY=e.pageY;
}); 

var picture=document.getElementById("picture");

function togglev(){
    if (picture.style.visibility=="hidden"){
	picture.style.visibility="";
    }
    else{
	picture.style.visibility="hidden";
    }
    
};

document.getElementById("visible").addEventListener('click',togglev);
picture.addEventListener('click',togglev);
