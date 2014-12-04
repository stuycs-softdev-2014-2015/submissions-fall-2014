var mouseX, mouseY;
var hX, hY;

window.addEventListener("mousemove",function(e){
	mouseX = e.pageX;
	mouseY = e.pageY;
	
    });

var moveImage = function(){
    hX = Math.floor(Math.random()* (window.innerWidth - 50)) + 50;
    hY = Math.floor(Math.random()* (window.innerHeight - 50)) + 50;
    var img = document.getElementById("Harvard");
    hX = 0;
    hY = 0;
    img.style.top = hY + "px";
    img.style.left = hX + "px";
};



window.addEventListener("click", function(e){
	if( mouseX >= (hX-50) &&  mouseX <= (hX+50) &&  mouseY >= (hY-50) && mouseY <= (hY+50) ){
	    var img = document.getElementById("Harvard");
	    img.style.visibility = "visible"
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


    
