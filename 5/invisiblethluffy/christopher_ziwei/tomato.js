var mouseX , mouseY;
var tomato = document.createElement("img");
tomato.src = "tomato.png";
tomato.width = 50;
tomato.height = 50;
var start = document.getElementById("start");
var tomatox , tomatoy;
var globaldistance;

var create_tomato = function() {
    this.remove();
    var x = Math.round(Math.random() * window.innerWidth);
    var y = Math.round(Math.random() * window.innerHeight);
    tomatox = x; tomatoy = y;
    console.log(x);
    console.log(y);
    tomato.style.position = "absolute";
    tomato.style.top = y + "px";
    tomato.style.left = x + "px";
    tomato.style.visibility = "hidden";
    document.body.appendChild(tomato);
    var event = setInterval(distance, 100);
}

var win = function(){
    if (globaldistance < 25){
	document.body.removeChild(tomato);
	tomato.style.visibility = "visible";
	document.body.appendChild(tomato);
	document.body.appendChild(start);
    }
}    

window.addEventListener('click' , win);
window.addEventListener('mousemove', function(e){
    mouseX = e.pageX;
    mouseY = e.pageY;
});

var event;
var distance = function(){
    var space = Math.sqrt(Math.pow((mouseX - tomatox) , 2) + 
		 Math.pow((mouseY - tomatoy) , 2));
    globaldistance = space;
    var d = document.getElementById("h1");
    d.innerHTML = space + "";
}

start.addEventListener('click', create_tomato);
