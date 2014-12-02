var mouseX, mouseY, myEvent;
var curposX = 5;
var curposY = 200;

var move = function(e){
    var topher = document.getElementById("topher");
    if (mouseX > curposX){
       curposX += 5;
   }
   else{
       curposX -=5;
   }
   if (mouseY > curposY){
       curposY += 5;
   }
   else{
       curposY -= 5;
   }
    topher.style.left = curposX + "px";
    topher.style.top = curposY + "px";
   if ((curposX == 300) && (curposY == 200)){
       alert("You won");
   }
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
}

document.getElementById("start").addEventListener('click', begin);
document.getElementById("stop").addEventListener('click', end);
