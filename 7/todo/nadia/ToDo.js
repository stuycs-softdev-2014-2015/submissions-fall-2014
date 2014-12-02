var removeItem = function(e) {
    var DL = document.getElementById("DL");
    DL.removeChild(this);
};

var moveItem = function(e) {
    this.removeEventListener("click", moveItem);
    var DL = document.getElementById("DL");
    DL.appendChild(this);
    this.addEventListener("click", removeItem);
};


var addTask = function(e) {
    var TDL = document.getElementById("TDL");
    var newTask = document.getElementById("input").value;
    if (newTask != "") {
	var newItem = document.createElement("li");
	newItem.innerHTML = newTask;
	newItem.addEventListener("click", moveItem);
	TDL.appendChild(newItem);
    }
}

var keyCallback = function(e) {    
    if (e.keyCode == 13) {
	addTask(e);
    }
};

var b = document.getElementById("b");
b.addEventListener("click", addTask);
var input = document.getElementById("input");
input.addEventListener("keypress", keyCallback);
