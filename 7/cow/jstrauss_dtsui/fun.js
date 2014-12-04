// Justin Strauss and Derek Tsui
// Software Development Period 7
// Invisible Cow

var mouseX, mouseY;
var dist, maxdist;
var genX, genY;
var count = 0;
/*
var bg = new Audio("theme1.mp3");

bg.addEventListener('ended', function() {
  this.currentTime = 0;
  this.play();
}, false);

bg.play();
*/
alert("Welcome to Find the Invisible Batman! To play, move your cursor around the screen to search for the invisible batman. The sound effect will become louder and more frequent as you approach the target. When you think you found him, click on the screen and if he's there, he will reveal himself.")

var updateCoords = function(e) {
    mouseX=e.pageX;
    mouseY=e.pageY;
    dist = Math.sqrt(Math.pow(mouseX-(genX+70),2)+Math.pow(mouseY-(genY+100),2));
    //console.log(dist);
}

var setup = function(e) { // create new batman in random X,Y
    document.getElementById("batman").src = "white.png";
    genX = Math.random() * screen.width; // border 140
    genY = Math.random() * screen.height; // border 200
    maxdist = Math.sqrt(Math.pow(screen.width-genX,2)+Math.pow(screen.height-genY,2));
    var move=document.querySelector('.move');
    move.style.left=genX+"px";
    move.style.top=genY+"px";
    move.style.opacity=0;
};

var reveal = function(e) {
    if(dist <= 50){
        document.getElementById("batman").src = "batman.png";
        var audio = new Audio('batman.mp3');
        audio.play();
        setTimeout(reset,2000);
        var move=document.querySelector('.move');
        move.style.opacity=1;
    };
};

var reset = function(e) {
    if (confirm("You found batman! Click OK to replay.")){
        setup();
    }
}

var radar = function(e){
    var bg=document.querySelector('bg');
    if (dist <= 50) {
        var sound = new Audio("theme4.mp3");
        document.body.style.background="#FF4D4D";
    }
    else if (dist <= 150) {
        var sound = new Audio("theme3.mp3");
        document.body.style.background="#FFFF85";
    }
    else if (dist <= 300) {
        var sound = new Audio("theme2.mp3");
        document.body.style.background="#85FF5C";
    }
    else if (dist <= 600) {
        var sound = new Audio("theme1.mp3");
        document.body.style.background="#94FFFF";
    }
    else {
        var sound = new Audio("theme1.mp3");
        document.body.style.background="#94FFFF";
    }
    sound.play();
};

var nanana = function(e){
  var na=document.getElementById("na");
  if (count < 40){
  na.innerHTML = na.innerHTML + "NA";
  count = count + 1;
} else if (count >= 40 && count < 50){
    na.innerHTML = "<center><b>Batman!!</b></center>";
    count = count + 1;
  } else if (count = 50){
    na.innerHTML = "";
    count = 0;
  }
}

var radarcheck = setInterval(radar, 1500);
var nananacheck = setInterval(nanana, 200);

setup();
window.addEventListener('mousemove',updateCoords);
window.addEventListener('click',reveal);
