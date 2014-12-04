var add = function(e) {
	var task = document.getElementById("newtask").value;
	var toDoList = document.getElementById("todo");
	var listItem = document.createElement("li");
	listItem.innerHTML = task;
	listItem.addEventListener('click', done);
	listItem.addEventListener('mouseover', function(e) {
		this.classList.toggle('red');
	});
	listItem.addEventListener('mouseout', function(e) {
		this.classList.toggle('black')
	});
	toDoList.appendChild(listItem);
}

var done = function(e) {
	var doneList = document.getElementById('done');
	this.addEventListener('click', add);
	doneList.appendChild(this);
}

var remove = function(e) {
	var doneList = document.getElementById('done');
	doneList.removeChild(this);
}

var b = document.getElementById('b');
b.addEventListener('click', add);


