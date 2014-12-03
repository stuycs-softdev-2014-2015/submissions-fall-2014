var mouseX,mouseY;
var hX, hY;
window.addEventListener("mousemove",function(e){
		// console.log(e.pageX+" "+e.pageY);
		mouseX = e.pageX;
		mouseY = e.pageY;
});

var randomLocation = function(){
    hX = random(window.innerWidth-50)
    hY = random(window.innerHeight-50)
    
}; 

var moveImage = function(){
    var x = Math.floor(Math.random()* (window.innerWidth - 50)) + 50;
    var y = Math.floor(Math.random()* (window.innerHeight - 50)) + 50;

    var img = document.getElementById("Harvard");
    img.style.top = y + "px";
    img.style.left = x + "px";
};


var go = function(){
    moveImage
}

    
