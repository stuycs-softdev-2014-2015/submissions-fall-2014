//apm stuff

var clicks = 0;
var minutes = 1; //test with 1
var calculateAPM = function() {
    if (minutes < 1) {
	c = clicks;
    }
    else {
	c = clicks/minutes;
    }
    item = document.getElementById("apm");
    item.innerHTML = ("APM: " + c);
}
var addMinute = function() {
    minutes += 1;
}
var minuteTimer = setInterval(addMinute, 60000);

//damage stuff
var barHP = 250;

function Zergling (x, y) {
    var self = this;
    self.item = document.createElement("img");
    self.image = "hand-pointer-icon.png";
    self.item.setAttribute("src",self.image);
    self.x = x;
    self.y = y;
    self.item.style.position = "absolute";
    self.item.style.left = parseInt(x) + "px";
    self.item.style.top = parseInt(y) + "px";
    self.speed = 5;
    self.HP = 3;
    self.isAlive = function() {
	return self.HP > 0;
    };
    self.hit = function() {
	clicks += 1;
	self.HP -= 1;
	console.log(self.HP);
	/*
	  if (!self.isAlive()) {
	    self.item.removeEventListener("click",self.hit);
	    document.body.removeChild(self.item);
	}
	*/
	//console.log(this.speed);
    };
    self.bound = 42; //the bound line
    self.move = function() { //only y axis
	if (self.y > self.bound) { 
	    self.item.style.top = parseInt(self.item.style.top) - self.speed + "px";
	    self.y -= self.speed;
	}
    };
    self.item.addEventListener("click",self.hit);

    self.attack = function() {
	if (self.y <= self.bound) {
	    barHP -= 1;
	}
    };
    self.damageTimer = setInterval(self.attack,333);

    document.body.appendChild(self.item);
}


var units = [];
var spawn1Timer;
var spawn4Timer;
var spawn6Timer;
var frameTimer;

var body = document.body;
var html = document.documentElement;

var height = Math.max( body.scrollHeight, body.offsetHeight, 
                       html.clientHeight, html.scrollHeight, html.offsetHeight );
var width = body.offsetWidth;
var stopTimer = function(e) {
    window.clearInterval(e);
};

var counter = 2;
var spawn1 = function() {
    var random = Math.random();
    units.push(new Zergling(random*width,height));
    stopTimer(spawn1Timer);
    spawn1Timer = setInterval(spawn1, 5000/Math.log(counter));
};
var spawn4 = function() {
    //console.log("test");
    var random = Math.random();
    units.push(new Zergling(random*width,height));
    units.push(new Zergling(random*width+28,height));
    units.push(new Zergling(random*width+28,height+36));
    units.push(new Zergling(random*width,height+36));
    stopTimer(spawn4Timer);
    spawn4Timer = setInterval(spawn4,10000);
};
var spawn6 = function() {
    var random = Math.random();
    units.push(new Zergling(random*width,height));
    units.push(new Zergling(random*width+28,height));
    units.push(new Zergling(random*width+28*2,height));
    units.push(new Zergling(random*width,height+36));
    units.push(new Zergling(random*width+28,height+36));
    units.push(new Zergling(random*width+28*2,height+36));
    stopTimer(spawn6Timer);
    spawn6Timer = setInterval(spawn6,20000);
};
var frame = function() {
    if (barHP <=0) {
	heading = document.getElementById("heading");
	heading.innerHTML = "You failed!";
	stopTimer(spawn1Timer);
	stopTimer(spawn4Timer);
	stopTimer(spawn6Timer);
	//stopTimer(frameTimer);
	for (var i=0; i<units.length;i++) {
	    units[i].bound = 0;
	    units[i].move();
	}
    }
    else {
	for (var i=0; i<units.length; i++) {
	    if (!units[i].isAlive()) {
		units[i].item.removeEventListener("click",units[i].hit);
		document.body.removeChild(units[i].item);
		units.splice(i, 1);
	    }
	    else {
		units[i].move();
	    }
	}
	heading = document.getElementById("heading");
	heading.innerHTML = "Defend Your Address Bar! HP: "+barHP;
	calculateAPM();
	counter += 1;
    }
};
spawn1Timer = setInterval(spawn1,5000);
spawn4Timer = setTimeout(spawn4, 20000);
spawn6Timer = setTimeout(spawn6, 60000);
frameTimer = setInterval(frame,100);
