var mouseX, mouseY;
var thluffyX, thluffyY;
var thluffy = document.getElementById("thluffy");
var playing= true;

thluffyX=Math.random() * (window.innerWidth-500);
thluffyY=Math.random()* (window.innerHeight-220);
thluffy.style.cursor="pointer";

document.getElementById("thluffy").style.left=thluffyX+"px";
document.getElementById("thluffy").style.top=thluffyY+"px";

window.addEventListener('mousemove', function(e) {
    mouseX = e.pageX;
    mouseY = e.pageY;
});


var buildup =document.getElementById('javert_loud');
var found =document.getElementById('donotforget');
var play = function(e) {
    var mode=document.getElementById("mode");
    var distance =Math.sqrt(Math.pow(mouseX-(thluffyX+250),2)+Math.pow(mouseY-(thluffyY+110),2));

    if (mode.options[mode.selectedIndex].text == "Scare"){
	buildup =document.getElementById('footsteps');
	found =document.getElementById('door');
	document.body.style.color= "#ffffff";
	document.body.style.backgroundColor= "#000000";
	if (distance >500)
	    buildup.volume=.3;
	else if (distance >400)
	    buildup.volume=.5;
	else if (distance >300)
	    buildup.volume=.7;
	else if (distance >200)
	    buildup.volume=1;
	else
	    buildup.volume=0;
	buildup.play();
    }
    else{
	buildup =document.getElementById('javert_loud');
	found =document.getElementById('donotforget');
	document.body.style.backgroundColor= "#ffffff";
	document.body.style.color= "#000000";
	if (distance >500)
	    buildup.volume=.1;
	else if (distance >400)
	    buildup.volume=.3;
	else if (distance >300)
	    buildup.volume=.5;
	else if (distance >200)
	    buildup.volume=.7;
	else
	    buildup.volume=1;
	buildup.play();
    }
    
    //console.log(distance);
    if (playing){
	myevent = setTimeout(play,300);
    }
}

var done=function(){
    
    playing=false;

    found.volume=1;
    buildup.pause();
    found.play();

    thluffy.style.opacity=1;


    
}

thluffy.addEventListener('click',done);
var myevent;
myevent = setTimeout(play,200);
