var todoList = document.getElementById("todo");
var doneList = document.getElementById("done");
var button = document.getElementById("button");

var add = function add(){
    var n = document.createElement("li");
    n.innerHTML = document.getElementById("input").value;
    n.addEventListener("click", done);
    todoList.appendChild(n);
}

var done = function done(){
    this.removeEventListener("click", done);
    doneList.appendChild(this);
    this.addEventListener("click", remove);
}

var remove = function remove(){
    this.removeEventListener("click", remove);
    doneList.removeChild(this);
}

button.addEventListener("click", add);
