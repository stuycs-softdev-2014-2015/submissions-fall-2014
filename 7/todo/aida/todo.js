var removeTask = function (e) {
	var doneList = document.getElementById('done');
	doneList.removeChild(this);
}

var addDone = function(e) {
	var doneList = document.getElementById('done');
	this.addEventListener('click', removeTask);
	doneList.appendChild(this);
}

var addToDo = function(e) {
	var newTask = document.getElementById("newtask").value;
	var toDoList = document.getElementById("todo");
	var listItem = document.createElement("li");
	listItem.innerHTML = newTask;
	listItem.addEventListener('click', addDone);
	listItem.addEventListener('mouseover', function(e) {
		this.classList.toggle('cyan');
	});
	listItem.addEventListener('mouseout', function(e) {
		this.classList.toggle('black');
	});
	toDoList.appendChild(listItem);
}

var b = document.getElementById('b');
b.addEventListener('click',addToDo);

var toDoListItems = document.getElementById('todo').children;