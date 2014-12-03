var mouseX, mouseY
<<<<<<< HEAD
=======
var findX, findY;
>>>>>>> 0fc50f4882704a62e9ce92fd1a50169eaceeba31
var dist;

window.addEventListener('mousemove', function(e) {
    mouseX = e.pageX;
    mouseY = e.pageY;
});

<<<<<<< HEAD
var light = document.createElement('img');
light.setAttribute('src', 'light.png');
light.setAttribute('height', '100px');
light.setAttribute('width', '100px');
light.style.position = 'absolute';
light.style.margin = '-50px';

var swiper = document.createElement('img');
swiper.setAttribute('src', 'swiper.png');
swiper.setAttribute('height', '50px');
swiper.setAttribute('width', '50px');
swiper.style.position = 'absolute';
swiper.style.visibility = 'hidden';
swiper.style.left =  20 + Math.random()*1000 + 'px';
swiper.style.top = 20 + Math.random()*500 + 'px';


document.getElementsByTagName('body')[0].appendChild(light);
document.getElementsByTagName('body')[0].appendChild(swiper);

var play = function() {

    var x = swiper.style.left;
    var y = swiper.style.top;
    x = x.substring(0, x.length-2)+25;
    y = y.substring(0, y.length-2)+25;

    if ( !isNaN(mouseX) && !isNaN(mouseY) ) {
	light.style.left = mouseX + 'px';
	light.style.top = mouseY + 'px';
    }

    if (mouseX < x) 
	x = x - 0 + 1;     
    else 
	x = x - 1;
    if (mouseY < y)
	y = y - 0 + 1;
    else 
	y = y - 1;
    swiper.style.left = x + 'px';
    swiper.style.top = y + 'px';
    x+=25;
    y+=25;
    dist = Math.sqrt( Math.pow(x-mouseX,2) + Math.pow(y-mouseY,2) )

    if ( dist < 45 ) 
	swiper.style.visibility = 'visible'
    else
	swiper.style.visibility = 'hidden'

    if (x < 0 || x > 1100 || y < 0 || y > 600) {
	window.alert("He got away!");
	location.reload();
    }
//    console.log(dist);
//    console.log(x + ", " + y);
//    console.log(mouseX + ", " + mouseY);

}


window.addEventListener('mousedown', function() { 
    if ( dist < 20 ) {
	window.alert("Swiper no swiping!");
	location.reload();
    }
} );

event = setInterval(play,100);
=======
var play = function() {

    findX = 400;
    findY = 400;

    dist = Math.sqrt( Math.pow(findX-mouseX,2) + Math.pow(findY-mouseY,2) )

    console.log(dist);
    console.log(mouseX + ", " + mouseY);

}

window.addEventListener('mousedown', function() { 
    if ( dist < 100 ) 
	window.alert("Yay!");
} );

event = setInterval(play,100);

>>>>>>> 0fc50f4882704a62e9ce92fd1a50169eaceeba31
