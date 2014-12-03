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

var game = function(image){
    var c = document.getElementById("myCanvas");
    var ctx=c.getContext("2d");
    var img = document.getElementById("Harvard");
    ctx.drawImage(img,hx,hY);
};
    
    
