var panel = document.getElementById("panel")

var addCircle = function(x,y,r,c){
    var c1 = document.createElementNS("http://www.w3.org/2000/svg","circle");
    c1.setAttribute('id','c1');
    c1.setAttribute('cx',x);
    c1.setAttribute('cy',y);
    c1.setAttribute('r',r);
    c1.setAttribute('fill',c);
    return c1
}

var createCircle = function(x,y,r,c){
    var c1 = document.createElementNS("http://www.w3.org/2000/svg","circle");
    c1.setAttribute('id','c1');
    c1.setAttribute('cx',x);
    c1.setAttribute('cy',y);
    c1.setAttribute('r',r);
    c1.setAttribute('fill',c);
    panel.appendChild(c1);
    return {
	x:x,
	y:y,
	r:r,
	isIn: function(x,y) {
	    if (Math.sqrt((this.x - x) * (this.x - x) + (this.y - y) * (this.y - y)) < this.r) {
		return true;
	    }
	    else {
		return false;
	    }
	}
    }
}

var addTable = function(x,y,w,h,c,rx,ry){
    var t1 = document.createElementNS("http://www.w3.org/2000/svg","rect");
    t1.setAttribute('id','t1');
    t1.setAttribute('x',x);
    t1.setAttribute('y',y);
    t1.setAttribute('width',w);
    t1.setAttribute('height',h);
    t1.setAttribute('fill',c);
    t1.setAttribute('rx',rx);
    t1.setAttribute('ry',ry);
    panel.appendChild(t1);
}

var addStick = function(x1,y1,x2,y2,w,c,v){
    var s1 = document.createElementNS("http://www.w3.org/2000/svg","line");
    s1.setAttribute('id','s1');
    s1.setAttribute('x1',x1);
    s1.setAttribute('y1',y1);
    s1.setAttribute('x2',x2);
    s1.setAttribute('y2',y2);
    s1.setAttribute('stroke-width',w);
    s1.setAttribute('stroke',c);
    s1.setAttribute('stroke',c);
    return s1;
}

var Stick = function(x1,y1,x2,y2,w,color,v,l) {
    var s1 = addStick(x1,y1,x2,y2,w,color);
    panel.appendChild(s1);
    return {
	x1:x1,
	y1:y1,
	x2:x2,
	y2:y2,
	color:color,
	s1:s1,
	v:v,
	l:l,
	moveTo: function(x1,y1,theta) {
	    this.x1 = x1;
	    this.y1 = y1;
	    this.x2 = Math.cos(theta) * this.l + this.x1;
	    this.y2 = Math.sin(theta) * this.l + this.y1; 
	    this.s1.setAttribute('x1',this.x1);
	    this.s1.setAttribute('y1',this.y1);
	    this.s1.setAttribute('x2',this.x2);
	    this.s1.setAttribute('y2',this.y2);
	    this.s1.setAttribute('visibility',"visible");
	},
	hide: function() {
	    this.s1.setAttribute('visibility',"hidden");
	}
    }
}

var Ball = function(x,y,dx,dy,ddx,ddy,r,color) {
    var c1 = addCircle(x,y,r,color);
    panel.appendChild(c1);
    return {
	x:x,
	y:y,
	dx:dx,
	dy:dy,
	ddx:ddx,
	ddy:ddy,
	r:r,
	color:color,
	dead:false,
	c1:c1,
	move: function() {
	    if ((this.dx * this.ddx) > 0) {
		this.ddx = this.ddx * -1;
	    }
	    if ((this.dy * this.ddy) > 0) {
		this.ddy = this.ddy * -1;
	    }
	    if ((this.x + this.dx) < 15) {
		this.dx = this.dx * -.9;
	    }
	    if ((this.x + this.dx) > 615) {
		this.dx = this.dx * -.9;
	    }
	    if ((this.y + this.dy) < 15) {
		this.dy = this.dy * -.9;
	    }
	    if ((this.y + this.dy) > 315) {
		this.dy = this.dy * -.9;
	    }
	    
	    this.x = this.x + this.dx;
	    this.y = this.y + this.dy;
	    this.c1.setAttribute('cx',this.x);
	    this.c1.setAttribute('cy',this.y);
	    if (Math.abs(this.dx) > Math.abs(this.ddx)) {
		this.dx = this.dx + this.ddx;
	    }
	    else {
		this.dx = 0;
	    }
	    if (Math.abs(this.dy) > Math.abs(this.ddy)) {
		this.dy = this.dy + this.ddy;
	    }
	    else {
		this.dy = 0;
	    }
	},
	isIn: function(x,y) {
	    if (Math.sqrt((this.x - x) * (this.x - x) + (this.y - y) * (this.y - y)) < this.r) {
		return true;
	    }
	    else {
		return false;
	    }
	}
    }
}

addTable(5,5,620,320,"#A0522D",20,20);
addTable(15,15,600,300,"#387C44",0,0);
var h1 = createCircle(20,20,15,"black");
var h2 = createCircle(315,20,15,"black");
var h3 = createCircle(610,20,15,"black");
var h4 = createCircle(20,310,15,"black");
var h5 = createCircle(315,310,15,"black");
var h6 = createCircle(610,310,15,"black");
var holes = [];
holes.push(h1);
holes.push(h2);
holes.push(h3);
holes.push(h4);
holes.push(h5);
holes.push(h6);


var b = Ball(100,100,-1,-1,.03,.03,10,'white');
var s = Stick(0,0,1,1,5,"#FF33CC","hidden",150);
var t = Date.now();
var t2 = Date.now();
var mdx = 0;
var mpx = 0;
var mdy = 0;
var mpy = 0;
var md = false;

var animloop = function() {
    if (!b.dead) {
	b.move();

	for (i=0;i<6;i=i+1) {
	    if (holes[i].isIn(b.x,b.y)) {
		b.dead = true;
		b.x = holes[i].x;
		b.y = holes[i].y;
		b.dx = 0;
		b.dy = 0;
		b.move();
		break;
	    }
	}
    }

    
    window.requestAnimationFrame(animloop);
}

panel.addEventListener('mousedown', function(e) {
    if ((b.dx == 0) && (b.dy == 0)) {
	var mx = e.offsetX;
	var my = e.offsetY;
	t2 = Date.now();
	mpx = mx;
	mpy = my;
	var theta = Math.atan2(my - b.y, mx - b.x);
	if (!b.isIn(mx,my)) {
	    s.moveTo(mx,my,theta);
	    md = true;
	}
    }
},true);

panel.addEventListener('mousemove', function(e) {
    if ((b.dx == 0) && (b.dy == 0) && (md==true)) {
	var mx = e.offsetX;
	var my = e.offsetY;
	if ((Date.now() - t2) > 100) {
	    mdx = mpx - mx;
	    mdy = mpy - my;
	    mpx = mx;
	    mpy = my;
	}
	var theta = Math.atan2(my - b.y, mx - b.x);
	if (b.isIn(mx,my)) {
	    md = false;
	    s.hide();
	    b.dx = -mdx;
	    b.dy = -mdy;
	}
	else {
	    s.moveTo(mx,my,theta);
	}
    }
},true);

panel.addEventListener('mouseup', function(e) {
    md = false;
    s.hide();
},true);

window.requestAnimationFrame(animloop);