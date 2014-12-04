//CTRL-SHIFT-J TO OPEN CONSOLE (in chrome, on linux)
   //displays the image if mouseX and mouseY are within a certain
    //range and clicked --> add element to change mouse, 
    // add source element for image
    //maybe add a fancy zoom in stuff (inc size of image)
    //increase score counter? if we feel like it?
    //use a reset function (document.body.innerHTML = "";
    //then display a replay button
    //if replay then???????????????
//how to change mouse eep
var one = new Audio('sleigh_one.mp3');
var two = new Audio('sleigh_two.mp3');
var three = new Audio('sleigh_three.mp3');
var four = new Audio('sleigh_four.mp3');
var five = new Audio('sleigh_five.mp3');
var rudolph = new Audio('rudolph.mp3');
var mouseX, mouseY;
var randX, randY;
var imageH = 200;
var imageW = 150;
var centerX, centerY;
var playing = false; 
var nowPlaying;
var changeX, changeY;
var dist;
var img;
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
    if (dist < 50){
	img = document.createElement("img");
	img.src = "rudolph.png";
	img.alt = "rudolph";
	img.id = "rudolph";
	img.width = imageW;
	img.height = imageH;
	img.style.top = randY+"px";
	img.style.left = randX+"px";
	//console.log(img);
	document.body.appendChild(img);
	playMusic(rudolph);
	
	var rot = setInterval(rotate_right, 2000);    
	window.removeEventListener('click', displayImage);
	window.addEventListener('mouseover', rot);
	window.removeEventListener('mousemove', whatMusic);
	setTimeout( function(){ window.location.reload(); }, 180000);
    }
}

var rotate_right = function(e) {
    var image = document.getElementById("rudolph");
    image.width = imageW + 40;
    //console.log(image);
    image.src = "right.png";
    setTimeout(rotate_left, 2000);
}

var rotate_left = function(e) {
    var image = document.getElementById("rudolph");
    
    image.width = imageW + 40;
    //console.log(image);
    image.src = "left.png";
    setTimeout(rotate_right, 2000);
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
    
    //console.log("centerX:" + centerX);
    //console.log("centerY:" + centerY);
    //console.log("changeX:" + changeX);
    //console.log("changeY:" + changeY);
    console.log("dist: "+dist);

    if(dist<50){
	playMusic(five);
    }

    else if(dist < 250){
	playMusic(four);
    }
    else if(dist < 450){
    	playMusic(three);
    }
    else if(dist < 650){
	playMusic(two);
    }
    else {
	playMusic(one);
    }
}
/*
var cursor = function(e) {
    if (dist<50){
	console.log("change!");
	var cursor = document.getElementById("area");
	cursor.style.cursor = "pointer";
	console.log(cursor);
    }
}

var map = function(e){
    var map = document.createElement("map");
    map.id = "map";
    document.body.appendChild(map);
    var area = document.createElement("area");
    area.shape = "rect";
    var right = randX + imageW;
    var bot = randY + imageH;
    console.log(right);
    console.log(bot);
    var str = randX + "," + randY + "," + right + "," + bot;
    console.log(str);
    area.coords=str;
    var add = document.getElementById("map");
    add.appendChild(area);
    console.log(area);
}
*/
var setup = function(e){	
    //http://stackoverflow.com/questions/3273552/html-5-audio-looping
    //chooses random coords for image placement
    randX = rand(0,window.innerWidth-imageW);
    randY = rand(0, window.innerHeight-imageH);
   // console.log("randX: " + randX);
   // console.log("randY: " + randY);
    
    //finds center of image randomly placed
    centerY = randY + (imageH/2);
    centerX = randX + (imageW/2);
   // console.log("centerY: "+centerY);
   // console.log("centerX: "+centerX);

    if (typeof one.loop == 'boolean')
    {
	one.loop = true;
	two.loop = true;
	three.loop = true;
	four.loop = true;
	five.loop = true;
	rudolph.loop = true;
    }
    else
    {
	one.addEventListener('ended', loop);
	two.addEventListener('ended', loop);
	three.addEventListener('ended', loop);
	four.addEventListener('ended', loop);
	five.addEventListener('ended', loop);
	rudolph.addEventListener('ended', loop);	
    }
}

var stopT = function(e){
    window.clearInterval(e);
}

window.addEventListener('load', setup);
window.addEventListener('load', map);

window.addEventListener('mousemove', mouseCoord);
window.addEventListener('mousemove',whatMusic);
//window.addEventListener('mousemove', cursor);
window.addEventListener('click', displayImage);
