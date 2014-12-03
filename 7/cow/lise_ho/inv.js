//MOZILLA FIREFOX doesnt like this javascript... Firefox does not write onto the document the mouseX / mouseY, but other functionality does work...
var picX,picY;
var victoryScreen = function(e){
    console.log("victory");
    var r = confirm("YAY!!!\n\nYOU HAVE FOUND THLUFFY!!!\n\nPlay Again?");
    if (r){
	//location.reload();
	hide();
    }else{
	var img = document.getElementById("goal");
	img.style.visibility= "visible";
	img.removeEventListener("click",victoryScreen);
	console.log("x");
    }    
};
var hide = function(e){
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
};
window.addEventListener('load',hide);

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
//var audio = document.getElementById("z");
window.addEventListener('mousemove',function(e){
   // console.log(window.innerHeight);
//     console.log(window.innerWidth);
    mouseX = e.pageX;
    mouseY = e.pageY;
    tracker.innerText= mouseX +" , " + mouseY;
    dista.innerText= dist(mouseX,mouseY,5,5).toString();
    //if (dist(mouseX,mouseY,picX,picY)>0 ){
//	timedevent();
   // }
    
});
var myevent;
var stoptimer = function(e){
    window.clearInterval(e);
};
var timedevent = function(){
    //do your stuff
    myevent = setInterval(sound,100);
};
var sound = function(e){
    //do your stuff here
    //play music
//	audio.play();
};

var givingup = function(e){
    var r = confirm("You are giving up on Fluffy. \nIs this really okay with you? ");
    if (r){
	window.location.href="home.html";
    } 
}
var giveup = document.getElementById("giveup");
giveup.addEventListener("click",givingup);

/*

html for the audio
<audio id="z" src="static/z.mp3"></audio>

*/
