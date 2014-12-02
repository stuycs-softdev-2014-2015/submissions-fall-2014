var removeTodo = function(e) {
    var isdonelist = document.getElementById("isdonelist");
    isdonelist.removeChild(this);
};

var moveTodo = function(e) {
    this.removeEventListener("click", moveTodo);
    var isdonelist = document.getElementById("isdonelist");
    isdonelist.appendChild(this);
    this.addEventListener("click", removeTodo);
};

var addTodo = function(e){
    var todolist = document.getElementById("todolist");
    var newItem = document.getElementById("newItem").value;
    if (newItem!=""){
	var newTodo = document.createElement("li");
	newTodo.innerHTML = newItem;
	newTodo.addEventListener("click", moveTodo);
	todolist.appendChild(newTodo);
	}
};

var keyCallback = function(e){
    if (e.keyCode==13){addTodo(e);}
};

var b = document.getElementById("b");
b.addEventListener("click", addTodo);
var newItem = document.getElementById("newItem");
input.addEventListener("keypress", keyCallback);
