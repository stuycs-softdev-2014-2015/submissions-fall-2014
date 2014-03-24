var  myFruit = new Array ();
myFruit[0] = new Array ("apple.jpeg", 1);
myFruit[1] = new Array ("Bannanas.jpg", 2);
myFruit[2] = new Array ("Kiwi.jpeg", 3);
myFruit[3] = new Array ("Orange.jpg", 2);
myFruit[4] = new Array ("Pear.jpeg",3);
myFruit[5] = new Array ("Pinapple.jpeg", 5);
myFruit[6] = new Array ("Strawberry.jpeg",5);
myFruit[7] = new Array ("Tomato.jpeg", 1);
myFruit[8] = new Array ("bomb.jpg", 0);
myFruit[9] = new Array ("bomb.jpg", 0);
myFruit[10] = new Array ("bomb.jpg", 0);


var score = 0;
var lives = 3;

var printScores = function () {
    textDiv = document.getElementById ("textdiv");
    textDiv.innerHTML = "";
    var sc  = document.createTextNode("Score: ");
    textDiv.appendChild(sc);

    var sc  = document.createTextNode(score);
    textDiv.appendChild(sc);
    textDiv.appendChild(document.createElement("br"));
    var lv  = document.createTextNode("Lives: ");
    textDiv.appendChild(lv);

    var lv  = document.createTextNode(lives);
    textDiv.appendChild(lv);
}

printScores ();
score = 0;
var addScore = function (val) {
    console.log (score);
    score = score + myFruit [val][1];
    if (myFruit [val][1] == 0) {
	if (lives <= 1) {
	    lives = lives - 1;
	    printScores ();
	    alert ("GameOver");
	    clearInterval (intv1);
	    clearInterval (intv2);	}
	else {
	    lives = lives - 1;
	    alert ("You have lost a life");}}
    printScores ();
}

var addImage = function (s) {
    num = Math.floor((Math.random()*myFruit.length));
    img1 =  myFruit [num][0];
    xVal = Math.floor((Math.random()*900));
    yVal = 40;
    svgimg = document.createElementNS('http://www.w3.org/2000/svg','image');
    svgimg.setAttribute('height','250');
    svgimg.setAttribute('width','250');
    svgimg.setAttribute('id','fruit');
    svgimg.setAttributeNS('http://www.w3.org/1999/xlink','href',img1);
    svgimg.setAttribute('x',xVal);
    svgimg.setAttribute('y',yVal);
    svgimg.setAttribute('itemNum',num);
    svgimg.addEventListener('click',cClick);
    s.appendChild(svgimg);
}

var move = function() {
   var cs = document.getElementsByTagName("image");
   for (var i=0;i<cs.length;i++) {
     var x = parseInt(cs[i].getAttribute('x'));
     var y = parseInt(cs[i].getAttribute('y'));
     y = y + 10;
     cs[i].setAttribute('y',y);
   }
}
s = document.getElementById ("s");


var cClick = function(e) {
    e.preventDefault();
    val = this.getAttribute('itemNum');
    this.remove();
    addScore (val);
 }

var cs = document.getElementsByTagName("image");
var intv1 = setInterval (function () {move()},10);
var intv2 = setInterval (function () {addImage(s)},750);

for (var i=0;i<cs.length;i++) {
    var y = parseInt(cs[i].getAttribute('y'));
    if (y > 1000) {
	cs[i].remove();
    }
}


