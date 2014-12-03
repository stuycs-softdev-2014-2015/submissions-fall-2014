//MOZILLA FIREFOX doesnt like this javascript... :(
//bouncey balls???
var picX,picY;

var victoryScreen = function(e){
    
    
};
window.addEventListener('load',function(e){
    var img = document.getElementById("goal");
    img.style.position = "absolute";
    picX = randomness(window.innerWidth-70);
    picY = randomness(window.innerHeight-70);
    img.style.left= picX +"px";
    img.style.top= picY +"px";
    console.log(picX);
    console.log(picY);
    img.style.visibility="hidden";
    img.addEventListener("click",victoryScreen);
});
var randomness = function(n){
    return Math.random()*n;
};
var tracker = document.getElementById("tracker");
var dista = document.getElementById("dist");
var mouseX, mouseY;
var sq = function(d){
    return Math.pow(d,2);
};
var dist = function(x1, y1, x2,y2){
    return Math.sqrt(sq(y2-y1)+ sq(x2-x1));
};
var audio = document.getElementById("z");
window.addEventListener('mousemove',function(e){
   // console.log(window.innerHeight);
//     console.log(window.innerWidth);
    mouseX = e.pageX;
    mouseY = e.pageY;
    tracker.innerText= mouseX +"," + mouseY;
    dista.innerText= dist(mouseX,mouseY,5,5).toString();
    if (dist(mouseX,mouseY,picX,picY)>0 ){
	//play music
//	audio.play();
    }
    
});
var myevent;
var stoptimer = function(e){
    window.clearInterval(e);
};
var timedevent = function(){
    //do your stuff

    myevent = setInterval(act,100);
};
var act = function(e){
    //do your stuff here

};



/*

html for the audio
<audio id="z" src="static/z.mp3"></audio>

*/