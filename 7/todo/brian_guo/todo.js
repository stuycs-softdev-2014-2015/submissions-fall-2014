
var finishedTodo = function (e){
	//console.log(finishedTodo,this);
	var deletelist = document.getElementById("todo");
	deletelist.removeChild(this);
}

var deleted = function (e) {
	//console.log(deleted,this);
	var deletelist = document.getElementById("completed");
	deletelist.removeChild(this);
}

var addToCompleted = function (e) {
	//console.log(addToCompleted,this);
	var addlist = document.getElementById("completed");
	this.addEventListener('click',deleted);
	addlist.appendChild(this);
}

var finishedTask = function (e) {
	console.log(finishedTask,this);
	this.finishedTodo;
	this.addToCompleted;
}

var add = function (e){
	var entry = document.createElement('li');
	var words = document.getElementById('text').value;
	document.getElementById('text').value = '';
	entry.innerHTML = words;
	entry.addEventListener('click', addToCompleted);
	var Todo = document.getElementById('todo');
	Todo.appendChild(entry);
}

var thebutton = document.getElementById("alpha");
thebutton.addEventListener('click',add);

