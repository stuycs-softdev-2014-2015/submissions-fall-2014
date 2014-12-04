var img = document.getElementById("img");
var imgX = document.getElementById("img").x;
var imgY = document.getElementById("img").y;
var mouseX = 0;
var mouseY = 0;

var distance = function(e) {
    //var body = document.getElementById("body");
    var body = document.getElementsByTagName("body")[0].style
    mouseX = e.pageX;
    mouseY = e.pageY;
    //console.log(mouseX);
    //console.log(mouseY);
    dist = Math.sqrt(
	Math.pow(mouseX - imgX, 2) +
	    Math.pow(mouseY - imgY, 2)
    )
    console.log(dist);
    if (dist < 5){
	body.backgroundImage = 'url("2048.png")';
    }
    else if (dist < 20){
	body.backgroundImage = 'url("1024.png")';
    }
    else if (dist < 40){
	body.backgroundImage = 'url("512.png")';
    }
    else if (dist < 80){
	body.backgroundImage = 'url("256.png")';
    }
    else if (dist < 160){
	body.backgroundImage = 'url("128.png")';
    }
    else if (dist < 320){
	body.backgroundImage = 'url("64.png")';
    }
    else {
	body.backgroundImage = 'url("32.png")';
    }
}

document.addEventListener("mousemove", distance);


