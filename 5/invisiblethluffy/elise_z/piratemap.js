var mouseX, mouseY;
var dist;
var tX, tY; //the x,y cor of the TREASURE

window.addEventListener('mousemove',function(e) { 
    mouseX = e.pageX;
    mouseY = e.pageY;
});

//TREASURE image
var treasure = document.createElement('img');
treasure.setAttribute('src','treasure.png');
treasure.setAttribute('height','100px');
treasure.setAttribute('width','100px');
treasure.style.position = 'absolute';
treasure.style.visibility = 'visible';
tX =  Math.random()*window.innerWidth;
tY =  Math.random()*window.innerHeight;
treasure.style.left = tX + 'px';
treasure.style.top = tY + 'px';

//FOOTSTEPS image
var foot_right = document.createElement('img');
var foot_left = document.createElement('img');
//right foot
foot_right.setAttribute('src','foot-right.gif');
foot_right.setAttribute('height','100px');
foot_right.setAttribute('width','100px');
foot_right.style.position = 'absolute';
foot_right.style.visibility = 'visible';


//left foot
foot_left.setAttribute('src','foot-left.gif');
foot_left.setAttribute('height','100px');
foot_left.setAttribute('width','100px');
foot_left.style.position = 'absolute';
foot_left.style.visibility = 'visible';

document.getElementsByTagName('body')[0].appendChild(treasure);
document.getElementsByTagName('body')[0].appendChild(foot_right);
document.getElementsByTagName('body')[0].appendChild(foot_left);

var start = function() { 
    dist = Math.sqrt( Math.pow(mouseX-tX,2) + Math.pow(mouseY-tY,2));
    foot_right.style.left = mouseX-60 + 'px';
    foot_right.style.top = mouseY-60 + 'px';
    foot_left.style.left = mouseX-60 + 'px';
    foot_left.style.top = mouseY-60 + 'px';
    // make dist an int 
    var int_dist = Math.floor(dist);
    	   
    //feet grow when closer to the light
    if (int_dist > 650) {
	foot_right.setAttribute('height','75px');
	foot_right.setAttribute('width','75px');
	foot_left.setAttribute('height','75px');
	foot_left.setAttribute('width','75px');	
    }
    if (int_dist > 500 && int_dist < 650) {
	foot_right.setAttribute('height','100px');
	foot_right.setAttribute('width','100px');
	foot_left.setAttribute('height','100px');
	foot_left.setAttribute('width','100px');
    }
    if (int_dist > 350 && int_dist < 500) {
	foot_right.setAttribute('height','125px');
	foot_right.setAttribute('width','125px');
	foot_left.setAttribute('height','125px');
	foot_left.setAttribute('width','125px');	
    }
    if (int_dist < 350 && int_dist > 250) {
	foot_right.setAttribute('height','150px');	
	foot_right.setAttribute('width','150px');
	foot_left.setAttribute('height','150px');
	foot_left.setAttribute('width','150px');	
    }
    if (int_dist < 250 && int_dist > 150) {
	foot_right.setAttribute('height','175px');
	foot_right.setAttribute('width','175px');
	foot_left.setAttribute('height','175px');
	foot_left.setAttribute('width','175px');	
    }
    if (int_dist < 150 && int_dist > 50) {
	foot_right.setAttribute('height','200px');
	foot_right.setAttribute('width','200px');
	foot_left.setAttribute('height','200px');
	foot_left.setAttribute('width','200px');	
    }
    if (int_dist < 50) {
	foot_right.setAttribute('height','225px');
	foot_right.setAttribute('width','225px');
	foot_left.setAttribute('height','225px');
	foot_left.setAttribute('width','225px');
	treasure.style.visibility = 'visible';
    }
    if (tX < mouseX) { 
	foot_left.style.visibility = 'hidden';
	foot_right.style.visibility = 'visible';
    }
    else { 
	foot_left.style.visibility = 'visible';
	foot_right.style.visibility = 'hidden';
    }
}

window.addEventListener('mousedown',function() { 
    if (dist < 50) { 
	window.alert("You ARRR worthy!");
	window.alert("What did the pirate say when he turned 80?");
	window.alert("Ay, matey!");
	location.reload();
    }
});


event = setInterval(start,100);
