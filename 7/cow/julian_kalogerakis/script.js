var mousex;
var mousey;
var h = window.innerHeight - (window.innerHeight*.9*Math.random());
var w = window.innerWidth - (window.innerWidth*Math.random());
var m;
var wildFerrell;


window.addEventListener('mousemove', function(e){
	mousex = e.pageX;
	mousey = e.pageY;
	moveMeter();
    });

function moveMeter(){
    var dist = Math.sqrt(Math.pow(mousex-wildFerrell.style.left,2) + Math.pow(mousey-wildFerrell.style.top,2));
    console.log("" + dist);
    var maxDist = Math.sqrt(Math.pow(window.innerHeight,2) + Math.pow(window.innerWidth,2));
    var percentage = dist/maxDist;
    m = document.getElementById("temperature");
    m.style.marginLeft = percentage*window.innerWidth + "px";
}

function reset(){
    wildFerrell = document.getElementById("Ferrell");
    wildFerrell.style.marginTop = h + "px";
    wildFerrell.style.marginLeft = w + "px";
}



window.onload = reset();


