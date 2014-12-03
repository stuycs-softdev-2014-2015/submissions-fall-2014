var mouseX, mouseY, hedgehogX, hedgehogY;
var hedgehog = document.getElementById("hedgehog");
hedgehog.addEventListener('click', reveal);
hedgehogX = Math.floor((Math.random() * window.innerWidth));
hedgehogY = Math.floor((Math.random() * window.innerHeight));
hedgehog.top = hedgehogY.toString() + "px;";
hedgehog.left = hedgehogX.toString() + "px;";
window.addEventListener('mousemove', function(e) {
    mouseX = e.pageX;
    mouseY = e.pageY;
});


var setHedgehogCoordinates = function(e) {
    
}
var distance = function(e) {
    var dist;
    dist = Math.sqrt(Math.pow((mouseX - hedgehogX),2) + Math.pow((mouseY - hedgehogY),2));
};
