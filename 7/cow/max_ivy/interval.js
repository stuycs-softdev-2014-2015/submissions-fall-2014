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

window.addEventListener("mousemove", checkDist);
init();
