var mole_counter = 0;
var dead_moles = 0;
var hasMole; //boolean 
var whacked = false; //boolean

var removeMole = function(){
    if (document.getElementById("b") != null){
	document.getElementById("b").remove();
    }
};

var whackMole = function(e){ 
    console.log("Whack Mole");
    mole_counter++;
    document.getElementById("mole_counter").innerHTML =  mole_counter + " Moles Whacked";
    removeMole();
    whacked = true;
};


var makeMole = function(e){
    removeMole();
    newmole = document.createElement("img");
    //console.log(newmole);
    newmole.width = 60;
    newmole.height = 46;
    newmole.src = "mole.png";
    newmole.id = "b";
    moleX = Math.floor(Math.random() * (window.innerWidth - 50));
    moleY = Math.floor(Math.random() * (window.innerHeight - 80)); 
    //console.log(moleX+" "+moleY);    
    //console.log(newmole.style);
    newmole.style.marginLeft = moleX+"px";
    newmole.style.marginTop = moleY+"px";
    document.getElementById("img").appendChild(newmole);
    newmole.addEventListener("click",whackMole);
};

var clearGame = function(e){
    console.log("Clicked clear");
    removeMole();
    window.removeEventListener("click",whackMole);
    mole_counter = 0;
    dead_moles = 0;
    hasMole = false;
    document.getElementById("img").innerHTML="";
};

var onScreen = function(){
    console.log("on screen function reached");
    if (dead_moles == 3){
	var loser = document.createElement("img");
	if (mole_counter > 20)
	    loser = "star3.jpg";
	else if (mole_counter > 10)
	    loser = "star2.jpg";
	else loser = "star1.jpg";
	clearGame();
	document.getElementById("img").innerHTML = 
	    "YOU LOSE <br> <img src= "+ loser + " id=\"star\">";
    } else if (hasMole){
	console.log("has mole");
	removeMole();
	hasMole = false;
	if (whacked == false) 
	    dead_moles++;
	myevent = setTimeout(onScreen, 500);
	whacked = false;
    }else{
	console.log("no mole - false");
	makeMole();
	hasMole = true;
	myevent = setTimeout(onScreen, 2000 - mole_counter * 100);
    } 
};

var startGame = function(e){
    console.log("Start game");
    hasMole = false;
    if (document.getElementById("star")){
	document.getElementById("star").remove();
    }
    onScreen();
};


//buttons
var start = document.getElementById("start");
start.addEventListener("click",startGame);

var clear = document.getElementById("clear");
clear.addEventListener("click",clearGame);
