var toDo = document.getElementById("todo");
var done = document.getElementById("done");
var button = document.getElementById("button");

var addTask = function() {
    var text = document.getElementById("text");
    var task = document.createElement("li")
    task.innerHTML = text.value;
    task.addEventListener('click', moveToDone)
    toDo.appendChild(task);
}

var moveToDone = function() {
    this.removeEventListener('click', moveToDone)
    done.appendChild(this);
    this.addEventListener('click', removeTask);
}

var removeTask = function() {
    this.removeEventListener('click', removeTask);
    done.removeChild(this);
}

button.addEventListener('click', addTask);