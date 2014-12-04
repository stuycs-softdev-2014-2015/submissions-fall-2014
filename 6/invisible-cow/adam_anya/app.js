var img = document.getElementById("img");
var imgX = document.getElementById("img").x;
var imgY = document.getElementById("img").y;
var mouseX = 0;
var mouseY = 0;

var distance = function(e) {
    //var body = document.getElementById("body");
    var body = document.body.style.background;
    console.log(body);
    mouseX = e.pageX;
    mouseY = e.pageY;
    //console.log(mouseX);
    //console.log(mouseY);
    dist = Math.sqrt(
	Math.pow(mouseX - imgX, 2) +
	    Math.pow(mouseY - imgY, 2)
    )
    console.log(dist);
    if (dist < 500){
	//body.background-size = "15px 15px";
	body = 'url("2048.png")';
    }
}

document.addEventListener("mousemove", distance);


