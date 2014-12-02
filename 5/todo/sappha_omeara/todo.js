var task = document.getElementById("newtask");
var buttonA = document.getElementById("addB");
var todoList = document.getElementById("todo");
var doneList = document.getElementById("done");

var addListItem = function() {
    var item = document.createElement('li');
    item.innerHTML = task.value;
    item.addEventListener("click", moveToDone);
    todoList.appendChild(item);
}

var moveToDone = function() {
    console.log(this);
    todoList.removeChild(this);
    doneList.appendChild(this);
    this.removeEventListener("click", moveToTodo);
    this.addEventListener("click", moveToDone);
}

var moveToTodo = function() {
    console.log(this);
    doneList.removeChild(this);
    todoList.appendChild(this);
    this.removeEventListener("click", moveToDone);
    this.addEventListener("click", moveToTodo);
}


buttonA.addEventListener("click", addListItem);
