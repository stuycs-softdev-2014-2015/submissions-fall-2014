var c = document.getElementById("c");
var ctx = c.getContext("2d");

var block = function(x,y,w,h,ctx) {
    return {
	x:x,
	y:y,
	w:w,
	h:h,
	ctx:ctx,
	color:"#000000",
	dx:Math.random()*10,
	dy:Math.random()*10,
	draw:function() {
	    ctx.fillStyle=this.color;
	    ctx.fillRect(this.x, this.y, this.w, this.h);
	    ctx.stroke();
	},
	move:function() {
	    this.x = this.x + this.dx;
	    this.y = this.y + this.dy;
	    if (this.x<0 || this.x>600-this.w) {
		this.dx=this.dx*-1;
	    }
	    if (this.y<0 || this.y>600-this.h) {
		this.dy=this.dy*-1;
	    }
	},
	bounceX:function() {
	    this.dx = this.dx * -1;
	},
	bounceY:function() {
	    this.dy = this.dy * -1;
	}
    };
}

var bloop = function() {
    ctx.fillStyle="#ffffff";
    ctx.fillRect(0,0,600,600);
    for (var i = 0; i < blocks.length; i++) {
	blocks[i].move();
	blocks[i].draw();
	for (var j = 0; j < blocks.length; j++) {
	    if (j != i) {
		if (Math.abs(blocks[i].x-blocks[j].x) < Math.min(blocks[i].w,blocks[j].w) &&
		    Math.abs(blocks[i].y-blocks[j].y) < Math.min(blocks[i].h,blocks[j].h)) {
		    if (blocks[i].x != blocks[j].x) {
			blocks[i].bounceX();
			blocks[j].bounceX();
		    }
		    if (blocks[i].y != blocks[j].y) {
			blocks[i].bounceY();
			blocks[j].bounceY();
		    }
		}
	    }
	}
    }
    window.requestAnimationFrame(bloop);
}

var blocks=[];
for (var i = 0; i < 5; i++) {
    blocks.push(block(Math.random()*600,Math.random()*600,5+Math.random()*30,5+Math.random()*30,ctx));
}

window.requestAnimationFrame(bloop);