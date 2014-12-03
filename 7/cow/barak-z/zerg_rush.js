var spawnTimer;
var spawn = function() {
    console.log("test");

}
    spawnTimer=setInterval(spawn,1000);
var stopTimer = function(e) {
    window.clearInterval(e);
}


