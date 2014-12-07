var mouseX, mouseY;
var targetX, targetY;
var container = document.getElementById("container");

var distance, inRange = false;
var reqDistance = 100; // Threshold in pixels

// Audio tag
var audio = document.getElementById("audio");

function init(){
    var clientHeight = window.innerHeight;
    var clientWidth = window.innerWidth;
    console.log(clientHeight);

    // Create target
    var target = document.createElement("img");

    // Uncomment the next line when done debugging:
    //target.style.opacity = 0;

    target.style.draggable = false;
    target.style.position = "absolute";
    target.src = "thluffy.jpg";
    target.id = "target";

    // Generate random Target X, Y coordinates within container
    targetX = Math.floor(Math.random() * (clientWidth - 0)) + 0;
    targetY = Math.floor(Math.random() * (clientHeight - 0)) + 0;
    console.log(targetX + ' ' + targetY);
    console.log('heyyo' + clientHeight + ' ' + clientWidth);

    // Add target to the page
    container.appendChild(target);

    // Set the target's coordinates
    target.style.left = targetX + "px";
    target.style.top = targetY + "px";

    // Setting up event listeners for mouse movement, clicking
    window.addEventListener("mousemove", update);
    window.addEventListener("click", click);

    audio.volume = 0.1;
};

function update(e){
    // Get current mouse cursor position
    mouseX = e.pageX;
    mouseY = e.pageY;

    // Compute distance from target

    distance = calcDistance();

    console.log(distance);
    if (distance < reqDistance) {
        inRange = true;
    }
    else {
        inRange = false;
    }

    if (inRange) {
        document.body.style.cursor = 'crosshair';
    } else {
        document.body.style.cursor = 'defualt';
    }

   console.log(inRange);
   incVolume();
};

function click(e){
    if (inRange){
        console.log("Hit!");
        target.style.opacity = 100;
        window.clearInterval(event);
   }
};

function calcDistance(){
    //console.log('mouseX' + mouseX + 'mouseY' + mouseY + 'imgX' + targetX + 'y' + targetY);
    var distance = parseInt(Math.sqrt(
        Math.pow(mouseX - targetX, 2) + 
       Math.pow(mouseY - targetY, 2)))
    return distance;
};

function incVolume(){
    console.log(audio.volume + "Here");
    if (audio.volume < 0.95) {
        audio.volume = audio.volume + 0.001;
    }
    audio.play()
};

init();
//console.log(calcDistance());