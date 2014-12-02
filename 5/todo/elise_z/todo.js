var task = document.getElementById("task");
var buttonToAdd = document.getElementById("add");

var doList = document.getElementById("do_list");
var doneList = document.getElementById("done_list");

var newItem = function() {
    var item = document.createElement('li');
    item.innerHTML = task.value;
    item.addEventListener("click", moveToDone);
    doList.appendChild(item);
}

var moveToTodo = function() {
    this.parentNode.removeChild(this);
    doList.appendChild(this);
    this.removeEventListener("click", moveToTodo);
    this.addEventListener("click", moveToDone);
}

var moveToDone = function () {
    this.parentNode.removeChild(this);
    doneList.appendChild(this);
    this.removeEventListener("click", moveToDone);
    this.addEventListener("click", moveToTodo);
}

buttonToAdd.addEventListener("click", newItem);
