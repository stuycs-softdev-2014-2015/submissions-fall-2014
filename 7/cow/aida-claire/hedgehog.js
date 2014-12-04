var mouseX, mouseY, hedgehogX, hedgehogY;
var hedgehog = document.getElementById("hedgehog");

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
var mouseOnImg = function() {
	if (mouseX > hedgehogX && mouseX < 150 + hedgehogX) {
		if (mouseY > hedgehogY && mouseY < 100 + hedgehogY) {
			return true;
		}
	}
	return false;
}
var distance = function(e) {
    mouseX = e.pageX;
    mouseY = e.pageY;
    var dist;
    dist = Math.sqrt(Math.pow((mouseX - hedgehogX),2) + Math.pow((mouseY - hedgehogY),2));
    if (mouseOnImg()) {
    	reveal();
    }
};
window.addEventListener('mousemove', distance); 
