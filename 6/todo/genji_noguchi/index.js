var todoList = document.getElementById("todo-ordered");
var doneList = document.getElementById("done-ordered");





//Run on callback
var markDone = function(e) {
	todoList.removeChild(this);
	this.removeEventListener("click", markDone);
	doneList.appendChild(this);
}
var markTodo = function(e) {
	var input = document.getElementById("input");
	if (input.value) {
		var newItem = document.createElement("li");
		newItem.innerHTML = input.value;
		newItem.addEventListener("click",markDone);
		todoList.appendChild(newItem);
		input.value = "";
	}
}



var submit = document.getElementById("submit");
submit.addEventListener("click",markTodo);