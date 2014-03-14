var c = document.getElementById("c");
var ctx = c.getContext("2d");

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

var addImage = function (x,y, img1,dx,dy) {
    return {
	x:x,
	y:y,
	dx:dx,
	dy:dy,
	undraw: function () {
	    ctx.fillStyle="#FFFFFF";
	    ctx.fillRect(this.x,this.y,275,250);
	},
	draw: function () {
	    img1.style.height = "200px";
	    img1.style.width = "200px";
	    ctx.drawImage(img1,this.x,this.y);
	},
	move: function () {
	    this.x = this.x + dx;
	    this.y = this.y + dy;

	}
    }
}

var createNewImage = function () {
    num = Math.floor((Math.random()*myFruit.length));
    img1 = new Image();
    img1.src= myFruit [num][0];

//The following code is modified from online (http://stackoverflow.com/questions/9880279/how-do-i-add-a-simple-onclick-event-handler-to-a-canvas-element)

    // detect event
    elemLeft = c.offsetLeft,
    elemTop = c.offsetTop,
    elements = [];

    // Add event listener for `click` events.
    c.addEventListener('click', function (event) {
	var x = event.pageX - elemLeft,
	y = event.pageY - elemTop;

	// Collision detection between clicked offset and element.
	elements.forEach(function(element) {
	    if (y > element.top && y < element.top + element.height  && x > element.left && x < element.left + element.width) {
		alert ("clicked")
		score = score + myFruit [val][1];
		if (myFruit [val][1] == 0) {
		    lives = lives - 1;
		    alert ("You have lost a life");
		}}})}, false)
  
  elements.push(img1);
    
//collision detection code from online ends here

			  xVal = Math.floor((Math.random()*1000));
			  y = 50;
			  m = addImage (xVal,y,img1,0,10);
			  return m;
			 }


    var animationLoop = function () {
	var myImg = createNewImage ();
	img1.onload = function() {
	    myImg.draw();
	}
	var intv1 = setInterval (function () {myImg.undraw ();},15);
	var intv2 = setInterval (function () {myImg.move ();},15);
	var intv3 = setInterval (function () {myImg.draw ();},15);

	
	var repeat = setTimeout (function () {window.requestAnimationFrame(animationLoop);}, 750);
	
	if (lives == 0) {
	    alert ("Game Over");
	    clearTimeout (repeat);
	    clearInterval (intv1);
	    clearInterval (intv2);
	    clearInterval (intv3);

	}
    }
    
    window.requestAnimationFrame(animationLoop);
