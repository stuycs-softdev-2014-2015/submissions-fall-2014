var doList = document.getElementById("todo");
var doneList = document.getElementById("done");

var text = document.getElementById("txt");
var button = document.getElementById("but");

var newItem = function() {
    var item = document.createElement('li');
    item.innerHTML = text.value;
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

button.addEventListener("click", newItem);
