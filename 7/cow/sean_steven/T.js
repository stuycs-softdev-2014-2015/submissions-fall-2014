var image = document.getElementById("image");
var delay = 1000;
var score = 0;
var streak = 0;
var unwhacked = 0;
var paused = 0;
var started = 0;
var event;
var spawn = function() {
    clearTimeout(event); // Maybe this is necessary? Some odd issues.
    image.style.left = Math.random() * window.innerWidth + "px";
    image.style.top = Math.random() * window.innerHeight + "px";
    event = setTimeout(spawn, delay);
    if (delay <= 1000) {
	delay += 10 * unwhacked;
    }
    if (unwhacked > 0) {
	streak = 0;
    }
    unwhacked++;
    document.getElementById("delay").innerHTML = "<b>Delay: </b>" + delay;
    document.getElementById("score").innerHTML = "<b>Score: </b>" + score;
    document.getElementById("streak").innerHTML = "<b>Streak: </b>" + streak;
};
var whack = function() {
    clearTimeout(event);
    score++;
    delay -= 50;
    streak++;
    score += streak;
    unwhacked = 0;
    spawn();
};
image.addEventListener("click", whack);
document.getElementById("start").addEventListener("click", function() {
    if (started == 0) {
	started = 1;
	document.getElementById("start").value = "Reset";
	spawn();
    } else {
	started = 0;
	document.getElementById("start").value = "Start";
	delay = 1000;
	score = 0;
	document.getElementById("delay").innerHTML = "<b>Delay: </b>" + delay;
	document.getElementById("score").innerHTML = "<b>Score: </b>" + score;
	image.style.left = "100px";
	image.style.top = "100px";
	clearTimeout(event);
    }
});
document.getElementById("pause").addEventListener("click", function() {
    if (paused == 0) {
	clearTimeout(event);
	document.getElementById("pause").value = "Resume";
	paused = 1;
    } else {
	document.getElementById("pause").value = "Pause";
	paused = 0;
	spawn();
    }
});
