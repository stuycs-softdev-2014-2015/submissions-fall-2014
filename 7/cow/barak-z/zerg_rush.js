function Zergling (x, y) {
    this.item = document.createElement("img");
    this.image = "hand-pointer-icon.png";
    this.item.setAttribute("src",this.image);
    this.x = x;
    this.y = y;
    this.speed = 5;
    this.HP = 5;
    this.isAlive = function() {
	return this.HP > 0;
    }
    this.hit = function() {
	this.HP -= 1;
	console.log("hit");
    }
    this.item.addEventListener("click",this.hit); //problem!!
   
    document.body.appendChild(this.item);
}


var units = [];
var spawnTimer;

//item = document.createElement("img");
//item.setAttribute("src","hand-pointer-icon.png");
//document.body.appendChild(item);
//item.setAttribute("id","image");
//console.log(document.getElementById("image"));

var spawn = function() {
    //console.log("test");
    units.push(new Zergling(0,0));
    console.log(units);
}
    spawnTimer=setInterval(spawn,1000);
var stopTimer = function(e) {
    window.clearInterval(e);
}


