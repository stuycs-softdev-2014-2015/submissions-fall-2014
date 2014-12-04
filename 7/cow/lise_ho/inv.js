//MOZILLA FIREFOX doesnt like this javascript... Firefox does not write onto the document the mouseX / mouseY, but other functionality does work...
var myevent;
var picX,picY;
var victoryScreen = function(e){
    var r = confirm("YAY!!!\n\nYOU HAVE FOUND THLUFFY!!!\n\nPlay Again?");
    if (r){
	//location.reload();
	hide();
    }else{
	var img = document.getElementById("goal");
	//img.style.display="";
	//img.style.visibility="visible"  <- not working
	img.removeEventListener("click",victoryScreen);
	img.src="static/thluffy.png";
	window.location.href="home.html";
    }    
    var c = document.getElementById("count");
    c.innerText= parseInt(c.innerText)+1;
    if (c.innerText == 4){
	alert("You have unlocked a secret feature. Click on THLUFFY DONUTS!");
    }
    if(c.innerText >=4){
	var zum = document.getElementById("zum");
	zum.href="extras/donuts.html";
	zum.innerText="THLUFFY DONUTS";
    }
};
var hide = function(e){
    var img = document.getElementById("goal");
    img.src ="static/large.gif";
    img.style.position = "absolute";
    picX = randomness(window.innerWidth-70);
    picY = randomness(window.innerHeight-70);
    img.style.left= picX +"px";
    img.style.top= picY +"px";
    img.addEventListener("click",victoryScreen);
};
window.addEventListener('load',hide);

var randomness = function(n){
    return Math.random()*n;
};
var audio = document.getElementById("zzz");
var stoptimer = function(e){
    window.clearInterval(e);
};
var soundy = function(e){
    if (distance <100){
	audio.volume = 1;
    }
    else if (distance<250){
	audio.volume = .49;
    }
    else if(distance<540){
	audio.volume = .4;
    }
    else {
	audio.volume = .17;
    }
    audio.play();
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
var distance;
window.addEventListener('mousemove',function(e){
    myevent = setInterval(soundy,700);
    mouseX = e.pageX;
    mouseY = e.pageY;
    distance = dist(mouseX,mouseY,picX,picY);
});

var givingup = function(e){
    var r = confirm("You are giving up on Fluffy.\n\nIs this really okay with you?\n ");
    if (r){
	window.location.href="home.html";
    } 
}
var giveup = document.getElementById("giveup");
giveup.addEventListener("click",givingup);

var pause = function(){
    alert("BREAK TIME.\n\nThluffy will stop hissing at you for now.\n\nPress okay with you are ready to resume your search for Thluffy.");
}
var p = document.getElementById("break");
p.addEventListener("click",pause);


var reset = document.getElementById("reset");
reset.addEventListener("click",function(e){
    hide();
});

