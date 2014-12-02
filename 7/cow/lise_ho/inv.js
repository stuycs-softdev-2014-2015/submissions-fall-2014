//MOZILLA FIREFOX doesnt like this javascript... :(
//bouncey balls???

var tracker = document.getElementById("tracker");
var dista = document.getElementById("dist");
var mouseX, mouseY;

var sq = function(d){
    return Math.pow(d,2);
};
var dist = function(x1, y1, x2,y2){
    return Math.sqrt(sq(y2-y1)+ sq(x2-x1));
};
    

window.addEventListener('mousemove',function(e){
    mouseX = e.pageX;
    mouseY = e.pageY;
    tracker.innerText= mouseX +"," + mouseY;
    dista.innerText= dist(mouseX,mouseY,5,5).toString();
    console.log(dist(mouseX,mouseY,5,5));
});


