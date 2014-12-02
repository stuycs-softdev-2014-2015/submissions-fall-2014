// Justin Strauss
// Software Development Period 7
// Javascript To Do List

var addItem = function(text) {
	var todolist = document.getElementById('todo');
	var newtodo = document.createElement('li');
	newtodo.innerHTML = text;
	todolist.appendChild(newtodo);
	document.getElementById('task').value = "";
	newtodo.addEventListener('click', moveItem);
};

var removeItem = function (e) {
	var donelist = document.getElementById('done');
	donelist.removeChild(this);
};

var moveItem = function(e) {
	var donelist = document.getElementById('done');
	this.addEventListener('click', removeItem);
	donelist.appendChild(this);
};

var buttonCallback = function(e) {
	var task = document.getElementById('task').value;
	if (task != ""){
		addItem(task);
	};
};

var keyCallback = function(e){
	var task = document.getElementById('task').value;
    if (e.keyCode == 13){
        addItem(task);
    };
};

var submit = document.getElementById('submit');
submit.addEventListener('click', buttonCallback);
var enter = document.getElementById('task');
enter.addEventListener('keypress', keyCallback);