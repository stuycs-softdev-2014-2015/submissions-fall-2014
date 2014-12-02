var button = document.getElementById("button");
var todo = document.getElementById("todo");
var done = document.getElementById("done");
var text = document.getElementById("add");

var makedone = function(e) {
    this.removeEventListener("click", makedone);
    done.appendChild(this);
};

var addItem = function(e) {
    var n = document.createElement("li");
    n.innerHTML = text.value;
    n.addEventListener("click", makedone);
    todo.appendChild(n);
    text.value="";
    text.focus();
};

button.addEventListener("click", addItem);
text.addEventListener("keypress", function(e) {
	if (e.keyCode === 13) {
	    addItem();
	}
    }, false);