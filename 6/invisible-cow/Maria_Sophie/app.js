var mole_counter;
var moleX;
var moleY;

//Gets the location of the mouse
var getLocation = function(e){
    console.log(e.pageX+" "+e.pageY);
    var mouseX=e.pageX;
    var mouseY=e.pageY;
}


var startGame = function(e){
    window.addEventListener("mousemove",getLocation);
    
}

//removes the listener and should stop the moles from happening i guess
var clearGame = function(e){
    console.log("Clicked clear");
    window.removeEventListener("mousemove",getLocation);
    //idk how to remove it properly Do i needa rewrite the whole
    //function block or not????
}

//decides the mole's position but idk if it really works yet
var moveMole = function(e){
    moleX = Math.floor(Math.random() * screen.width) - 46;
    moleY = Math.floor(Math.random() * screen.height) - 60;
    
}


//buttons
var start = document.getElementById("start");
start.addEventListener("click",startGame);
var clear = document.getElementById("clear");
clear.addEventListener("click",clearGame);
