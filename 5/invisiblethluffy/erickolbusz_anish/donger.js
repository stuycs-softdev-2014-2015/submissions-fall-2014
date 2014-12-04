//ᕕ( ᐛ )ᕗ

var donger_image = document.getElementById("donger");
var kek_image = document.getElementById("kek");
var dancedong_image = document.getElementById("dancingdonger")
var score_disp = document.getElementById("scoredisplay"); //shows current score
var dongx,dongy;
var kekx,keky;
var eX, eY;
var global_dist;
var score;
var colors = ['Blue', 'CornflowerBlue', 'LightSteelBlue','LightCoral', 'IndianRed', 'FireBrick'];


//this takes the url and grabs the variables in it, then selects the value of score to store
var params = {};

if (location.search) {
    var parts = location.search.substring(1).split('&');

    for (var i = 0; i < parts.length; i++) {
        var nv = parts[i].split('=');
        if (!nv[0]) continue;
        params[nv[0]] = nv[1] || true;
    }
}

//getting the score
score = params.score;
//if it bugs out and doesnt have a score (i.e. just starting out) then it gives of NaN so let's fix that
score = score || 0;
//displaying the score
score_disp.innerHTML = "Score: "+score;


window.addEventListener('mousemove',update_mouse_cor);

var update_mouse_cor = function(e) {
    //changes globals mouse_xcor and _ycor to reflect current state, used for clicking and distance 
    eX = e.pageX;
    eY = e.pageY;

    //calculates distance
    var dong_distance = Math.floor(Math.sqrt(Math.pow(dongx-eX, 2) + Math.pow(dongy-eY,2)));
	var kek_distance = Math.floor(Math.sqrt(Math.pow(kekx-eX , 2) + Math.pow(keky-eY , 2)));

	global_dist = Math.max(dong_distance,kek_distance);

	if (global_dist > 750)
		dancedong_image.src = "1dd.jpg"
	else if (global_dist > 600)
		dancedong_image.src = "2dd.jpg"
	else if (global_dist > 450)
		dancedong_image.src = "3dd.jpg"
	else if (global_dist > 300)
		dancedong_image.src = "4dd.jpg"
	else if (global_dist > 150)
		dancedong_image.src = "5dd.jpg"
	else
		dancedong_image.src = "6dd.jpg"
}

var dong_dance = function(){
	//if (global_dist > 150)
	//	dancedong_image.style.backgroundColor = colors[0];
	//setting colors like this didn't work for some reason...

	//originally had color code hre
}

//----- DONGER -----
var setup_donger = function() {
    //generates random coordinates for the donger
    var xcor = Math.floor(Math.random() * (window.innerWidth - 437));
    var ycor = Math.floor(Math.random() * (window.innerHeight - 225));
    //this is used when generating kek and clicking
    dongx = xcor;
    dongy = ycor;
    //sets coordinates
    donger_image.style.left = xcor+"px";
    donger_image.style.top = ycor+"px";
    //clickerino = winerino
    donger_image.addEventListener('click',found_donger);
}

var found_donger = function() {
    //changing from blank to revealed donger
    donger_image.src = "donger.jpg";
    //waits a bit before redirecting to youtube
    score++;
    console.log(score);
    setTimeout(function() {
	window.location = "?score="+score;
    }
	       , 1500);
}



//----- KEK -----
var setup_kek = function(dongx,dongy) {
    //generates random coordinates for the kek
    var xcor = Math.floor(Math.random() * (window.innerWidth - 225));
    var ycor = Math.floor(Math.random() * (window.innerHeight - 225));
    //no overlap allowed!
    while ((Math.abs(xcor-dongx) <= 437) || (Math.abs(ycor-dongy) <=225)) {
	xcor = Math.floor(Math.random() * (window.innerWidth - 225));
	ycor = Math.floor(Math.random() * (window.innerHeight - 225));
    }
    //this is used for clicking
    kekx = xcor;
    keky = ycor;
    //sets coordinates
    kek_image.style.left = xcor+"px";
    kek_image.style.top = ycor+"px";
    //click event
    kek_image.addEventListener('click',found_kek);
}

var found_kek = function() {
    //changing from blank to revealed kek
    kek_image.src = "kek.jpg";
    //rest in peace you lost
    alert("Game over! Your final score was "+score+" dongers.");
    //waits a bit before redirecting to youtube
    setTimeout(function() {
	window.location = "https://www.youtube.com/watch?v=dQw4w9WgXcQ";
    }
	       , 1500);
}



//----- Start -----
setup_donger();
setup_kek(dongx,dongy);

    
    
