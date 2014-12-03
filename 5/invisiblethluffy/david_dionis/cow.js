var mouseX, mouseY;
var x,y;
var thluffy = document.getElementById("cow");
function placethluffy(){
    i = Math.floor(Math.random()*10)+1;
    thluffy.src = "static/Cow1.gif";
    x = Math.floor(Math.random()*window.innerWidth);
    y = Math.floor(Math.random()*window.innerHeight);
    thluffy.style.left = x;
    thluffy.style.find.top = y;
    thluffy.style.find.visibility = "visible";
    thluffy.addEventListener('mouseclick',show);
};
var show= function(e){
    thluffy.style.left = (window.innerWidth/2);
    thluffy.style.top = (window.innerHeight/2);
    thluffy.style.visibility = "visible";
};
var loc = function(e){
    var text;
    if((mouseX-x+mouseY-y)<100){
	text = "Getting really Close!";
    }else if ((mouseX-x+mouseY-y)<500){
	text = "Close";
    }
    var place = document.getElementById("h1");
    place.innerHTML=text;
    myevent=setTimeout(loc,100)
};
window.addEventListener('mousemove', function(e) {
    mouseX = e.pageX;
    mouseY = e.pageY;
});
var myevent = setTimeout(loc, 100);
placethluffy();
