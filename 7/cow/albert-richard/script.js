var mouseX, mouseY;
var printLocation = function(){
    console.log(""+mouseX+","+mouseY);
};
var myEvent;
//myEvent = setInterval(printLocation,100);


window.addEventListener('mousemove',function(e){
	mouseX = e.pageX;
	mouseY = e.pageY;
	coor = document.getElementById("coor");
	coor.innerHTML = ""+mouseX+","+mouseY;
});

var stopTimer = function(e){
	window.clearInterval(e);
}
