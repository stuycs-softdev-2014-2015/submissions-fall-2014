var mouseX;
var mouseY;

var music = document.getElementById('music');
console.log('music',music);
var canvas = document.getElementById('canvas');
var canvasrect = canvas.getBoundingClientRect();
var minX = canvasrect.left;
var maxX = canvasrect.right;
var minY = canvasrect.top;
var maxY = canvasrect.bottom;

var goalX;
var goalY;

window.addEventListener('mousemove',function(e){
    mouseX=e.pageX;
    mouseY=e.pageY;
    //console.log("mouse moved to ("+mouseX+','+mouseY+')')
});

var check = function(){
    //calculate distance
    var dx = mouseX-goalX;
    var dy = mouseY-goalY;
    var dist = Math.sqrt(dx*dx+dy*dy);
    dist = Math.floor(dist);
    var range = Math.sqrt(((maxX-minX)/2)*((maxX-minX)/2)+((maxY-minY)/2)*((maxY-minY)/2))/6;
    console.log(dist);
    if(dist<10){
	//canvas.innerHTML = 'grab';
	canvas.style.cursor = 'pointer';
	console.log('YAY');
    }
    else{
	canvas.style.cursor = 'auto';
    }
    if(dist < range){
	music.src = "Topher6.m4a";
	music.play();
    }
    else if (dist < (range*2)){
	music.pause();
	music.src = "Topher5.m4a";
	music.play();
    }
}

var game;
function start(){
    goalX = Math.random()*(maxX-minX)+minX;
    goalY = Math.random()*(maxY-minY)+minY;
    console.log(goalX+','+goalY);
    game = setInterval(check,100);
}
function stop(){
    window.clearTimeout(game);
}

document.getElementById('start').addEventListener('click',start);
document.getElementById('stop').addEventListener('click',stop);
