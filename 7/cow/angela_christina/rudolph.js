//CTRL-SHIFT-J TO OPEN CONSOLE (in chrome, on linux)

var mouseX, mouseY;
var randX, randY;
var playing = false; 
var nowPlaying;
//sets our variables mouseX and mouseY to current mouse's x and y
var mouseCoord = function(e){
    mouseX = e.pageX;
    mouseY = e.pageY;
    console.log("x: " + mouseX);
    console.log("y: " + mouseY);
}

//returns a random integer from min to max inclusive
var rand = function(min, max) {
    return Math.floor(Math.random() * (max - min)) + min;
}


var placeImage = function(e){//e necessary?
    randX = rand(0,window.innerWidth);
    randY = rand(0, window.innerHeight);
    console.log("randX: " + randX);
    console.log("randX: " + randY);
}
//doesnt work lol woops
var playMusic = function(e){
    if(!playing){
	this.play();
	nowPlaying = this;
	this.addEventListener("playing",whatMusic);
    }
    else{
	nowPlaying.pause();
	this.play();
	nowPlaying = this;
	this.addEventListener("playing",whatMusic);
    
    }
}
	

    
var whatMusic = function(e){
    changeX=randX-mouseX;
    changeY=randY-mouseY;
    dist= Math.sqrt(Math.pow(changeX,2) + Math.pow(changeY,2));
    if(dist<50){
	var five= document.getElementById("five");
	playing = true;
	five.addEventListener("canplay",playMusic);
    }
    else if(dist < 250){
	var four= document.getElementById("four");
	playing = true;
	four.addEventListener("canplay",playMusic);
    }
    else if(dist < 450){
	var three= document.getElementById("three");
	playing = true;
	three.addElementListener("canplay",playMusic);
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

}	
var displayImage = function(){
    //displays the image if mouseX and mouseY are within a certain
    //range and clicked --> add element to change mouse, 
    // add source element for image
    //maybe add a fancy zoom in stuff (inc size of image)
    //increase score counter? if we feel like it?
    //use a reset function (document.body.innerHTML = "";
    //then display a replay button
    //if replay then???????????????
}

window.addEventListener('mousemove', mouseCoord);
window.addEventListener('load', placeImage);
window.addEventListener('load',whatMusic);
