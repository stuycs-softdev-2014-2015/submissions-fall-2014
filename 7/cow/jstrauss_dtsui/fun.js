// Justin Strauss and Derek Tsui
// Software Development Period 7
// Invisible Cow

var mouseX, mouseY;
var dist, maxdist;
var genX, genY;

alert("Welcome to Find the Invisible Batman! To play, move your cursor around the screen to search for the invisible batman. The sound effect will become louder and more frequent as you approach the target. When you think you found him, click on the screen and if he's there, he will reveal himself.")

var updateCoords = function(e) {
    mouseX=e.pageX;
    mouseY=e.pageY;
    dist = Math.sqrt(Math.pow(mouseX-(genX+70),2)+Math.pow(mouseY-(genY+100),2));
    console.log(dist);
}

var setup = function(e) { // create new batman in random X,Y
    document.getElementById("batman").src = "white.png";
    genX = Math.random() * screen.width; // border 140
    genY = Math.random() * screen.height; // border 200
    maxdist = Math.sqrt(Math.pow(screen.width-genX,2)+Math.pow(screen.height-genY,2));
    var move=document.querySelector('.move');
    move.style.left=genX+"px";
    move.style.top=genY+"px";
};

var reveal = function(e) {
    if(dist <= 50){
        document.getElementById("batman").src = "batman.png";
        var audio = new Audio('batman.mp3');
        audio.play();
        setTimeout(reset,2000);
    };
};

var reset = function(e) {
    if (confirm("You found batman! Click OK to replay.")){
        setup();
    }
}

var radar = function(e){
    if (dist <= 50) {
        var sound = new Audio("batman.mp3");
    }
    else if (dist <= 100) {
        var sound = new Audio("batman.mp3");
    }
    else if (dist <= 200) {
        var sound = new Audio("batman.mp3");
    }
    else if (dist <= 400) {
        var sound = new Audio("batman.mp3");
    }
    else {
        var sound = new Audio("batman.mp3");
    }
    //sound.play();
};

var radarcheck = setInterval(radar,1000);

setup();
window.addEventListener('mousemove',updateCoords);
window.addEventListener('click',reveal);