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


var printLocation = function(){
    console.log(""+mouseX+","+mouseY);
};


window.addEventListener('mousemove',function(e){
    mouseX = e.pageX;
    mouseY = e.pageY;
    coor = document.getElementById("coor");
    coor.innerHTML = ""+mouseX+","+mouseY;
    getDistance();
});

/*
var seizure = document.getElementById("rave");
seizure.addEventListener("click",function(e){
    isColor=!isColor;
});
*/

var stopTimer = function(e){
    window.clearInterval(e);
}

var popup = function(e){
    var pic = document.getElementById("king");
    pic.src="sandking.jpg"
}

var createHiddenLocation = function(e){
    hiddenX = Math.floor(Math.random()*size.width);
    hiddenY = Math.floor(Math.random()*size.height);
    var pic = document.getElementById("king");
    //pic.style.position="absolute";
    pic.hspace=hiddenX;
    pic.vspace=hiddenY;
    //pic.style.display="none";
}

var getDistance = function(e){
    var xplace = hiddenX - mouseX;
    var yplace = hiddenY - mouseY;
    console.log(xplace);
    console.log(Math.pow(xplace,2));
    distance = Math.sqrt(Math.pow(xplace+10,2)+Math.pow(yplace+170,2));
    console.log(distance);
    dist = document.getElementById("dist");
    dist.innerHTML = distance;
}



createHiddenLocation();
var recalculate = setInterval(getDistance,100);
/*
var colorDU = setInterval(function(e){
    if (isColor){
	document.body.style.background = colors[color%colors.length];
	color++;
    }
},1000);
*/
var checkLocation = function(e){
    if (distance <= 50){
	popup();
    }
}
window.addEventListener('click',checkLocation);
