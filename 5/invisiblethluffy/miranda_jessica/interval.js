var mouseX, mouseY;
var thluffyX, thluffyY, phoneX, phoneY;
var mode=document.getElementById("mode");
var thluffy = document.getElementById("thluffy");
var phone = document.getElementById("phone");


var playing= true;
var change= true;


thluffyX=Math.random() * (window.innerWidth-500);
thluffyY=Math.random()* (window.innerHeight-220);
PhoneX=Math.random() * (window.innerWidth-110);
PhoneY=Math.random() * (window.innerWidth-110);

thluffy.style.cursor="pointer";

document.getElementById("thluffy").style.left=thluffyX+"px";
document.getElementById("thluffy").style.top=thluffyY+"px";
document.getElementById("phone").style.left=phoneX+"px";
document.getElementById("phone").style.top=phoneY+"px";

window.addEventListener('mousemove', function(e) {
    mouseX = e.pageX;
    mouseY = e.pageY;
});

var buildup =document.getElementById('javert_loud');
var found =document.getElementById('donotforget');
var play = function(e) {
    
    var distance=Math.sqrt(Math.pow(mouseX-(thluffyX+250),2)+Math.pow(mouseY-(thluffyY+110),2));
    var distanceP=Math.sqrt(Math.pow(mouseX-(phoneX+110),2)+Math.pow(mouseY-(phoneY+110),2));
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

    if (mode.options[mode.selectedIndex].text == "Scare"){
	phone.style.opacity=1;
	//thluffy.style.opacity=1;

	document.getElementById('ring').play();
	document.getElementById('Busy').play();
    }else {
	thluffy.style.opacity=1;
    }

    
}

thluffy.addEventListener('click',done);
//phone.addEventListener('click',done);

var myevent;
myevent = setTimeout(play,200);
