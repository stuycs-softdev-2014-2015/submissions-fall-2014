var mouseX, mouseY;
var hiddenX, hiddenY;
var distance;
var size = {
    width: window.innerWidth || document.body.clientWidth,
    height: window.innerHeight || document.body.clientHeight
};

var colors = ['orange','green','purple','red','blue','yellow']; 
var color = 0;
var isColor = true;

var seizure = document.getElementById("rave");
seizure.addEventListener("click",function(e){
    isColor=!isColor;
});
var colorDU = setInterval(function(e){
    if (isColor){
    document.body.style.background = colors[color%colors.length];
    color++;
    }
},1000);


var isEasy = false;

var easymode = document.getElementById("easy");
easymode.addEventListener("click",function(e){
    isEasy=!isEasy;
    var dist = document.getElementById("dist");
    dist.innerHTML = "";
    var coor = document.getElementById("coor");
    coor.innerHTML = "";
    
});



var createHiddenLocation = function(e){
    hiddenX = Math.floor(Math.random()*(size.width-100));
    hiddenY = Math.floor(Math.random()*(size.height-100));
    var pic = document.getElementById("king");
    pic.src="sandking.jpg"
    var move = document.querySelector(".move");
    move.style.left = hiddenX+"px";
    move.style.top = hiddenY+"px";
    pic.style.display = "none";
    /* DOES NOT WORK */
    pic.addEventListener("mouseover", function(e){
	this.style.cursor="pointer";
    });
    pic.addEventListener("mouseout",function(e){
	this.style.cursor="auto";
    });
    
}
createHiddenLocation();


var getDistance = function(e){
    var xplace = hiddenX - mouseX;
    var yplace = hiddenY - mouseY;
    distance = Math.sqrt(Math.pow(xplace+50,2)+Math.pow(yplace+50,2));
    if (isEasy){
	var dist = document.getElementById("dist");
	dist.innerHTML = distance;
    }
    var sand = document.getElementById("sandstorm");
    if (distance < 50){
	sand.volume = 1.0;
    }
    else if (distance < 200){
	sand.volume = 0.8;
    }
    else if (distance < 400){
	sand.volume = 0.6;
    }
    else if (distance < 600){
	sand.volume = 0.4;
    }
    else if (distance < 800){
	sand.volume = 0.2;
    }
    else{
	sand.volume = 0.1;
    }
    
}
window.addEventListener('mousemove',function(e){
    mouseX = e.pageX;
    mouseY = e.pageY;
    if (isEasy){
	var coor = document.getElementById("coor");
	coor.innerHTML = ""+mouseX+","+mouseY;
    }
    getDistance();
});
var recalculate = setInterval(getDistance,100);


var popup = function(e){
    var pic = document.getElementById("king");
    pic.style.display = "inline-block";
    
}
var checkLocation = function(e){
    if (distance <= 50){
	popup();
	var sound = document.getElementById("winner");
	winner.play();
    }
}
window.addEventListener('click',checkLocation);
console.log("hi");
