var IMG_COUNT = 3;
var cowx = 0;
var cowy = 0;
var baseInterval = 200;
var interval = baseInterval;
var state = 0;
var spawnWindows;
var audioPanic;

var init = function(){
    var html = document.documentElement;
    var height = html.clientHeight;
    var width = html.clientWidth;
    console.log("H: " + height + " W: " + width);
    cowx = Math.random() * width;
    cowy = Math.random() * height;
    console.log("x: " + cowx + " y: " + cowy);
    
}

var d;
var checkDist = function(e){
    var counter = document.getElementById("distance");
    d = Math.sqrt(Math.pow(cowx - e.pageX, 2)+Math.pow(cowy - e.pageY, 2));
    counter.innerHTML = d;
}

var displayRandomImage = function(){
    //adjustInterval;
    begin();
    var src = "img" + Math.floor(Math.random()*IMG_COUNT) + ".jpg";    
    var top = Math.floor(Math.random()*document.documentElement.clientHeight) - 100 + "px";
    var right = Math.floor(Math.random()*document.documentElement.clientWidth) - 100 + "px";
    displayImage(src,top,right, NaN, NaN);
    //console.log(interval);
}

var displayImage = function(src, top, right, cursor, z){
    var img = document.createElement("img");
    img.src = src;
    img.style.position = "fixed";
    img.style.top = top;
    img.style.right = right;
    document.body.appendChild(img);
    if(z != NaN){
    	img.style.zIndex = z
    }
    if (cursor != NaN){ //not good check
	    img.style.cursor = cursor;
    }
}

var adjustInterval = function(){
    interval = baseInterval * (d / 400);
    if(interval < 50){
	    interval = 50;
    }
}


var begin = function(){
    if(state == 0){ //spamming windows
	    clearInterval(spawnWindows);
	    adjustInterval();
	    console.log(interval);
	    spawnWindows = setInterval(displayRandomImage,interval);
    }
    else if (state == 1){ //user clicked, start spamming xbox
	    clearInterval(spawnWindows);
	    displayImage("xbox.jpg", 0, 0, "crosshair", 99999);
	    state = 2;
	    setTimeout(function(){ begin() }, 3000); //begin panic timer
    }
    else if (state == 2){ //audio starts panicking
	    console.log("Made it to " + state + "!");
	    //audioPanic =
	    setTimeout(setInterval(displayImage("xbox.jpg", Math.floor(Math.random() * 500), Math.floor(Math.random() * 500), "text", 9), 50), 3000);
	    state = 3;
	    setTimeout( function(){ begin() }, 3000);
    }
    else if (state == 3){ //KERNEL PANIC
	    console.log("OH GOD");
    }
}

var button = document.getElementById("begin");
button.addEventListener("click", begin);
window.addEventListener("mousemove", checkDist);
init();

//spawnWindows = setInterval(displayRandomImage,100);

