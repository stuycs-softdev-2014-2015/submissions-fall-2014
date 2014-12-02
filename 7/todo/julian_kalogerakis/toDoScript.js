var add = function(e) {
    input = document.getElementById("input");
    var text = input.value;
    var item = document.createElement("li");
    item.innerHTML = text;
    item.addEventListener("click", doIt);
    document.getElementById("inProg").appendChild(item);
};

var doIt = function(e) {
    var inProg = document.getElementById("inProg");
    var isDone = document.getElementById("isDone");
    var movedItem = inProg.removeChild(this);
    movedItem.removeEventListener("click", doIt);
    movedItem.addEventListener("click", undoIt);
    isDone.appendChild(movedItem);
};

var undoIt = function(e) {
    var inProg = document.getElementById("inProg");
    var isDone = document.getElementById("isDone");
    var movedItem = isDone.removeChild(this);
    movedItem.removeEventListener("click", undoIt);
    movedItem.addEventListener("click", doIt);
    inProg.appendChild(movedItem);
};

var submit = document.getElementById("submit");
submit.addEventListener("click",add);