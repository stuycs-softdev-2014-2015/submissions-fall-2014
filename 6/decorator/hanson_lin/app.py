<!DOCTYPE html>

<html>
before
<div>
<canvas height="600" width="600" id="c"
	style="border:1px solid black">
</canvas>
</div>
after

<script>
 var c = document.getElementById("c");
 var ctx = c.getContext("2d");
 
 var block = function(x,y,w,h,ctx) {
   return {
     x:x,
     y:y,
     w:w,
     h:h,
     ctx:ctx,
     color:"#ff0000",
     dx:1,
     draw:function() {
       ctx.fillStyle=this.color;
       ctx.fillRect(this.x,this.y,this.w,this.h);
       ctx.stroke();
     },
     move:function() {
       this.x = this.x + this.dx;
       this.y = this.y + 2*Math.random() - 1;
       if (this.x<10||this.x>560) {
	 this.dx=this.dx*-1;
       }
       if (this.y<20 || this.y>580) {
	 this.y = 100+400*Math.random();
       }
     }
   };
 }

 var clicked = function(e) {
   var x = e.offsetX;
   var y = e.offsetY;
   var w = 10+Math.random()*40;
   var h = 5+Math.random()*40;

   b = block(x,y,h,w,ctx);
   blocks.push(b);

 }

var animloop = function(){
   ctx.fillStyle="#ffffff";
   ctx.fillRect(0,0,600,600);
   for (var i=0;i<blocks.length;i++) {
     blocks[i].move();
     blocks[i].draw();
   }
   window.requestAnimationFrame(animloop);
 } 

 var blocks=[];
 var b1 = block(50,100,30,15,ctx);
 var b2 = block(100,200,30,15,ctx);
 b2.color="#00ff00";
 blocks.push(b1);
 blocks.push(b2);
 
 c.addEventListener("click",clicked);
 window.requestAnimationFrame(animloop);

</script>
</html>