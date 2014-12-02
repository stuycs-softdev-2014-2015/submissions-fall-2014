var mouseX, mouseY;
var thluffyX, thluffyY;
thluffyX=Math.random() * (window.innerWidth-500);
thluffyY=Math.random()* (window.innerHeight-220);
var thluffy = document.getElementById("thluffy");
console.log(thluffyX)
document.getElementById("thluffy").style.left=thluffyX+"px";
document.getElementById("thluffy").style.top=thluffyY+"px";
var doStuff = function(e) {
		
		var distance =Math.sqrt(Math.pow(mouseX-(thluffyX+250),2)+Math.pow(mouseY-(thluffyY+110),2));
		if (distance <200){
			document.getElementById('javert_loud').play();
			document.getElementById("thluffy").style.visibility="visible";
		}
		document.getElementById("header").innerHTML= distance;
	
		myevent = setTimeout(doStuff,100);
		
}

window.addEventListener('mousemove', function(e) {
		mouseX = e.pageX;
		mouseY = e.pageY;
});

var myevent;
myevent = setTimeout(doStuff,100);