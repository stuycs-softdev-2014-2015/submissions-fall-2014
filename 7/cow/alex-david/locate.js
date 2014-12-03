var pic = document.getElementById("batman");

var X;
var Y;
var d;

var picX;
var picY;

var found = false;

var randomLoc = function(){
    var width = parseInt(pic.getAttribute("width"));
    var height = parseInt(pic.getAttribute("height"));
    var a  = Math.floor(Math.random() * (window.innerWidth - width));
    var b  = Math.floor(Math.random() * (window.innerHeight - height));
    picX = a + Math.ceil(width / 2);
    picY = b + Math.ceil(height / 2);
    pic.style.left = a + "px";
    pic.style.top = b + "px";
    pic.style.visibility = "hidden";
    console.log("pic x: " + picX);
    console.log("pic y: " + picY);
};

randomLoc();

var getMouseCor = function(e){
    X = e.pageX;
    Y = e.pageY;
    console.log("x: " + X + " y: " + Y);
    dist(e);
};

var dist = function(e){
    d = Math.sqrt(Math.pow(X - picX,2) + Math.pow(Y - picY,2));
    console.log("d: " + d);
};

var music = function(){//Needs Play-testing and MP3s
    if (dist > 1500){
	document.getElementById("sound_element").innerHTML= 
	    "<embed src='"+sound_file_url+"' hidden=true autostart=true loop=false>";
    }
    if (dist <= 1500 && dist > 750){
	document.getElementById("sound_element").innerHTML= 
	    "<embed src='"+sound_file_url+"' hidden=true autostart=true loop=false>";
    }
    if (dist <= 750 && dist > 400){
	document.getElementById("sound_element").innerHTML= 
	    "<embed src='"+sound_file_url+"' hidden=true autostart=true loop=false>";
    }
    if (dist <= 400 && dist >= 100){
	document.getElementById("sound_element").innerHTML= 
	    "<embed src='"+sound_file_url+"' hidden=true autostart=true loop=false>";
    }
    if (dist <= 100 && dist >= 0){
	document.getElementById("sound_element").innerHTML= 
	    "<embed src='"+sound_file_url+"' hidden=true autostart=true loop=false>";
    }
};
    
		    
var checkIfFound = function(e){
    console.log("click");
    if (d <= 80){
	pic.style.visibility = "visible";
	found = true;
    }
}

window.addEventListener("mousemove",getMouseCor);
window.addEventListener("click",checkIfFound);
