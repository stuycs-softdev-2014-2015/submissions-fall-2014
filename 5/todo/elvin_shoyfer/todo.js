// Current Task List
var currentTasks = document.getElementById("currentTasks");

// Finished Task List
var finishedTasks = document.getElementById("completedTasks");

// Button
var addTaskButton = document.getElementById("addTask");

// Textarea

var textArea = document.getElementById("taskInput");


var addNewTask = function(e) {
	var newTask = document.createElement("li");
	newTask.setAttribute("class", "list-group-item"); // Need this so CSS works

	var taskInput = textArea.value; // Take data from the textarea
	newTask.innerHTML = taskInput;

	newTask.addEventListener("click", finishTask);

	currentTasks.appendChild(newTask);
}

var finishTask = function(e) {
	currentTasks.removeChild(this);

	// Clicking will now delete it
	this.removeEventListener("click", finishTask);
	this.addEventListener("click", deleteTask); 

	finishedTasks.appendChild(this);
}

var deleteTask = function(e) {
	finishedTasks.removeChild(this);
}

addTaskButton.addEventListener("click", addNewTask);