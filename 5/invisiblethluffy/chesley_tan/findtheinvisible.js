var mouseX = 0, mouseY = 0;
var thluffyX = 0, thluffyY = 0;
var interval = 125;
var audio = document.getElementById("audio");
var mute = false;

function setup() {
    var h = document.body.clientHeight;
    var w = document.body.clientWidth;
    var thluffy = document.createElement("img");
    var container = document.getElementById("container");
    thluffy.src = "thluffy.png";
    thluffy.id = "thluffy";
    thluffy.style.position = "relative";
    thluffy.style.opacity = 0;
    
    thluffy.draggable = false;
    thluffy.height = 100;
    thluffy.width = 125;
    thluffyX = Math.floor(Math.random() * (w - (2 * container.offsetLeft))) - thluffy.width;
    if (thluffyX < thluffy.width) {
        thluffyX = 0;
    }
    thluffyY = Math.floor(Math.random() * (h - container.offsetTop) - thluffy.width);
    if (thluffyY < 0) {
        thluffyY = 0;
    }
    thluffy.style.left = thluffyX;
    thluffy.style.top = thluffyY;
    thluffyX += thluffy.offsetLeft + thluffy.width / 2;
    thluffyY += thluffy.offsetTop + (2 * thluffy.height );
    thluffy.addEventListener("click", reveal);
    document.getElementById("reveal_button").addEventListener("click", reveal);
    container.appendChild(thluffy);
    audio.addEventListener("ended", function () {
        if (!mute) {
            this.currentTime = 0;
            setTimeout(function() {audio.play();}, interval);
        }
    });
    audio.play();
}

function updateMouseCoords(e) {
    mouseX = e.pageX;
    mouseY = e.pageY;
    var mouseStatsDiv = document.getElementById("mouse_stats");
    mouseStatsDiv.innerHTML = "X: " + mouseX + "<br/>" + "Y: " + mouseY;
}

function updateBeepIntervalAndVolume() {
    var manhattan = getManhattanDist();
    interval = 125 + (manhattan / 3);
    audio.volume = (manhattan / 100 > 1) ? 50 / manhattan : 1;
}

function reveal(e) {
    document.getElementById("thluffy").style.opacity = 100;
    mute = true;
}

function getManhattanDist() {
    return (Math.abs(mouseX - thluffyX) + Math.abs(mouseY - thluffyY));
}

document.addEventListener("DOMContentLoaded", setup);
window.addEventListener("mousemove", updateMouseCoords);
setInterval(function() {updateBeepIntervalAndVolume();}, 250);
