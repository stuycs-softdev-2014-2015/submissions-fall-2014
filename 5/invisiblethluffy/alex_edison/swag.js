var mousex;
var mousey;
var swagX;
var swagY;
var swag = document.getElementById("swag");
swag.style.position="absolute";

window.addEventListener('mousemove',function(e){
    mousex=e.pageX;
    mousey=e.pageY;

});

swagX=Math.random()*(window.innerWidth-100);
swagY=Math.random()*(window.innerHeight-150);
swag.style.left=swagX+"px";
swag.style.top=(50+swagY)+"px";

var swagger=function(e){
    var distance=Math.sqrt(Math.pow(mousex-(swagX+50),2)+Math.pow(mousey-(swagY+50),2));
}


var complete=function(e){
    swag.style.visibility="visible";
}

swag.addEventListener("click",complete(e));
var swagevent;
swagevent=setTimeout(swagger,300);
