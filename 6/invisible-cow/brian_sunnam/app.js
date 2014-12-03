var mouseX;
var mouseY;

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
    console.log(dist);
    if(dist<100){
	//canvas.innerHTML = 'grab';
	canvas.style.cursor = 'pointer';
	console.log('YAY');
    }
    else{
	canvas.style.cursor = 'auto';
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
