var mouseX, mouseY;
var distance;
var x, y;
var image = document.getElementById("hidden");
var sound;
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

    if (Math.abs(distance) > 500) {
	sound = document.getElementById("first");
} else if (Math.abs(distance) > 50) {
	sound = document.getElementById("second");
    } else {
	sound = document.getElementById("third");
    }
    sound.play();
   // console.log("play");

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

myevent = setInterval(play, 100);

window.addEventListener('mouseover', play);
image.addEventListener('mouseover', looking);

image.addEventListener('click', found);
