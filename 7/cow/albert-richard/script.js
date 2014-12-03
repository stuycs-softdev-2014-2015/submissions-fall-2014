var mouseX, mouseY;
var hiddenX, hiddenY;
var distance;
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
	getDistance();
});

var stopTimer = function(e){
	window.clearInterval(e);
}

var createHiddenLocation = function(e){
	hiddenX = 200;
	hiddenY = 200;
}

var getDistance = function(e){
	var xplace = hiddenX - mouseX;
	var yplace = hiddenY - mouseY;
	distance = Math.sqrt(Math.pow(xplace,2)+Math.pow(yplace,2));
	dist = document.getElementById("dist");
	dist.innerHTML = distance;
}