console.log("???");
var toInt = function(e){
    return parseInt(e.substring(0,e.length-2));
}
var random_num = function(x){
    return parseInt(Math.random()*x);
}
var toRad = function(value) {
    /** Converts numeric degrees to radians */
    return (value * Math.PI) / 180;
}
var abs_value_from = function(value1,value2){
    /** Finds the difference between the 2 values **/
    /** used in heading changing **/
    return Math.abs(value1-value2);
}

var hide = function(){
    console.log("hidden");
    cow.src="invisible.png";
    valid=true;
    cow.height=128;
    cow.width=128;
    growing = false;
}

var tracker = 0;
var growing = false;

var growhelp = function() {
    //console.log(cow.height);
    if (growing == true) {
	if (tracker<75) {
	    console.log("growing");
	    cow.height=cow.height+1;
	    cow.width=cow.width+1;
	    if (tracker%2 == 0) {
		var newX = cow.style.left;
		newX =  parseInt(newX.substring(0,newX.length-2))-1;
		var newY = cow.style.top;
		NewY = parseInt(newY.substring(0,newY.length-2))-1;
		cow.style.left=newX+"px";
		cow.style.top=newY+"px";
	    }
	}
	else if (tracker>150) {
	    growing = false;
	}
	else {
	    console.log("shrinking");
	    cow.height=cow.height-1;
	    cow.width=cow.width-1;
	    if (tracker%2 == 0) {
		var newX = cow.style.left;
		newX =  parseInt(newX.substring(0,newX.length-2))+1;
		var newY = cow.style.top;
		NewY = parseInt(newY.substring(0,newY.length-2))+1;
		cow.style.left=newX+"px";
		cow.style.top=newY+"px";
	    }
	}
	tracker++;
    }
}

var grow = function(){
    growing = true;
    console.log("growing");
    tracker = 0;
    setInterval(function(){growhelp()}, 10);   
}

var valid = true;
var width = document.documentElement.clientWidth;
var height = document.documentElement.clientHeight; 

var cow=document.getElementById("cow");
cow.style.cursor="pointer";
cow.speed=0;
cow.heading=0;
cow.style.position="absolute";
cow.style.left="200px";
cow.style.top="200px";
hide();

var changeLoc = function(x,y){
    cow.style.left=x;
    cow.style.top=y;
}
setInterval(timer,50);

function timer(e){
    var x = cow.style.left;
    x =  parseInt(x.substring(0,x.length-2));
    x = Math.floor(x + cow.speed*Math.cos(toRad(cow.heading)));
    var y = cow.style.top;
    y = parseInt(y.substring(0,y.length-2));
    y = Math.floor(y - cow.speed*Math.sin(toRad(cow.heading)));
    //console.log(Math.sin(toRad(cow.heading)));
    //console.log(Math.cos(toRad(cow.heading)));
    //console.log("heading"+cow.heading);
    if(x<0 && abs_value_from(180,cow.heading) < 90){
	cow.heading=(180-cow.heading)%360;
    }else if (x>width-200 &&abs_value_from(0,cow.heading) <90){
	cow.heading=(180-cow.heading)%360;
    }else if (y<0 && abs_value_from(90,cow.heading) < 90){
	cow.heading=(360-cow.heading)%360;
    }else if(y>height-200 && abs_value_from(270,cow.heading)<90){
	cow.heading=(360-cow.heading)%360;
    }
    changeLoc(x+"px",y+"px")
    //console.log("cow is at:"+x+","+y);
    cow.heading=(cow.heading+random_num(10)-5)%360;
    while(cow.heading<0){//mod doesnt deal with negatives?
	cow.heading+=360;
    }
    //console.log(cow.heading);
    //console.log(width);	
}
var updateMusic = function(e){
    mouseX = e.pageX;
    mouseY = e.pageY;	
    var x = cow.style.left.substring(0,cow.style.left.length-2);
    var y = cow.style.top.substring(0,cow.style.top.length-2);
    x = parseInt(x)+64;
    y = parseInt(y)+64;
    var deltaX = (x-mouseX)/(width-64);
    var deltaY = (y-mouseY)/(height-64);	
    var dist = Math.sqrt((deltaX*deltaX)+(deltaY*deltaY));
    var newVol = 1-dist;
    //console.log(newVol);
    music.volume = newVol;
}

var button=document.getElementById("b");
var start=function(){
    console.log("started your stupid game");
    cow.speed = 0;
    music = new Audio("cantina.mp3");
    music.addEventListener("ended",function () {
	this.currentTime = 0;
	this.play();
    }, false);
    music.play();
    window.addEventListener("mousemove",updateMusic);
    cow.addEventListener('click',
		     function(e){
			 if (valid) {
			     console.log("swigity swag clicked circle");
			     document.getElementById("trap").play();
			     cow.speed+=1;
			     console.log(cow.speed);
			     cow.src="admiral.png";
			     valid = false;
			     grow();
			     setTimeout(function(){hide()}, 1500);
			 }
		     });
}
button.addEventListener('click',start);
