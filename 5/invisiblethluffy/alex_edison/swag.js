var mousex;
var mousey;
var swagX;
var swagY;
var swag = document.getElementById("swag");

window.addEventListener('mousemove',function(e){
    mousex=e.pageX;
    mousey=e.pageY;

});

swagX=Math.random() * (window.innerWidth-400);
swagY=Math.random() * (window.innerHeight-430);

document.getElementById("swag").style.left=swagX+"px";
document.getElementById("swag").style.top=swagY+"px";

var swagger=function(e){
    var distance=Math.sqrt(Math.pow(mousex-(swagX+200),2)+Math.pow(mousey-(swag+215),2));
}


var complete=function(){
    swag.style.opacity=1;
}

swag.addEventListener('click',complete);
var swagevent;
swagevent=setTimeout(swagger,300);
