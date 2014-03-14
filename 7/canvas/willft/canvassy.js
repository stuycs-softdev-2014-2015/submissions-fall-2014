var canvas = document.getElementById("c")
var ctx = canvas.getContext("2d")

var randcolor = function() {
    return '#'+Math.floor(Math.random()*16777215).toString(16)
}

var g = 9.8
//size of pixel in meters
var pixsize = .03

var balls = []

var ball = function(x, y, dx, dy, ctx) {
    var bounce = .5
    var radius = 10
    return {
	x:x, y:y, dx:dx, dy:dy, ctx:ctx,
	color:randcolor(),
	move:function(ts) {
	    this.x += this.dx * ts / pixsize
	    this.y += this.dy * ts / pixsize
	    this.dy += g * ts

	    if (this.y + radius >= this.ctx.canvas.height) {
		this.y = this.ctx.canvas.height - radius
		this.dy *= -bounce
	    }
	    if (this.x + radius >= this.ctx.canvas.width) {
		this.x = this.ctx.canvas.width - radius
		this.dx *= -bounce
	    }
	    if (this.x - radius <= 0) {
		this.x = radius
		this.dx *= -bounce
	    }
	},
	draw:function() {
	    this.ctx.beginPath()
	    this.ctx.arc(this.x, this.y, radius, 0, 2 * Math.PI, false);
	    this.ctx.fillStyle = this.color
	    this.ctx.fill();
	    this.ctx.strokeStyle = '#000000'
	    this.ctx.stroke()
	}
    }
}
var tscale = document.getElementById('tscale')
//var dscale = document.getElementById('dscale')
var elapsed = new Date().getTime() / 1000
var update = function() {
    ctx.clearRect(0, 0, canvas.width, canvas.height)
    var t = new Date().getTime() / 1000
    for(var i=0; i<balls.length; i++) {
	balls[i].move((t - elapsed) * tscale.value)
	balls[i].draw()
    }
    elapsed = t
    window.requestAnimationFrame(update)
}

var fire = function(e) {
    balls.push(ball(e.offsetX, e.offsetY, (Math.random() * 20) - 10, (Math.random() * -10), ctx))
}
canvas.addEventListener('click', fire)

var shake = function(e) {
    //shake constant
    var sk = 100
    for (var i=0; i < balls.length; i++) {
	balls[i].dx = ((Math.random() * sk) - (sk/2)) * tscale.value
	balls[i].dy = ((Math.random() * sk) - (sk/2)) * tscale.value
    }
}
document.getElementById('shake').addEventListener('click', shake)

update()
