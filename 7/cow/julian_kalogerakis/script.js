var mousex, mousey;
var h = window.innerHeight - (window.innerHeight*.9*Math.random());
var w = window.innerWidth - (window.innerWidth*Math.random());
var m;
var dist = 0;
var maxDist = 0;
var percentage = 0;
var wildFerrell = 0;
var fX = 0;
var fY = 0;

window.addEventListener('mousemove', function(e){
	mousex = e.pageX;
	mousey = e.pageY;
	moveMeter();
    });

function moveMeter(){
    dist = Math.sqrt(Math.pow((mousex-fX),2) + Math.pow((mousey-fY),2));
    maxDist = Math.sqrt(Math.pow(window.innerHeight,2) + Math.pow(window.innerWidth,2));
    percentage = dist/maxDist;
    console.log("dist: " + dist);
    console.log("max dist: " + maxDist);
    console.log("percentage: " + percentage);
    m = document.getElementById("temperature");
    m.style.marginLeft = (1-percentage)*window.innerWidth + "px";
}

function reset(){
    wildFerrell = document.getElementById("Ferrell");
    wildFerrell.style.marginTop = h + "px";
    wildFerrell.style.marginLeft = w + "px";
    fX = wildFerrell.style.marginLeft;
    fY = wildFerrell.style.marginTop;
    fX = fX.substring(0, fX.length-2);
    fY = fY.substring(0, fY.length-2);
    fX = parseInt(fX) + 63;
    fY = parseInt(fY) + 175;

}

window.onload = reset();


