var text = document.getElementById("text");
var add = document.getElementById("add");
var todo = document.getElementById("todo");
var done = document.getElementById("done");

var moveToToDo = function() {
	console.log(this);
	done.removeChild(this);
	todo.appendChild(this);
	this.removeEventListener("click", moveToToDo);
    this.addEventListener("click", moveToDone);
}

var moveToDone = function() {
	console.log(this);
	todo.removeChild(this);
	done.appendChild(this);
	this.removeEventListener("click", moveToDone);
    this.addEventListener("click", moveToToDo);
}

var addToList = function() {
	var newTask = document.createElement("li");
	newTask.innerHTML = text.value;
	console.log(text.value);
	newTask.addEventListener("click", moveToDone);
	todo.appendChild(newTask);
}

add.addEventListener("click", addToList);