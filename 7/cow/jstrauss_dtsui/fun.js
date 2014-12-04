// Justin Strauss and Derek Tsui
// Software Development Period 7
// Invisible Cow

var mouseX;
var mouseY;
var dist;
var genX, genY;

var updateCoords = function(e) {
    mouseX=e.pageX;
    mouseY=e.pageY;
    getDist();
};

var getDist = function(e){
    dist = Math.sqrt(Math.pow(mouseX-(genX+70),2)+Math.pow(mouseY-(genY+100),2));
    console.log(dist);
}

var generate = function(e) { // create new batman in random X,Y
    genX = Math.random() * screen.width; // border 140
    genY = Math.random() * screen.height; // border 200
    console.log("(" + genX + " , " + genY + ")");
    //var batman = document.getElementByID("batman");
    var move=document.querySelector('.move');
    move.style.left=genX+"px";
    move.style.top=genY+"px";
};

var reveal = function(e) {
    if(dist <= 50){
	console.log("I'm batman!!!!!!");
    };
};

var radar = function(e){

};

var radarcheck = setInterval(radar,1000);

generate();
window.addEventListener('mousemove',updateCoords);
window.addEventListener('click',reveal);
