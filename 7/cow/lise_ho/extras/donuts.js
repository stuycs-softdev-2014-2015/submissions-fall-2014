var pics = ["2xchoco.png","coconut.png","glazed.png","passion.jpg","pchoco.png","pink2.png"];
var myevent;
var fallevent;
var stopTimer = function(e){
   window.clearInterval(e);
}
var rand = function(n){
    return Math.round(Math.random()*n);
};

var createDonut = function(){
    var don = document.createElement('img');
    don.src = "../static/doughy/" + pics[rand(pics.length-1)];
    don.className = "donuts";
    don.style.visibility ="visible";
    don.style.height= "60px";
    don.style.width= "60px";
    don.style.position = "absolute";
    var gamearea = document.getElementById("gamearea");
    don.style.top = gamearea.offsetTop-2+"px";
    don.style.left = rand(window.innerWidth-(gamearea.offsetLeft+30)*2)+gamearea.offsetLeft-7 + "px";
    gamearea.appendChild(don);
    fallingdonuts();
}
var fallingdonuts = function(){
    var doughnuts = document.getElementsByClassName("donuts");
    for (var i=0; i<doughnuts.length; i++){
	var d = doughnuts[i].style.top;
	d = d.substring(0,d.length-2);
	d = parseInt(d);
	if (d+20 >= window.outerHeight){
	    doughnuts[i].remove();
	}else{
	    d = d+20+"px";
	    doughnuts[i].style.top = d;
	}
    }  
};

window.addEventListener("load",function(e){
    myevent = setInterval(createDonut,300);
});

