var item = document.getElementById("item");
var add = document.getElementById("add");
var to_do = document.getElementById("to_do");
var done = document.getElementById("done");


var reItem = function() {
    console.log(this);
    todo.removeChild(this);
    done.appendChild(this);
    this.removeEventListener("click", reItem);
}

var addItem = function() {
    console.log(item.value);
    var newTask = document.createElement("li");
    newTask.innerHTML = item.value;
    newTask.addEventListener("click", reItem);
    to_do.appendChild(newTask);
}

add.addEventListener("click", addItem);
