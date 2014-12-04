var mouseX, mouseY;
var monsterX, monsterY;
var cookieX, cookieY;
var veggieX, veggieY;
var count=45;
var mover, counter;
var score=0;
var highscore=0;
var windowheight = window.innerHeight;
var windowwidth = window.innerWidth;
var veggiexvel = 22;
var veggieyvel = 22;

function timer(){
    count--;
    if (count < 0){
        clearInterval(counter);
        clearInterval(mover);
        count = 45;
        var highscored = document.getElementById("highscore");
        highscore = Math.max(highscore,score);
        highscored.innerHTML = "High Score: " + highscore;
        score = 0;
        setup();
    }
    var time = document.getElementById("timer");
    time.innerHTML = "Time: " + count;
    var scored = document.getElementById("score");
    scored.innerHTML = "Score: " + score;
}


function setup(){
    var monster = document.getElementById("monster");
    var veggie = document.getElementById("veggie");
    monster.style.left = (windowwidth / 2 - 75) + "px";
    monsterX = windowwidth / 2 - 75;
    monster.style.top = (windowheight / 2 - 80) + "px";
    monsterY = windowheight / 2 - 80;
    var ex = Math.floor(Math.random() * (windowwidth - 370)) + 50;
    var why = Math.floor(Math.random() * (windowheight - 235)) + 50;
    veggie.style.left = ex + "px";
    veggieX = ex;
    veggie.style.top = why + "px";
    veggieY = why;
    setupcookie();
}

function setupcookie(){
    var cookie = document.getElementById("cookie");
    var ex = Math.floor(Math.random() * (windowwidth - 200)) + 100;
    var why = Math.floor(Math.random() * (windowheight - 200)) + 100;
    cookie.style.left = ex + "px";
    cookieX = ex;
    cookie.style.top = why + "px";
    cookieY = why;
}

function move(){
    if ((Math.abs((monsterX+75) - (veggieX+135)) < 135) && (Math.abs((monsterY+80) - (veggieY+62.5)) < 75)){
	score--;
	setup();
    }
    if ((Math.abs((monsterX+75) - (cookieX+37.5)) < 75) && (Math.abs((monsterY+80) - (cookieY+25)) < 50)){
        score++;
        setupcookie();
    }

    var monster = document.getElementById("monster");
    if (mouseX > monsterX + 30){
        monsterX += 15;
    }
    else if (mouseX < monsterX - 30){
        monsterX -=15;
    }
    if (mouseY > monsterY + 30){
        monsterY += 15;
    }
    else if (mouseY < monsterY - 30){
        monsterY -= 15;
    }

    if (monsterY <= 30){
	monsterY = windowheight - 40;
    }
    if (monsterY >= windowheight - 30){
	monsterY = 40;
    }
    if (monsterX <= 80){
	monsterX = windowwidth - 40;
    }
    if (monsterX >= windowwidth - 30){
	monsterX = 90;
    }
    monster.style.left = monsterX + "px";
    monster.style.top = monsterY + "px";

    var veggie = document.getElementById("veggie");
    if (veggieX <= 50 || veggieX >= windowwidth - 320){
        veggiexvel = veggiexvel * -1;
    }
    if (veggieY <= 50 || veggieY >= windowheight - 185){
        veggieyvel = veggieyvel * -1;
    }
    veggieX += veggiexvel;
    veggieY += veggieyvel;
    veggie.style.left = veggieX + "px";
    veggie.style.top = veggieY + "px";
    
    var scored = document.getElementById("score");
    scored.innerHTML = "Score: " + score;
}


window.addEventListener('mousemove',function(e){
	mouseX = e.pageX;
	mouseY = e.pageY;
    });


function begin() {
    if (count == 45){
	setup();
	mover = setInterval(move,100);
	counter = setInterval(timer,1000);
    }
}


document.getElementById("start").addEventListener('click', begin);
