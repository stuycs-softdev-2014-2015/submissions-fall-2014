var mouseX,mouseY;
var hX, hY;
window.addEventListener("mousemove",function(e){
		// console.log(e.pageX+" "+e.pageY);
		mouseX = e.pageX;
		mouseY = e.pageY;
    
});



var moveImage = function(){
    hX = Math.floor(Math.random()* (window.innerWidth - 50)) + 50;
    hY = Math.floor(Math.random()* (window.innerHeight - 50)) + 50;

    var img = document.getElementById("Harvard");
    img.style.top = hY + "px";
    img.style.left = hX + "px";
};

var appear = document.querySelector(".img");
document.addEventListener("click", function(e){
   if( mouseX >= (hX-50) &&  mouseX <= (hX+50) &&  mouseY >= (hY-50) && mouseY <= (hY+50) ){
       appear.style.display = "none"
       console.log("Winner")
   }
   else{
       console.log("No Win")
       
       console.log(mouseX)
       console.log(hX)
       console.log(mouseY)
       console.log(hY)
   }
});

   /* var xPosition = e.clientX
    var yPosition = e.clientY
    console.log(xPosition)
    console.log(yPosition)*/



var go = function(){
    moveImage
}

    
