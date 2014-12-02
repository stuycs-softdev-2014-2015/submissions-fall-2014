//fun stuff
var task = document.getElementById("task");
var buttonToAdd = document.getElementById("add");

//the 2 lists
var doList = document.getElementById("do_list");
var doneList = document.getElementById("done_list");

//create a new task
var newItem = function() {
    var item = document.createElement('li');
    item.innerHTML = task.value;
    item.addEventListener("click", moveToDone);
    doList.appendChild(item);
}

//move something to the todo list
var moveToTodo = function() {
    this.parentNode.removeChild(this);
    doList.appendChild(this);
    this.removeEventListener("click", moveToTodo);
    this.addEventListener("click", moveToDone);
}

//move something to the completed tasks list
var moveToDone = function () {
    this.parentNode.removeChild(this);
    doneList.appendChild(this);
    this.removeEventListener("click", moveToDone);
    this.addEventListener("click", moveToTodo);
}

//does this have to go at the end?
buttonToAdd.addEventListener("click", newItem);
