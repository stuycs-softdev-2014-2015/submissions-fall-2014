var todoList = document.getElementById("todo");
var doneList = document.getElementById("done");
var newItem = document.getElementById("newEntry");
var button = document.getElementById("submit");

var moveToDone = function(){
    this.removeEventListener("click",moveToDone);
    this.addEventListener("click",moveToDo);
    doneList.appendChild(this);
}

var moveToDo = function(){
    this.removeEventListener("click",moveToDo);
    this.addEventListener("click",moveToDone);
    todoList.appendChild(this);
}

var addItem = function(){
    var newListItem = document.createElement("li");
    newListItem.innerHTML = newItem.value;
    newListItem.addEventListener("click",moveToDone);
    todoList.appendChild(newListItem);
}

button.addEventListener("click",addItem);
