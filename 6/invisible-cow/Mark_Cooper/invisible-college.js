var mouseX, mouseY;
var hX, hY;
var img = document.getElementById("Harvard");


window.addEventListener("mousemove",function(e){
	mouseX = e.pageX;
	mouseY = e.pageY;

	var study = document.getElementById("Study");
	var distance = Math.sqrt(Math.pow((mouseX - hX),2) + Math.pow((mouseY - hY),2));
	var sX, sY;
	if (distance < 100){
	    sX = 500;
	    sY = 100;
	}else if(distance < 200){
	    sX = 400;
	    sY = 80;
	}else if(distance < 300){
	    sX = 350;
	    sY = 70;
	}else if(distance < 400){
	    sX = 300;
	    sY = 60;
	}else if(distance < 500){
	    sX = 250;
	    sY = 50;
	}else if(distance < 600){
	    sX = 200;
	    sY = 40;
	
	}else if(distance < 1000){
	    sX = 200;
	    sY = 33;
	}else if(distance < 2000){
	    sX = 100;
	    sY = 17;
	}
	study.style.height= sY + "px";
	study.style.width = sX + "px";
	
    });




var moveImage = function(){
    hX = Math.floor(Math.random()* (window.innerWidth - 25));
    hY = Math.floor(Math.random()* (window.innerHeight - 25));
    if (hX < 25){
	hX = 25;
    }
    if (hY < 100){
	hY = 100;
    }
		  
    
    img.style.top = hY + "px";
    img.style.left = hX + "px";

    var win = document.getElementById("victory").style.visibility = "hidden";
    img.style.visibility="hidden";
    var img2 = document.getElementById("middle");
    img2.style.visibility = "hidden"
};



window.addEventListener("click", function(e){
	if( mouseX >= (hX-50) &&  mouseX <= (hX+50) &&  mouseY >= (hY-50) && mouseY <= (hY+50) ){

	    img.style.visibility = "visible";
	    var img2 = document.getElementById("middle");
	    img2.style.visibility = "visible"
	    var win = document.getElementById("victory");
	    win.style.visibility = "visible"

	    
	    img.style.visibility = "visible";
	    console.log("Winner");
	}
	else{
	    console.log("No Win");		
	    console.log(mouseX);
	    console.log(hX);
	    console.log(mouseY);

	}
    });


    
var newGame = function(){
    //    img.style.visibility = "hidden";
    moveImage()

}






