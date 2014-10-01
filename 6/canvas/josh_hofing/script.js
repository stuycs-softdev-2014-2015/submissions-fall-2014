var canvas = document.getElementById("can");
canvas.width = 255;
canvas.height = 255;
var ctx = canvas.getContext("2d");

ctx.fillRect(0, 0, canvas.width, canvas.height);

var fib = function(){
  var fibcache = {}
  function fib(n) {
    if (fibcache[n] == undefined) {
      if (n < 2) fibcache[n] = 1;
      else fibcache[n] = fib(n-1) + fib(n-2);
    }
    return fibcache[n];
  }
  return fib;
}();

for (var i = 0; i < canvas.width; i++) {
  fib(i);
}
var k = 1;
var kup = true;
var sizeup = true;
var step = 8;
function run() {
  var w = window,
      d = document,
      e = d.documentElement,
      g = d.getElementsByTagName('body')[0],
      x = w.innerWidth || e.clientWidth || g.clientWidth,
      y = w.innerHeight|| e.clientHeight|| g.clientHeight;
  canvas.width = x;
  canvas.height = y;
  var size = (x+y) / 2 / step;
  for (var i = 0; i < canvas.width; i+=size) {
    var first = fib(i);
    for (var j = 0; j < canvas.height; j+=size) {
      var second = fib(j);
      var color = (first * second);
      //ctx.fillStyle = "" + (color % (k));
      ctx.fillStyle = "rgb("+(first%k)+","+(second%k)+","+(color%k)+")";
      ctx.fillRect(i, j, size+1, size+1);
    }
  }
  if (k%255 == 0) kup = !kup;
  kup ? k++ : k--;
  //var tot = 0;
  //var n = 0;
  //for (var i = 0; i < 50; i++) {
    //tot += (k-i)%150;
    //n++;
  //}
  //step += Math.round(Math.random()*2 - 1);
  sizeup ? step++ : step--;
  if (step < 16) sizeup = true;
  if (step > 64) sizeup = false;
  //setTimeout(run, tot/n);
  setTimeout(run, 50);
}
run();
