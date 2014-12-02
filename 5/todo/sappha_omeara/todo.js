var task = document.getElementById("newtask");
var buttonA = document.getElementById("addB");

var todoList = document.getElementById("todo");
var doneList = document.getElementById("done");

var newListItem = function() {
    var item = document.createElement('li');
    item.innerHTML = task.value;
    item.addEventListener("click", moveToDone);
    todoList.appendChild(item);
}

var moveToDone = function() {
    this.parentNode.removeChild(this);
    doneList.appendChild(this);
    this.removeEventListener("click", moveToDone);
}

buttonA.addEventListener("click", newListItem);
