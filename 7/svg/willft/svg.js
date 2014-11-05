var svg = document.getElementById("c")

var randcolor = function() {
    return '#'+Math.floor(Math.random()*16777215).toString(16)
}

var g = 9.8
//size of pixel in meters
var pixsize = .03

var balls = []

var ball = function(x, y, dx, dy) {
    var bounce = (Math.random() * .2) + .4
    var radius = (Math.random() * 10) + 10
    ret = {
	x:x, y:y, dx:dx, dy:dy,
	color:randcolor(),
	move:function(ts) {
	    this.x += this.dx * ts / pixsize
	    this.y += this.dy * ts / pixsize
	    this.dy += g * ts

	    if (this.y + radius >= svg.getAttribute("height")) {
		this.y = svg.getAttribute("height") - radius
		this.dy *= -bounce
	    }
	    if (this.x + radius >= svg.getAttribute("width")) {
		this.x = svg.getAttribute("width") - radius
		this.dx *= -bounce
	    }
	    if (this.x - radius <= 0) {
		this.x = radius
		this.dx *= -bounce
	    }
	},
	draw:function() {
            this.body.setAttribute('cx',this.x);
            this.body.setAttribute('cy',this.y);
	}
    }
    ret.body = document.createElementNS("http://www.w3.org/2000/svg","circle");
    ret.body.setAttribute('r',radius);
    ret.body.setAttribute('fill',ret.color);
    ret.body.setAttribute('stroke', 'black');
    ret.draw()
    svg.appendChild(ret.body);
    return ret
}
var tscale = document.getElementById('tscale')
//var dscale = document.getElementById('dscale')
var elapsed = new Date().getTime() / 1000
var update = function() {
    //ctx.clearRect(0, 0, canvas.width, canvas.height)
    var t = new Date().getTime() / 1000
    for(var i=0; i<balls.length; i++) {
	balls[i].move((t - elapsed) * tscale.value)
	balls[i].draw()
    }
    elapsed = t
}

var fire = function(e) {
    balls.push(ball(e.offsetX, e.offsetY, (Math.random() * 20) - 10, (Math.random() * -10) - 5))
}
svg.addEventListener('click', fire)

var shake = function(e) {
    //shake constant
    var sk = 100
    for (var i=0; i < balls.length; i++) {
	balls[i].dx = ((Math.random() * sk) - (sk/2)) * tscale.value
	balls[i].dy = ((Math.random() * sk) - (sk/2)) * tscale.value
    }
}
document.getElementById('shake').addEventListener('click', shake)

var addmulti = function(e) {
    for (var i=0; i < document.getElementById('addmultival').value; i++)
	fire({offsetX:svg.getAttribute('width')/2, offsetY:svg.getAttribute('height')/2});
}
document.getElementById("addmultisubmit").addEventListener('click', addmulti)

var t =0;
var go = function() {
    if (t==0){
        t = setInterval(update,30);
    } else {
        clearInterval(t);
        t=0;
    }
}
go();
