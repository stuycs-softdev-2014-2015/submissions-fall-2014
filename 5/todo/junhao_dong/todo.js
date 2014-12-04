var addButton = document.getElementById("addTask");
var todo = document.getElementById("todo");
var done = document.getElementById("done");

var addTask = function(e){
    var task = document.createElement("li");
    var newTask = document.getElementById("task");
    task.innerHTML = newTask.value;
    task.addEventListener("click", removeTask);
    todo.appendChild(task);
}

var removeTask = function(e){
    if (this.parentNode == todo){
	todo.removeChild(this);
	done.appendChild(this);
    }
    else{ // in done
	done.removeChild(this);
    }
}

addButton.addEventListener("click", addTask);
