var score = 0;
var mosquito;
var m2;
var juice;
var x, y;
var fps = 120;

mosquito = document.createElement("img");
juice = document.createElement("img");
mosquito.setAttribute("src", "./res/mosquito.png");
mosquito.style.display = "block";
mosquito.style.position = "absolute";
mosquito.width = '20';
juice.setAttribute("src","./res/mosquito_juice.png");
document.body.appendChild(mosquito);



//Sound
//document.getElementById("hidden-sound").innerHTML= "<embed src=\"./res/sound.mp3\" hidden=\"true\" autostart=\"true\"	loop=\"true\" />";

//some code from stack overflow to clear highlighting when furiously trying
//to kill the mosquito
function clearSelection() {
    if(document.selection && document.selection.empty) {
        document.selection.empty();
    } else if(window.getSelection) {
        var sel = window.getSelection();
        sel.removeAllRanges();
    }
}


var reload = function(score) {
	console.log(score);
	mosquito.setAttribute("src", "./res/mosquito.png");
	mosquito.style.left = "600px";
	mosquito.style.top = "300px";
        if(score == 0){
	    mosquito.height = 100;
	    mosquito.width = 100;
	}
        else if(score == 1){
	    mosquito.height = 20;
	    mosquito.width = 20;
	}
}

var winAction = function() {
	mosquito.setAttribute("src","./res/mosquito_juice.png");
	score++;
	alert("You win! Score: "+ (score));
	reload(score);
}

var handleMousePos = function(e) {
	x = e.clientX;
	y = e.clientY;
	//console.log("x: "+ e.clientX + "\ty: " + e.clientY);
}

var go = function() {
        var newx2 = 0;
        var newy2 = 0;
        var dist = function(thing){
            mx = parseFloat(thing.style.left);
            my = parseFloat(thing.style.top);
            dxs = Math.pow( (mx-x), 2);
            dys = Math.pow( (my-y), 2);
            d = Math.sqrt(dxs + dys);
	    return d;
	}

        var randCoords = function(thing){
	    var randx = 0;
            var randy = 0;
     	    var k = Math.random()*40;

            if (Math.abs(dist(mosquito)) < 200){
		randx = 2*k*Math.random() - k;
		randy = 2*k*Math.random() - k;
		
		/*
		var r = Math.random();
		if(r < 0.50){
		    randx = -5*Math.random();
		    randy = -5*Math.random();
		}else{
		    randx = 5*Math.random();
		    randy = 5*Math.random();
		}
		*/
	    }else{
		randx = k*Math.random() - k/2;
		randy = k*Math.random() - k/2;
	    }
	    var newc = [randx, randy];
	    return newc;
	}
	//console.log("Randoms : "+randx+","+randy);

        var newc = randCoords(mosquito);
	var newx = parseFloat(mosquito.style.left) + newc[0];
	var newy = parseFloat(mosquito.style.top) + newc[1];

	if(newx < 0) newx = 0;
	if(newy < 0) newy = 0;
	if(newx > 1000) newx = 600;
	if(newy > 800) newy = 600;

	mosquito.style.left = newx.toString() + "px";
	mosquito.style.top = newy.toString() + "px";
     
        clearSelection();

	setTimeout( go, 1000/fps ); //loops
}


window.addEventListener("mousemove", handleMousePos);
mosquito.addEventListener("click", winAction);
reload(score);
go();
