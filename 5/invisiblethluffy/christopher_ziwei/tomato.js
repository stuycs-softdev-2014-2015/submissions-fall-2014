var mouseX , mouseY;
var tomato = document.createElement("img");
tomato.src = "tomato.png";
tomato.width = 50;
tomato.height = 50;
tomato.addEventListener('click' , win);
var start = document.getElementById("start");

var create_tomato = function() {
    this.remove();
    var x = Math.round(Math.random() * window.innerWidth);
    var y = Math.round(Math.random() * window.innerHeight);
    console.log(x);
    console.log(y);
    tomato.style.position = "absolute";
    tomato.style.top = y + "px";
    tomato.style.left = x + "px";
    tomato.style.visibility = "hidden";
    document.body.appendChild(tomato);
}

var win = function(){
}    

window.addEventListener('mousemove', function(e){
    mouseX = e.pageX;
    mouseY = e.pageY;
});



start.addEventListener('click', create_tomato);
