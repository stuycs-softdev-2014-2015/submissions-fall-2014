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
hedgehog.addEventListener('click', function(e) {
    hedgehog.style.visibility = "visible";
    console.log("FOUND IT");
});
var distance = function(e) {
    mouseX = e.pageX;
    mouseY = e.pageY;
    var dist;
    dist = Math.sqrt(Math.pow((mouseX - hedgehogX),2) + Math.pow((mouseY - hedgehogY),2));
    console.log(dist);
};
window.addEventListener('mousemove', distance); 



