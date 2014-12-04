

var s1 = document.getElementById("1");
var s2 = document.getElementById("2");
var s3 = document.getElementById("3");
var s4 = document.getElementById("4");
var s5 = document.getElementById("5");
var s6 = document.getElementById("6");
var ow = document.getElementById("ow");
var mouseX;
var mouseY;
window.addEventListener('click',function(e){
    mouseX=e.pageX;
    mouseY=e.pageY;
    sacked();
}); 
function sacked(){
    var x = mouseX;
    var y = mouseY;
    var qb = document.getElementById("QB");
    if (x >= parseInt(qb.style.left)
	&& x <= parseInt(qb.width) + parseInt(qb.style.left)
	&& y >= parseInt(qb.style.top)
	&& y <= parseInt(qb.height) + parseInt(qb.style.top)){
	    console.log(x);
	qb.style.visibility="visible";
	s1.pause();
	ow.play();
	window.alert("REKT THE " + qb.id);
	s1.play();
	qb.style.visibility="hidden";
	var w = Math.random() * window.innerWidth;
	var h = Math.random() * window.innerHeight;
	while (w > window.innerWidth - parseInt(e.width)) {
	    w = Math.random() * window.innerWidth;
	}
	while (h > window.innerHeight - parseInt(e.height)) {
	    h = Math.random() * window.innerHeight;
	}
	qb.style.left = "" + w + "px";
	qb.style.top = "" + h + "px";
    }
    else {
	console.log(x);
	console.log(parseInt(qb.style.left));
	console.log((x >= parseInt(qb.left)
		    /* && x <= parseInt(qb.width) + parseInt(qb.left)
		     && y >= parseInt(qb.top)
		     && y <= parseInt(qb.height) + parseInt(qb.top)*/));
    }
};

