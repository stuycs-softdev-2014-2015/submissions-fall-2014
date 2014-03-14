var main = function(){
    var cvs = document.getElementById('cvs');
    var ctx = cvs.getContext('2d');
    var ball = function(x,y,ctx){
	return {
	    x:x,
	    y:y,
	    color:'#FF0000',
	    radius:Math.random() * 45 + 5,
	    ctx:ctx,
	    dx:Math.random() * 10 + 1,
	    dy:Math.random() * -30 + 1,
	    draw:function(){
		//draw ball
		ctx.beginPath();
		ctx.strokeStyle=this.color;
		ctx.arc(this.x,this.y,this.radius,0,2*Math.PI);
		ctx.fillStyle=this.color;
		ctx.stroke();
		ctx.fill();
		//draw velocity of ball
		ctx.beginPath();
		ctx.strokeStyle='#000000';
		ctx.moveTo(this.x,this.y);
		ctx.lineTo(this.x + this.dx * 10,this.y + this.dy * 10);
		ctx.stroke();
	    },
	    gravity:function(){
		this.dy += .981;
	    },
	    move:function(){		
		this.gravity();
		this.x = this.x + this.dx;
		this.y = this.y + this.dy
		if(this.x > cvs.width-this.radius){
		    this.dx=this.dx*-.99;
		    this.x = cvs.width-this.radius;
		}
		else if (this.x < this.radius){
		    this.dx = this.dx*-.99;
		    this.x = this.radius;
		}
		if(this.y > cvs.height-this.radius){
		    this.dy=this.dy*-.975;
		    this.y = cvs.height-this.radius;
		    this.dx = this.dx*.99;
		}
	    }
	}
    };
    var paused = false;
    var animloop = function(){
	//console.log(paused);
	ctx.fillStyle="#FFFFFF";
	ctx.fillRect(0,0,cvs.width,cvs.height);
	b.draw();	
	if(!paused){
	    b.move();
	}else{
	    ctx.font="30pt Arial";
	    ctx.fillStyle="#000000";
	    ctx.fillText("Bouncy Ball Paused!",75,cvs.height/2 + 15);
	}
	window.requestAnimationFrame(animloop);
    }
    
    var b = ball(100,300,ctx);
    b.draw();
    cvs.addEventListener("click",function(e){paused = !paused;});
    window.requestAnimationFrame(animloop);
    
}();
