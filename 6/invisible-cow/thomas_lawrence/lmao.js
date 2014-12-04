var spawntime = 500;
var updaterate = 30;
var lookmod = 0.5;

var aimX, aimY;
var offsetX, offsetY;
var sceneObjectList = [];
var targetList = [];

var updateEvent;
var spawnTargetEvent;

function SceneObject(element,x,y) {
    this.elem = element;
    this.initX = x;
    this.initY = y;
}

function Target(element,x,y) {
    SceneObject.call(this,element,x,y);
}
Target.prototype = Object.create(SceneObject.prototype);
Target.prototype.ouch = function(e) {
    console.log("ouch");
    this.remove();
}

function mousemove(e) {
    aimX = e.pageX;
    aimY = e.pageY;
    offsetX = lookmod * (aimX - 320);
    offsetY = lookmod * (aimY - 240);
}

function movescene(e) {
    for (var i=0; i<sceneObjectList.length; i++) {
        var tomove = sceneObjectList[i];
        tomove.elem.style.left = (tomove.initX-offsetX)+"px";
        tomove.elem.style.top = (tomove.initY-offsetY)+"px";
    }
}

function bangbang(e) {
    console.log("bangbang");
}

function spawnTarget() {
    elem = document.createElement("img");
    elem.className = "target";
    elem.setAttribute("src","b.png");

    randX = Math.floor(Math.random()*620) + 10;
    randY = Math.floor(Math.random()*460) + 10;

    var o = new Target(elem,randX,randY);

    elem.addEventListener("mousedown", o.ouch);
    document.body.appendChild(elem);
    targetList[targetList.length] = o;
    sceneObjectList[sceneObjectList.length] = o;
}

function start() {
    var elems = document.getElementsByClassName("sceneobject");
    for (var i=0; i<elems.length; i++) {
        var el = elems[i];
        var o = new SceneObject(el, el.offsetLeft, el.offsetTop);
        sceneObjectList[sceneObjectList.length] = o;
    }
    updateEvent = setInterval(movescene,1000/updaterate);
    spawnEvent = setInterval(spawnTarget,spawntime);
}

function stop() {
    window.clearTimeout(updateEvent);
}

start();
window.addEventListener("mousemove", mousemove);
window.addEventListener("mousedown", bangbang);
