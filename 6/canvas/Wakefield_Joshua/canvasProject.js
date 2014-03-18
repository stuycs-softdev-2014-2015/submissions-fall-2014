var canvass = document.getElementById("canvas1");
var ctx = canvass.getContext("2d");

var Hole = function(x,y,r) {
    return {
	x:x,
	y:y,
	r:r,
	draw: function(ctx) {
	    ctx.beginPath();
	    ctx.arc(this.x, this.y,r,0,2*Math.PI);
	    ctx.fillStyle='#000000';
	    ctx.stroke();
	    ctx.fill();
	},
	death: function(xx,yy) {
	    if ((Math.sqrt((xx - this.x)*(xx - this.x) + (yy - this.y)*(yy - this.y)) < r) && (b.dead == false)) {
		fin = true;
		b.x = this.x;
		b.y = this.y;
		b.dead = true;
		msg = "I fell in a hole yey... that was sarcasm btw.";
	    }
	},
	pullx: function(x,y,r) {
	    if ((this.x <= x) && (this.x + this.w >= x) && (this.y <= y) && (this.y + this.h >= y)) {
		cx = 0;
		cy = 0;
		c = 0;
		if (Math.abs((this.x - x)) < Math.abs((this.x + this.w - x)))
		    cx = this.x;
		else cx = this.x + this.w;
		if (Math.abs((this.y - y)) < Math.abs((this.y + this.h - y)))
		    cy = this.y;
		else cy = this.y + this.h;
		if (Math.abs((cx - x)) < Math.abs((cy - y))) {
		    return cx - x;
		}
	    }
	}
    }
}

var rectangularHole = function(x,y,w,h) {
    return {
	x:x,
	y:y,
	w:w,
	h:h,
	draw: function(ctx) {
	    ctx.fillStyle = '#FFFFFF';
	    ctx.fillRect(this.x, this.y, this.w, this.h);
	}
    }
}

var Ball = function(x,y,dx,dy,ddx,ddy,r) {
    return {
	x:x,
	y:y,
	dx:dx,
	dy:dy,
	ddx:ddx,
	ddy:ddy,
	r:r,
	dead:false,
	draw: function(ctx) {
	    ctx.beginPath();
	    ctx.arc(this.x, this.y,this.r,0,2*Math.PI);
	    ctx.fillStyle='#FF00FF';
	    ctx.stroke();
	    ctx.fill();
	},
	move: function(ax,ay) {
	    this.x = this.x + this.dx;
	    this.y = this.y + this.dy;
	    this.ddx = ax;
	    this.ddy = ay;
	    this.dx = this.dx + this.ddx;
	    this.dy = this.dy + this.ddy;
	}
    }
}

var End = function(x,y,r) {
    return {
	x:x,
	y:y,
	r:r,
	draw: function(ctx) {
	    ctx.beginPath();
	    ctx.arc(this.x, this.y,this.r,0,2*Math.PI);
	    ctx.fillStyle='#FF0000';
	    ctx.stroke();
	    ctx.fill();
	},
	victory: function(xx,yy,rr) {
	    if (Math.sqrt((xx - this.x)*(xx - this.x) + (yy - this.y)*(yy - this.y)) < r + rr)
		fin = true;
	}
    }
}

var State = function(ax,ay) {
    return {
	ax:ax,
	ay:ay,
	lessAx: function(amount) {
	    this.ax = this.ax - amount;
	},
	lessAy: function(amount) {
	    this.ay = this.ay - amount;
	},
	moreAx: function(amount) {
	    this.ax = this.ax + amount;
	},
	moreAy: function(amount) {
	    this.ay = this.ay + amount;
	},
	outOfBounds: function(xx,yy,rr) {
	    if (xx + b.dx < rr) {
		b.dx = b.dx*(-.4);
	    }
	    if (yy + b.dy < rr) {
		b.dy = b.dy*(-.4);
	    }
	    if (xx + b.dx > 1000 - rr) {
		b.dx = b.dx*(-.4);
	    }
	    if (yy + b.dy > 600 - rr) {
		b.dy = b.dy*(-.4);
	    }

	}
    }
}

var b = Ball(50,50,0,0,0,0,10);
var s = State(0,0);
var e = End(200,300,20);
var t = Date.now();
var msg = "Congratzies uve 1";
var fin = false;

var holes = [];

for(i = 0; i<= 800; i = i + 6) {
    holes.push(Hole(i,100,30));
}
for(i = 100; i<= 400; i = i + 6) {
    holes.push(Hole(800,i,30));
}
holes.push(Hole(980,300,40));
holes.push(Hole(980,50,40));
holes.push(Hole(900,550,60));
holes.push(Hole(650,550,40));
holes.push(Hole(650,350,30));
holes.push(Hole(650,270,20));

for(i = 500; i>= 100; i = i - 6) {
    holes.push(Hole(i,600-i,30));
}



var animloop = function() {
    e.victory(b.x,b.y,b.r);
    
    ctx.fillStyle="#defbb4";
    ctx.fillRect(0,0,1000,600);

    for (i=0; i<holes.length;i=i+1) {	
	holes[i].draw(ctx);
	holes[i].death(b.x,b.y);
    }
    
    ctx.fillText("Get to the red dot without falling to doom using the arrow keys. Careful, you can only control your acceleration and 1 press in the opposite direction reverses the acceleration.",10,10);
    b.draw(ctx);
    e.draw(ctx);
    b.move(s.ax,s.ay);
    s.outOfBounds(b.x,b.y,b.r);
    
    if (fin == true) 
	alert(msg);
    else window.requestAnimationFrame(animloop);
}

window.addEventListener('keydown', function(e) {
    if (Date.now()-t > 250) {
	if (e.keyCode == 37) {
	    if (b.ddx > 0) 
		s.lessAx(s.ax+.06);
	    else s.lessAx(.02);
	}
	if (e.keyCode == 38) {
	    if (b.ddy > 0) {
		s.lessAy(s.ay+.06);
		//alert('hey');
	    }
	    else s.lessAy(.02);
	}
	if (e.keyCode == 39) {
	    if (b.ddx < 0) {
		s.lessAx(s.ax-.06);
		//alert('yo123');
	    }
	    else s.moreAx(.02);
	}
	if (e.keyCode == 40) {
	    if (b.ddy < 0) 
		s.lessAy(s.ay-.06);
	    else s.moreAy(.02);
	}
    }
},true);


window.requestAnimationFrame(animloop);
