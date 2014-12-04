var mouseX;
var mouseY;
var targetX =0;
var targetY=0;
var gameState=true;
var timesFound=0;

window.addEventListener('mousemove',function(e){
    mouseX=e.clientX;
    mouseY=e.clientY;
});
var randomize = function(){
    
    targetY = Math.random()*394 + 6;
    targetX = Math.random()*725;
       }    

var myevent;
var calc =function(){
     var totalDistance= Math.sqrt(((mouseX-targetX-35)*(mouseX-targetX-35))+((mouseY-targetY-66)*(mouseY-targetY-66)));
    document.getElementById("coords").innerHTML= "Distance from Epic Sax Guy is " +totalDistance
    
};

var show = function(){
    if(gameState==true){
	document.getElementById("myImg").style.opacity ='100';
	timesFound+=1;
	setTimeout(go,2000);
	}
    else{
	document.getElementById("myImg").style.opacity ='100';
	}
}

var noGo =function(){
    window.clearInterval(myevent);
    timesFound=0;
    gameState=false;
    document.getElementById("myImg").addEventListener('click',console.log("Press start to begin"));
    show();
    
};
var go = function(){
    gameState=true;
    randomize();
    document.getElementById("myImg").style.opacity='0' ;
    document.getElementById("myImg").style.top = targetY +'px' ;
    document.getElementById("myImg").style.left =targetX +'px';
    document.getElementById("myImg").addEventListener('click',show);
    myevent= setInterval(calc,100);
    document.getElementById("found").innerHTML= "You found Epic Sax Guy: "+ timesFound+" times";
    }

document.getElementById("stop").addEventListener('click',noGo);
document.getElementById("start").addEventListener('click',go);


