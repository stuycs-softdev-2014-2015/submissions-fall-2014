var mouseX, mouseY;

var findTree = function(e) {
    var tree = document.createElement("IMG");
    tree.setAttribute("src", "tree.jpeg");
    tree.setAttribute("width", "naturalWidth");
    tree.setAttribute("height", "naturalHeight");
    var left = Math.random( 
   }

window.addEventListener('mousemove', function(e) {
    mouseX = e.pageX;
    mouseY = e.pageY;
});

var myevent;

function start(){
    myevent = setInterval(findTree,100);
}

function stop(){
    window.clearTimeout(myevent);
}

document.getElementById("start").addEventListener('click',start);
document.getElementById("stop").addEventListener('click',stop);
