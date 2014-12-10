var level = 1;
var mouseX, mouseY, myEvent;
var tophX = 28;
var tophY = 200;
var moranX = 600;
var moranY = 68;
var moran2X = 600;
var moran2Y = 450;
var mDirection = true;
var djX = document.getElementById("board").offsetWidth - 98;
console.log(djX);
var djY = 200;

document.getElementById("board").style.width = (window.innerWidth - 50) + "px";
document.getElementById("board").style.height = (window.innerHeight - 80) + "px";
document.getElementById("dj").style.left = (document.getElementById("board").offsetWidth - 98) + "px";


var insideX = function(xCor){
	var minX = 28;
	var maxX = document.getElementById("board").offsetWidth - 70;
	if (xCor < minX || xCor > maxX){
		return false;
	}
	else {
		return true;
	}
};

var insideY = function(yCor){
	var minY = 60;
	var maxY = document.getElementById("board").offsetHeight - 40;
	if (yCor < minY || yCor > maxY){
		return false;
	}
	else {
		return true;
	}
};

var move = function(e){
	if ((Math.abs(tophX - moranX) < 80) && (Math.abs(tophY - moranY) < 60)){
		var body = document.getElementsByTagName("body")[0];
		body.style.background = "url('lostmoran.jpg')";
		end()
	}

	if ((Math.abs(tophX - moran2X) < 80) && (Math.abs(tophY - moran2Y) < 60) && (level == 2)){
		var body = document.getElementsByTagName("body")[0];
		body.style.background = "url('lostmoran.jpg')";
		end()
	}

	if ((Math.abs(tophX - djX) < 70) && (Math.abs(tophY - djY) < 50)){
		var body = document.getElementsByTagName("body")[0];
		body.style.background = "url('bowl.jpg')";
		var h1 = document.getElementsByTagName("h1")[0];
		if (level == 1){
			h1.innerHTML = "You won! Let the party live";
		}
		else{
			h1.innerHTML = "Sweet home Mississippi";
		}
		var start2 = document.getElementById("start2");
		start2.disabled = false;
		end();
	}

	var topher = document.getElementById("topher");
	if (mouseX > tophX && insideX(tophX + 15)){
		tophX += 15;
	}
	else {
		if (insideX(tophX - 15)){
			tophX -=15;
		}
	}
	if (mouseY > tophY && insideY(tophY+15)){
		tophY += 15;
	}
	else{
		if (insideY(tophY - 15)){
			tophY -=15;
		}
	}
	topher.style.left = tophX + "px";
	topher.style.top = tophY + "px";


	var moran = document.getElementById("moran1");
	if (mDirection == true){
		moranY += 14;
		if (moranY >= window.innerHeight-100){
			mDirection = !mDirection;
		}
	}

	if (mDirection == false) {
		moranY -= 14;
		if (moranY <= 0){
			mDirection = !mDirection;
		}
	}

	moran.style.top = moranY + "px";
	// console.log("level is " + level);
	if (level == 2){
		var moran2 = document.getElementById("moran2");
		moran2.style.visibility = "visible";
		if (moran2X > tophX){
			moran2X -= 2;
		}
		else{
			moran2X += 2;
		}
		if (moran2Y > tophY){
			moran2Y -= 2;
		}
		else{
			moran2Y += 2;
		}
		moran2.style.left = moran2X + "px";
		moran2.style.top = moran2Y + "px";
	}
}

window.addEventListener('mousemove',function(e){
	mouseX = e.pageX;
	mouseY = e.pageY;
});

function begin() {
	var h1 = document.getElementsByTagName("h1")[0];
	h1.innerHTML = "YOU LOST!!!! THE PARTY IS RUINED WITHOUT THE DJ.";
	var body = document.getElementsByTagName("body")[0];
	body.style.background = "";
	myEvent = setInterval(move,100);
}

function begin2() {
	level = 2;
    // Code to prepare level 2 game
    var dj = document.getElementById("dj");
    dj.style.visibility = "hidden";
    var miss = document.getElementById("miss");
    miss.style.visibility = "visible";
    var h1 = document.getElementsByTagName("h1")[0];
    h1.innerHTML = "You lost! You're the worst DJ on this side of the Mississippi";
    var body = document.getElementsByTagName("body")[0];
    body.style.background = "";
    myEvent = setInterval(move,100);
}


function end() {
	window.clearTimeout(myEvent);
	var topher = document.getElementById("topher");
	var moran = document.getElementById("moran1");
	var moran2 = document.getElementById("moran2");
	topher.style.left = "28px";
	tophX = 0;
	topher.style.top = "200px";
	tophY = 200;
	moran.style.top = "63px";
	var moranX = 600;
	var moranY = 0;
	moran2.style.top = "450px";
	moran2.style.left = "600px";
	var moran2X = 600;
	var moran2Y = 450;
	if (level == 2){
		moran2.style.visibility = "hidden";
		level = 1;
	}
}

function restart(){
	location.reload();
}

document.getElementById("start").addEventListener('click', begin);
document.getElementById("start2").addEventListener('click', begin2);
document.getElementById("restart").addEventListener('click', restart);
