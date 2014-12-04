var mouseX, mouseY, hedgehogX, hedgehogY;
var hedgehog = document.getElementById("hedgehog");
var jingles = document.getElementById("jingles");

//Setting coordinates of hedgehog at random
hedgehogY = Math.random() * window.innerHeight * .9;
hedgehogX = Math.random() * window.innerWidth * .9;
hedgehog.style.top = hedgehogY + "px";
hedgehog.style.left = hedgehogX + "px";

//Hiding hedgehog
hedgehog.style.visibility = "hidden";

///Adding event listener to hedgehog. Will become visible once clicked.
var reveal = function(e) {
    hedgehog.style.visibility = "visible";
    console.log("FOUND IT");
};

//determines if the mouse is on the hedgehog 
var mouseOnImg = function() {
	if (mouseX > hedgehogX && mouseX < 150 + hedgehogX) {
		if (mouseY > hedgehogY && mouseY < 100 + hedgehogY) {
			return true;
		}
	}
	return false;
}

/*reveals hedgehog if found 
var distance = function(e) {
    jingles.play();
    mouseX = e.pageX;
    mouseY = e.pageY;
    var dist;
    dist = Math.sqrt(Math.pow((mouseX - hedgehogX),2) + Math.pow((mouseY - hedgehogY),2));
    if (mouseOnImg()) {
    	reveal();
    }
};*/

var sound = function(d) {
    var dist = d;
    if (dist < 50) {
	jingles.play();
    };
    else if (dist < 100) {
	jingles.play();
    };
    else if (dist < 150) {
	jingles.play();
    };
    else if (dist < 200) {
	jingles.play();
    };
    else if (dist < 250) {
	jingles.play();
    };
    else if (dist < 300) {
	jingles.play();
    };
    else if (dist < 350) {
	jingles.play();
    };
    else if (dist < 400) {
	jingles.play();
    };
    else if (dist < 450) {
	jingles.play();
    };	
}; 

var distance = function() {
    var dist;
    dist = Math.sqrt(Math.pow((mouseX - hedgehogX),2) + Math.pow((mouseY - hedgehogY),2));
    return dist;
};
 
var find = function(e) {
    mouseX = e.pageX;
    mouseY = e.pageY;
    var dist = distance();
    sound(dist);
    if (mouseOnImg()) {
    	reveal();
    };
};

window.addEventListener('mousemove',find); 
