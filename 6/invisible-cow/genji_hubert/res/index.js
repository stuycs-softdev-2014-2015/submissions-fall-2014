var score = 0;
var mosquito;
var juice;
var x, y;
var fps = 60;

mosquito = document.createElement("img");
juice = document.createElement("img");
mosquito.setAttribute("src", "./res/mosquito.png");
mosquito.style.display = "block";
mosquito.style.position = "absolute";
mosquito.width = '20';
juice.setAttribute("src","./res/mosquito_juice.png");

document.body.appendChild(mosquito);



//Sound
//document.getElementById("hidden-sound").innerHTML= "<embed src=\"./res/sound.mp3\" hidden=\"true\" autostart=\"true\"	loop=\"true\" />";



var reload = function() {
	//console.log("reloading");
	mosquito.setAttribute("src", "./res/mosquito.png");
	mosquito.style.left = "600px";
	mosquito.style.top = "300px";
}

var winAction = function() {
	mosquito.setAttribute("src","./res/mosquito_juice.png");
	score++;
	alert("You win! Score: "+ (score));
	reload();
}

var handleMousePos = function(e) {
	x = e.clientX;
	y = e.clientY;
	//console.log("x: "+ e.clientX + "\ty: " + e.clientY);
}

var go = function() {
	//Get a random number between -0.1 and 0.1
	var k = Math.random()*100;
	var randx = k*Math.random() - k/2;
	var randy = k*Math.random() - k/2;
	//console.log("Randoms : "+randx+","+randy);

	var newx = parseFloat(mosquito.style.left) + randx;
	var newy = parseFloat(mosquito.style.top) + randy;

	if(newx < 0) newx = 0;
	if(newy < 0) newy = 0;
	if(newx > 1000) newx = 1000;
	if(newy > 800) newy = 600;

	mosquito.style.left = newx.toString() + "px";
	mosquito.style.top = newy.toString() + "px";

	setTimeout( go, 1000/fps ); //loops
}


window.addEventListener("mousemove", handleMousePos);
mosquito.addEventListener("click", winAction);
reload();
go();
