var add_to_done = function (x) {
	var doneList = document.getElementById('done');
	this.addEventListener('click', removeTask);
	doneList.appendChild(this);
}

var removetask = function (x) {
	var doneList = document.getElementById('done');
	doneList.removeChild(this);
}

var add_to_do = function (x) {
	var newTask = document.getElementById("newtask").value;
	var toDoList = document.getElementById("todo");
	var listItem = document.createElement("li");
	listItem.innerHTML = newTask;
	listItem.addEventListener('click', addDone);
	listItem.addEventListener('mouseover', function(x) {
		this.classList.toggle('cyan');
	});
	listItem.addEventListener('mouseout', function(x) {
		this.classList.toggle('black');
	});
	toDoList.appendChild(listItem);
}

var submit = document.getElementById('sumbit');
sumbit.addEventListener('click',add_to_do);

var to_do_list_items = document.getElementById('todo').children;
