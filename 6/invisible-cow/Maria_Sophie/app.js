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


var startGame = function(e){
    window.addEventListener("mousemove",getLocation);
    //mousemove or click? 
};

//removes the listener and should stop the moles from happening i guess
var clearGame = function(e){
    console.log("Clicked clear");
    window.removeEventListener("mousemove",getLocation);
    //idk how to remove it properly Do i needa rewrite the whole
    //function block or not????
    
};

//decides the mole's position but idk if it really works yet
var makeMole = function(e){
    newmole = document.createElement("IMG");
    console.log(newmole);
    newmole.width = 60;
    newmole.height = 46;
    newmole.src = "mole.png";
    newmole.id = "b";
    moleX = Math.floor(Math.random() * screen.width ) - 46;
    moleY = Math.floor(Math.random() * screen.height) - 60; 
    console.log(moleX+" "+moleY)    
    console.log(newmole.style);
    newmole.style.margeLeft = moleX+"px";
    newmole.style.marginTop = moleY+"px";
    document.getElementById("img").appendChild(newmole);
};

var removeMole = function(){
    document.getElementById("b").remove();
};



/*var inMole = function(){
    
}*/

//buttons
var start = document.getElementById("start");
start.addEventListener("click",startGame);
var clear = document.getElementById("clear");
clear.addEventListener("click",clearGame);


window.addEventListener("click",makeMole);
