var mouseX, mouseY, myEvent;
var tophX = 0;
var tophY = 200;
var moranX = 600;
var moranY = 0;
var mDirection = true;

var move = function(e){
  var topher = document.getElementById("topher");
  if (mouseX > tophX){
   tophX += 7;
 }
 else{
   tophX -=7;
 }
 if (mouseY > tophY){
   tophY += 7;
 }
 else{
   tophY -= 7;
 }
 topher.style.left = tophX + "px";
 topher.style.top = tophY + "px";
 // if ((tophX == 300) && (tophY == 200)){
 //   alert("You won");
 // }

 var moran = document.getElementById("moran");
 if (mDirection == true){
  moranY += 14;
  if (moranY >= window.innerHeight){
    mDirection = !mDirection;
  }
}

console.log(window.innerHeight);

if (mDirection == false) {
  moranY -= 14;
  if (moranY <= 0){
    mDirection = !mDirection;
  }
}

 moran.style.top = moranY + "px";

}

window.addEventListener('mousemove',function(e){
  mouseX = e.pageX;
  mouseY = e.pageY;
});

function begin() {
    myEvent = setInterval(move,100);
}


function end() {
    window.clearTimeout(myEvent);
    var topher = document.getElementById("topher");
    topher.style.left = "0px";
    topher.style.top = "200px";
    moran.style.top = "0px";
}

document.getElementById("start").addEventListener('click', begin);
document.getElementById("stop").addEventListener('click', end);
