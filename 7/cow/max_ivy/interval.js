var IMG_COUNT = 3;
var cowx = 0;
var cowy = 0;

var init = function(){
    var html = document.documentElement;
    var height = html.clientHeight;
    var width = html.clientWidth;
    console.log("H: " + height + " W: " + width);
    cowx = Math.random() * width;
    cowy = Math.random() * height;
    console.log("x: " + cowx + " y: " + cowy);
}

var checkDist = function(e){
    //console.log(e.pageX + " " + e.pageY);
    var counter = document.getElementById("distance");
    var d = Math.sqrt(Math.pow(cowx - e.pageX, 2)+Math.pow(cowy - e.pageY, 2));
    console.log(d);
    counter.innerHTML = d;
}


var displayRandomImage = function(){
    var src = "img" + Math.floor(Math.random()*IMG_COUNT) + ".jpg";    
    var top = Math.floor(Math.random()*document.documentElement.clientHeight) - 100 + "px";
    var right = Math.floor(Math.random()*document.documentElement.clientWidth) - 100 + "px";
    displayImage(src,top,right);
}

var displayImage = function(src, top, right){
    var img = document.createElement("img");
    img.src = src;
    img.style.position = "fixed";
    img.style.top = top;
    img.style.right = right;
    document.body.appendChild(img);
}

var spawnWindows;
spawnWindows = setInterval(displayRandomImage,100);

window.addEventListener("mousemove", checkDist);
init();
