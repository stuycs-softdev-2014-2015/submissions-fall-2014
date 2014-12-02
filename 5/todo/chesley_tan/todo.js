var textarea = document.getElementById("textarea");
var addButton = document.getElementById("add");
var todoList = document.getElementById("todo_list");
var doneList = document.getElementById("done_list");

var addTodo = function() {
    var newItem = document.createElement('li');
    newItem.innerHTML = textarea.value;
    newItem.addEventListener("click", moveToDone);
    todoList.appendChild(newItem);
}

var moveToTodo = function () {
    this.parentNode.removeChild(this);
    todoList.appendChild(this);
    this.removeEventListener("click", moveToTodo);
    this.addEventListener("click", moveToDone);
}

var moveToDone = function () {
    this.parentNode.removeChild(this);
    doneList.appendChild(this);
    this.removeEventListener("click", moveToDone);
    this.addEventListener("click", moveToTodo);
}

addButton.addEventListener("click", addTodo);
