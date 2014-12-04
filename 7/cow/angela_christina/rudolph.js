//CTRL-SHIFT-J TO OPEN CONSOLE (in chrome, on linux)
   //displays the image if mouseX and mouseY are within a certain
    //range and clicked --> add element to change mouse, 
    // add source element for image
    //maybe add a fancy zoom in stuff (inc size of image)
    //increase score counter? if we feel like it?
    //use a reset function (document.body.innerHTML = "";
    //then display a replay button
    //if replay then???????????????
var one = new Audio('sleigh_one.mp3');
var two = new Audio('sleigh_two.mp3');
var three = new Audio('sleigh_three.mp3');
var four = new Audio('sleigh_four.mp3');
var five = new Audio('sleigh_five.mp3');
var mouseX, mouseY;
var randX, randY;
var imageH = 200;
var imageW = 150;
var centerX, centerY;
var playing = false; 
var nowPlaying;
//sets our variables mouseX and mouseY to current mouse's x and y

var loop = function(e) {
    this.currentTime = 0;
    this.play();
};

var mouseCoord = function(e){
    mouseX = e.pageX;
    mouseY = e.pageY;
    //console.log("x: " + mouseX);
    //console.log("y: " + mouseY);
}

//returns a random integer from min to max inclusive
var rand = function(min, max) {
    return Math.floor(Math.random() * (max - min)) + min;
}

//adds an image tag to our html document
var displayImage = function(e) {
    var img = document.createElement("img");
    img.src = "rudolph.png";
    img.alt = "rudolph";
    img.id = "rudolph";
    img.width = imageW;
    img.height = imageH;
    img.style.top = randY+"px";
    img.style.left = randX+"px";
    //console.log(img);
    document.body.appendChild(img);
}
//once per load, generates random X/Y coordinates for our image
var placeImage = function(e){
    randX = rand(0,window.innerWidth-imageW);
    randY = rand(0, window.innerHeight-imageH);
    //console.log("randX: " + randX);
    //console.log("randY: " + randY);
}

//returns the general-ish coordinates of middle of our pcitures
var centerPos = function(e){
    centerY = randY + (imageH/2);
    centerX = randX + (imageW/2);
    console.log("centerY: "+centerY);
    console.log("centerX: "+centerX);
}
	    
var playMusic = function(audio){
    if (playing){	    
	//console.log("nowPlaying: " + nowPlaying);
	nowPlaying.pause();
    }
    else {
	playing = true;
    }
    nowPlaying = audio;
    audio.play();
}
      
var whatMusic = function(e){
    changeX=centerX-mouseX;
    changeY=centerY-mouseY;
    dist= Math.sqrt(Math.pow(changeX,2) + Math.pow(changeY,2));
    console.log("dist: "+dist);

    if(dist<50){
	


	else if(dist < 250){
	if (playing){
	   // console.log("nowPlaying: " + nowPlaying);
	    nowPlaying.pause();
	}
	else {
	    playing = true;
	}
	
	nowPlaying = four;
	four.play();
}
/*
    else if(dist < 450){
	var three= document.getElementById("three");
	playing = true;
	three.addEventListener("canplay",playMusic);
    }
    else if(dist < 650){
	var two= document.getElementById("two");
	playing = true;
	two.addEventListener("canplay",playMusic);
    }
    else{
	var one = document.getElementById("one");
	playing = true;
	one.addEventListener("canplay",playMusic);
    }
*/
}	
//http://stackoverflow.com/questions/3273552/html-5-audio-looping
if (typeof one.loop == 'boolean')
{
    one.loop = true;
    two.loop = true;
    three.loop = true;
    four.loop = true;
    five.loop = true;
}
else
{
    one.addEventListener('ended', loop);
    two.addEventListener('ended', loop);
    three.addEventListener('ended', loop);
    four.addEventListener('ended', loop);
    five.addEventListener('ended', loop);

}
window.addEventListener('mousemove', mouseCoord);
window.addEventListener('load', placeImage);
window.addEventListener('load', displayImage);
window.addEventListener('load', centerPos);
window.addEventListener('mousemove',whatMusic);
