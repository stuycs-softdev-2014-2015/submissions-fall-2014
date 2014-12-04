var pic = document.getElementById("batman");

var X;
var Y;
var d=2000;

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

var music = function(){

    if (d > 1000 && found == false){
	document.getElementById("sound_element").innerHTML = "<embed src='"+ "banana1.wav" +"' hidden=true autostart=true loop=false>";
    }
    if (d <= 1000 && d > 700 && found == false){
	document.getElementById("sound_element").innerHTML = "<embed src='"+ "banana2.wav" +"' hidden=true autostart=true loop=false>";
    }
    if (d <= 700 && d > 400 && found == false){
	document.getElementById("sound_element").innerHTML = "<embed src='"+ "banana.wav" +"' hidden=true autostart=true loop=false>";
    }
    if (d <= 400 && d > 100 && found == false){
	document.getElementById("sound_element").innerHTML = "<embed src='"+ "banana4.wav" +"' hidden=true autostart=true loop=false>";
    }
    if (d <= 100 && d >= 0 && found == false){
	document.getElementById("sound_element").innerHTML = "<embed src='"+ "banana5.wav" +"' hidden=true autostart=true loop=false>";
    }
};
    
		    
var checkIfFound = function(e){
    console.log("click");
    if (d <= 80){
	pic.style.visibility = "visible";
	found = true;
	if (found = true){
	    document.getElementById("sound_element").innerHTML = "<embed src='"+ "found.wav" +"' hidden=true autostart=true loop=false>";
	}
    }
}

//var playSound = function(){
//    while (found == false){
//	checkIfFound();
//	music();
//    }
//};


window.addEventListener("mousemove",getMouseCor);
//window.addEventListener("click",music);
window.addEventListener("click",checkIfFound);
