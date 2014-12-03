var mouseX, mouseY;
var dist;

window.addEventListener('mousemove', function(e) {
    mouseX = e.pageX;
    mouseY = e.pageY;
});

//Image Light
var light = document.createElement('img');
light.setAttribute('src', 'light.png');
light.setAttribute('height', '100px');
light.setAttribute('width', '100px');
light.style.position = 'absolute';
light.style.margin = '-50px';

//Image Swiper
var swiper = document.createElement('img');
swiper.setAttribute('src', 'swiper.png');
swiper.setAttribute('height', '50px');
swiper.setAttribute('width', '50px');
swiper.style.position = 'absolute';
swiper.style.visibility = 'hidden';
//random coordinates
swiper.style.left = Math.random()*window.innerWidth + 'px';
swiper.style.top = Math.random()*window.innerHeight + 'px';
console.log(swiper.style.left + ", " + swiper.style.top);

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

    //move swiper
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

    //track distance from swiper
    dist = Math.sqrt( Math.pow(x-mouseX,2) + Math.pow(y-mouseY,2) );

    //light gets larger when closer to swiper, swiper is visible in the light
    if ( dist > 50 && dist < 100 ) {
	light.setAttribute('height', '150px');
	light.setAttribute('width', '150px');
	light.style.margin = '-75px';
	swiper.style.visibility = "hidden";
    } else if ( dist < 50 ) {
	light.setAttribute('height', '170px');
	light.setAttribute('width', '170px');
	light.style.margin = '-85px';
	swiper.style.visibility = 'visible';
    } else {
	light.setAttribute('height', '100px');
	light.setAttribute('width', '100px');
	light.style.margin = '-50px';
	swiper.style.visibility = 'hidden';
}

    //swiper is out of the window
    if (x < 0 || x > window.innerWidth || y < 0 || y > window.innerHeight) {
	window.alert("He got away!");
	location.reload();
    }
};

//swiper is found
window.addEventListener('mousedown', function() { 
    if ( dist < 20 ) {
	window.alert("Swiper no swiping!");
	location.reload();
    }
} );

event = setInterval(play,100);
