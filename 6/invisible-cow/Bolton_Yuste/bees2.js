var mouseX, mouseY;
var distance;
var x, y;
var image = document.getElementById("hidden");
var sound1 = document.getElementById("NotBees");
var sound2 = document.getElementById("NotThe");
var sound3 = document.getElementById("Not");
var sound4 = document.getElementById("bees");
var sound5 = document.getElementById("Cage");
var sounds = document.getElementsByTagName("audio");
console.log(sounds);
var myevent;

//get the x and y coordinates
window.addEventListener('mousemove', function(e){
    mouseX = e.pageX;
    mouseY = e.pageY;
    distance = ((mouseX - x)^2 + (mouseY - y)^2)^(0.5);
    distance = Math.abs(distance);
    console.log(distance);
})

//randomly position
var rand = function(){
    var xRand = Math.random();
    var yRand = Math.random();
    x = xRand * screen.width;
    y = yRand * screen.height;
    image.style.left = x + "px";
    image.style.top = y + "px";
    //console.log(x);
}


//the curson looks like a clicker when you click on oprah
var looking = function(){
    this.style.cursor = "pointer";
}

var play = function(){
    var noise;
    var distR = Math.abs(distance)
    if (distR >= 600){
      noise = sounds[0];
    }
    else if (distR > 400){
      noise = sounds[1];
    }
    else if (distR > 200){
      noise = sounds[2];
    }
    else if (distR > 50) {
      noise = sounds[3];
    }
    else {
      noise = sounds[4];
    }
    for (c = 0; c < sounds.length; c++){
      sounds[c].muted = true;
      sounds[c].pause();
    }
    noise.play();
    noise.muted = false;
    //console.log("play");
    myevent = setInterval(play, 1500);
}

var found = function(){
    var background = document.getElementById("body");

    background.style.backgroundImage = "url('oprah.jpg')";
    image.style.visibility = "hidden";
    for (i = 0; i < sounds.length; i++){
      sounds.pause();
      sounds.muted = true;
    }

    clearInterval(myevent);


    console.log("found");
};

rand(); //sets up the page


window.addEventListener('mouseover', play);
image.addEventListener('mouseover', looking);

image.addEventListener('click', found);
