var IMG_COUNT = 3;
var cowx = 0;
var cowy = 0;
var baseInterval = 350;
var interval = baseInterval;
var state = 0;
var spawnWindows;
var audioPanic;
var error, congrats;

var init = function(){
    var html = document.documentElement;
    var height = html.clientHeight;
    var width = html.clientWidth;
    console.log("H: " + height + " W: " + width);
    cowx = Math.random() * width;
    cowy = Math.random() * height;
    console.log("x: " + cowx + " y: " + cowy);
    error = new Audio("error.mp3");
    congrats = new Audio("congrats.mp3");

};

var d;
var checkDist = function(e){
    //var counter = document.getElementById("distance");
    d = Math.sqrt(Math.pow(cowx - e.pageX, 2)+Math.pow(cowy - e.pageY, 2));
    //counter.innerHTML = d;
    console.log(d);
};

var displayRandomImage = function(){
    //adjustInterval;
    begin();
    var src = "img" + Math.floor(Math.random()*IMG_COUNT) + ".jpg";    
    var top = Math.floor(Math.random()*document.documentElement.clientHeight) - 100 + "px";
    var right = Math.floor(Math.random()*document.documentElement.clientWidth) - 100 + "px";
    displayImage(src,top,right, NaN, NaN);
    error.pause();
    error.currentTime = 0;
    error.play();
    //console.log(interval);
};

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
};

var adjustInterval = function(){
    interval = baseInterval * (d / 400);
    if(interval < 50){
    	interval = 50;
    }
};

var checkClick = function(e){
    if(d < 50 && state == 0){
        state = 1;
        console.log("Found the Xbox!");
    } else {
        console.log("No cigar for you!");
    }
};

var displayRandomXbox = function(){
    congrats.pause();
    congrats.currentTime = 0;
    congrats.play();
    displayImage("xbox.jpg", Math.floor(Math.random() * document.documentElement.clientHeight) + "px", Math.floor(Math.random() * document.documentElement.clientWidth) + "px", "text",11);
};

var begin = function(){
    if(state == 0){ //spamming windows
    	clearInterval(spawnWindows);
        adjustInterval();
        //console.log(interval);
        spawnWindows = setInterval(displayRandomImage,interval);
    }
    else if (state == 1){ //"xbox" appears 
    	clearInterval(spawnWindows);
    	displayImage("xbox.jpg", 0, 0, "crosshair", 10);
        congrats.play();
    	state = 2;
    	setTimeout(function(){ begin() }, 3000); //begin panic timer
    }
    else if (state == 2){ //comp starts spazzing
    	console.log("Made it to " + state + "!");
        var intID = setInterval(displayRandomXbox, 500);
        console.log("IntID: " + intID);
    	setTimeout(function(){
            clearInterval(intID);
        }, 3000);
    	state = 3;
    	setTimeout( function(){ begin() }, 5000);
    }
    else if (state == 3){ //KERNEL PANIC
    	console.log("OH GOD");
        //displayImage("bsod.jpg",0,0,NaN,100000);
        var img = document.createElement("img");
        img.src = "bsod.jpg";
        img.style.position = "fixed";
        img.style.top = 0;
        img.style.left = 0;
        img.style["z-index"] = 10000;
        img.style["max-width"] = "100%";
        document.body.appendChild(img);
    }
};

var button = document.getElementById("begin");
button.addEventListener("click", begin);
window.addEventListener("mousemove", checkDist);
window.addEventListener("click", checkClick);
init();

//spawnWindows = setInterval(displayRandomImage,100);

