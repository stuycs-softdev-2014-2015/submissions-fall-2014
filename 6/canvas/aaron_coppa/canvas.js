var c = document.getElementsByTagName("canvas")[0];
var ctx = c.getContext("2d");
var x1 = Math.random() * 100;
var y1 = Math.random() * 100;
var r = 30;
var counter = 0;

function drawEllipseByCenter(ctx, cx, cy, w, h) {
  drawEllipse(ctx, cx - w/2.0, cy - h/2.0, w, h);
}

function drawEllipse(ctx, x, y, w, h) {
  var kappa = .5522848,
      ox = (w / 2) * kappa, // control point offset horizontal
      oy = (h / 2) * kappa, // control point offset vertical
      xe = x + w,           // x-end
      ye = y + h,           // y-end
      xm = x + w / 2,       // x-middle
      ym = y + h / 2;       // y-middle

  ctx.beginPath();
  ctx.moveTo(x, ym);
  ctx.bezierCurveTo(x, ym - oy, xm - ox, y, xm, y);
  ctx.bezierCurveTo(xm + ox, y, xe, ym - oy, xe, ym);
  ctx.bezierCurveTo(xe, ym + oy, xm + ox, ye, xm, ye);
  ctx.bezierCurveTo(xm - ox, ye, x, ym + oy, x, ym);
  ctx.closePath();
  ctx.stroke();
}

var newCicle = function() {
    x1 = Math.random() * c.width;
    y1 = Math.random() * c.height;
    r = Math.random() * 60 + 40;
    ctx.fillStyle = "#FF6666";
    ctx.fillRect(0,0,c.width,c.height);
    ctx.fillStyle = "#CC99FF";
    drawEllipseByCenter(ctx, x1, y1, r, r);
}
var clicked = function(e) {
    e.preventDefault();
    x = e.pageX - c.getBoundingClientRect().left;
    y = e.pageY - c.getBoundingClientRect().top;
    if( Math.sqrt( ((x1 - x)*(x1 - x)) + ((y1 - y)*(y1 - y)) ) < r ) {
        newCicle();
        counter++;
    }
}
var end = function(){ 
    var str = "Killed " + counter + " circles";
    alert( str );
    newCicle();
    counter = 0;
}
c.addEventListener("click", clicked);
setInterval(function(){end();},5000);
ctx.fillStyle = "#FF6666";
ctx.fillRect(0,0,c.width,c.height);
drawEllipseByCenter( ctx, x1, y1, r, r );
