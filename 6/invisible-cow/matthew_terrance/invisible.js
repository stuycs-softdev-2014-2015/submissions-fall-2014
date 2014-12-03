var mouseX;
var mouseY;

window.addEventListener('mousemove',function(e){
    mouseX=e.pageX;
    mouseY=e.pageY;
}); 

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
