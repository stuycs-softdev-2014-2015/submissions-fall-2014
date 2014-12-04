
var s1 = document.getElementById("1");
var s2 = document.getElementById("2");
var s3 = document.getElementById("3");
var s4 = document.getElementById("4");
var s5 = document.getElementById("5");
var s6 = document.getElementById("6");
var ow = document.getElementById("ow");
var current = s1;
s1.play();
var mouseX;
var mouseY;
window.addEventListener('click',function(e){
    mouseX=e.pageX;
    mouseY=e.pageY;
    sacked();
}); 
window.addEventListener("mousemove", function(e) {
    mouseX = e.pageX;
    mouseY= e.pageY;
    hut()});
var qb = document.getElementById("QB");

function dist(x1, y1, x2, y2) {
    return Math.sqrt(Math.pow(Math.abs(x1-x2),2)+Math.pow(Math.abs(y1-y2),2));
};
function hut() {
    var cx = parseInt(qb.style.left) + parseInt(qb.width)/2;
    var cy = parseInt(qb.style.top) + parseInt(qb.height)/2;
    var d = dist(cx, cy, mouseX, mouseY);
    var r = 100;
    console.log(current == s6);
    if (current == ow){
	return;
    }
    if (d < r) {
	if (current != s6) {
	    current.pause();
	    s6.play();
	    current = s6;
	}
    }
    else if (d < 2*r){
	if (current != s5) {
	    current.pause();
	    s5.play();
	    current = s5;
	}
    }
    else if (d < 3*r){
	if( current != s4) {
	    current.pause();
	    s4.play();
	    current = s4;
	}
    }
    else if (d < 4*r ) {
	if (current != s3) {
	    current.pause();
	    s3.play();
	    current = s3;
	}
    }
    else if (d < 5*r ){
	if( current != s2) {
	    current.pause();
	    s2.play();
	    current = s2;
	}
    }
    else {
	if (current != s1) {
	    current.pause();
	    s1.play();
	    current = s1;
	}
    }

};
function sacked(){
    var x = mouseX;
    var y = mouseY;
    if (x >= parseInt(qb.style.left)
	&& x <= parseInt(qb.width) + parseInt(qb.style.left)
	&& y >= parseInt(qb.style.top)
	&& y <= parseInt(qb.height) + parseInt(qb.style.top)){
	    console.log(x);
	qb.style.visibility="visible";
	current.pause();
	current = ow;
	ow.play();
	window.alert("U REKT THE " + qb.id);
	clearInterval(p);
	p = setInterval(failed,10000);
	reset();
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

function reset(){
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
    current.pause();
    current = s1;
    s1.play();
};
var p = setInterval(failed, 10000);
function failed() {
    current.pause();
    window.alert("You failed to sack the quarterback. He just threw the game winning touchdown.");
    reset();

};

