var mole_counter;
var moleX;
var moleY;
var mouseX;
var mouseY;
var hasMole; //boolean 

//Gets the location of the mouse
var getLocation = function(e){
    console.log(e.pageX+" "+e.pageY);
    mouseX=e.pageX;
    mouseY=e.pageY;
};

var removeMole = function(){
    if (document.getElementById("b") != null){
	document.getElementById("b").remove();
    }
};


var removeMole = function(){
    if (document.getElementById("b") != null){
	document.getElementById("b").remove();
    }
};

//decides the mole's position but idk if it really works yet
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
};

var onScreen = function(){
    console.log("on screen function reached");
    if (endgame){
	//something;
    }
    else if (hasMole){
	console.log("has mole");
	removeMole();
	hasMole = false;
	myevent = setTimeout(onScreen, 300);
    }else{
	console.log("no mole - false");
	makeMole();
	hasMole = true;
	myevent = setTimeout(onScreen, 300);
    } 
};

var startGame = function(e){
    window.addEventListener("click",makeMole);
    hasMole = false;
    endgame = false;
    onScreen();
};
var clearGame = function(e){
    console.log("Clicked clear");
    window.removeEventListener("click",whackMole);
    
};
var whackMole = function(e){
    
    mole_counter++;
    document.getElementById("mole_counter").appendChild(mole_counter);
}

/*var inMole = function(){
    
}*/

//buttons
var start = document.getElementById("start");
start.addEventListener("click",startGame);
var clear = document.getElementById("clear");
clear.addEventListener("click",clearGame);
