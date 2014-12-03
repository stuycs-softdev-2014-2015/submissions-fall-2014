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
    console.log(e.pageX + " " + e.pageY);
    var counter = document.getElementById("distance");
    var d = Math.sqrt(Math.pow(cowx - e.pageX, 2)+Math.pow(cowy - e.pageY, 2));
    console.log(d);
    counter.innerHTML = d;
}

var displayImage = function(){
    console.log(image);
    //var img = document.createElement("img");
    var src + "img" + Math.floor(Math.random()*2) + ".jpg";
    var img = document.createElement(src);
    img.style.position = "absolute";
    img.style.top=Math.floor(Math.random()*document.documentElement.clientHeight);
    img.style.right=Math.floor(Math.random()*document.document.Element.clientWidth);
    document.body.appendChild(img);
}

window.addEventListener("mousemove", checkDist);
init();
