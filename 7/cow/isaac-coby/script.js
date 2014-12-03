var mouseX, mouseY, myEvent;
var tophX = 0;
var tophY = 200;
var moranX = 600;
var moranY = 0;
var mDirection = true;
var djX = (window.innerWidth * .9)
var djY = 200;

var move = function(e){
    if ((Math.abs(tophX - moranX) < 80) && (Math.abs(tophY - moranY) < 60)){
	var body = document.getElementsByTagName("body")[0];
	body.style.background = "url('lostmoran.jpg')";
	end()
    }

    if ((Math.abs(tophX - djX) < 70) && (Math.abs(tophY - djY) < 50)){
	var body = document.getElementsByTagName("body")[0];
	body.style.background = "url('bowl.jpg')";
	var h1 = document.getElementsByTagName("h1")[0];
	// console.log(h1);
	h1.innerHTML = "You won! Let the party live";
	end();
	
    }

    var topher = document.getElementById("topher");
    if (mouseX > tophX){
	tophX += 7;
    }
    else{
	tophX -=7;
    }
    if (mouseY > tophY){
	tophY += 7;
    }
    else{
	tophY -= 7;
    }
    topher.style.left = tophX + "px";
    topher.style.top = tophY + "px";


    var moran = document.getElementById("moran");
    if (mDirection == true){
	moranY += 14;
	if (moranY >= window.innerHeight-100){
	    mDirection = !mDirection;
	}
    }

    // console.log(window.innerHeight);

    if (mDirection == false) {
	moranY -= 14;
	if (moranY <= 0){
	    mDirection = !mDirection;
	}
    }

    moran.style.top = moranY + "px";

}

window.addEventListener('mousemove',function(e){
    mouseX = e.pageX;
    mouseY = e.pageY;
});

function begin() {
    myEvent = setInterval(move,100);
}


function end() {
    window.clearTimeout(myEvent);
    var topher = document.getElementById("topher");
    var moran = document.getElementById("moran");
    topher.style.left = "0px";
    tophX = 0;
    topher.style.top = "200px";
    tophY = 200;
    moran.style.top = "0px";
    var moranX = 600;
    var moranY = 0;
}

function restart(){
    var body = document.getElementsByTagName("body")[0];
    body.style.background = "";
    var h1 = document.getElementsByTagName("h1")[0];
    h1.innerHTML = "YOU LOST!!!! THE PARTY IS RUINED WITHOUT THE DJ.";
    end();
}

document.getElementById("start").addEventListener('click', begin);
document.getElementById("restart").addEventListener('click', restart);
