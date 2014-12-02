var addTodo = function(text){
	var items = document.getElementById('todo');
	var toAdd = document.createElement('li');
	toAdd.innerHTML = text;
	items.appendChild(toAdd);
};

var removeTodo = function(element){
	document.getElementById('todo').removeChild(element);
};

var addDone = function(text) {
	var items = document.getElementById('done');
	var toAdd = document.createElement('li');
	toAdd.innerHTML = text;
	items.appendChild(toAdd);
};

var finish = function(e){
	// console.log(this);
	addDone(this.innerHTML);
	removeTodo(this);
};

var giveTodoListeners = function() {
	var todo_list = document.getElementById('todo').childNodes;
	// console.log(todo_list);
	for (var i = 0; i < todo_list.length; i++){
		todo_list[i].addEventListener('click', finish);
	};
};

var buttonCallBack = function(e) {
	var input = document.getElementById('user_input').value;
	addTodo(input);
	giveTodoListeners();
};

var button = document.getElementById('add');
button.addEventListener('click', buttonCallBack);

