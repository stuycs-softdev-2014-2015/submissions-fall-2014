var c = document.getElementById("c");
var ctx = c.getContext("2d");

var block = function(x,y,w,h,ctx) {
    return {
        x:x,
        y:y,
        w:w,
        h:h,
        dx:1,
        dy:y,
        color:'#ff0000',
        ctx:ctx,
        draw: function() {
            ctx.fillStyle=this.color;
	    ctx.fillRect(this.x,this.y,this.w,this.h);
	    ctx.strokeRect(this.x,this.y,this.w,this.h);
	    ctx.stroke();
	},
	move: function() {
	    this.x = this.x + this.dx;
	    this.y = this.y + Math.random()*2-1;
	    if (this.x>550 || this.x<10){
		this.dx=this.dx*-1;
	    }
	}
    }
}

var animloop = function() {
    b1.move();
    b2.move();
    window.requestAnimationFrame(animloop);
}    
    /*var clickLoc = function(e) {
      var mouseX, mouseY;
      if(e.offsetX){
      mouseX = e.offsetX;
      mouseY = e.offsetY;
      }
      else if(e.layerX){
      mouseX = e.layerX;
      mouseY = e.layerY;
      }
      }
    */
    
    var b1 = block(0,0,200,200,ctx);
    var b2 = block(200,0,200,200,ctx); 
    var b3 = block(400,0,200,200,ctx);
    var b4 = block(0,200,200,200,ctx);
    var b5 = block(200,200,200,200,ctx);
    var b6 = block(400,200,200,200,ctx);
    var b7 = block(0,400,200,200,ctx);
    var b8 = block(200,400,200,200,ctx);
    var b9 = block(400,400,200,200,ctx);
    b9.color="#000000";
    b1.draw();    
    b2.draw();
    b3.draw();
    b4.draw();
    b5.draw();
    b6.draw();
    b7.draw();
    b8.draw();
    b9.draw();
    
    //window.requestAnimationFrame(animloop);
