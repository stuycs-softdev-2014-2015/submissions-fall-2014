var finish = function(e){
	addDone(this.innerHTML);
	removeItem(this, 'todo');
};

var restart = function(e){
	addTodo(this.innerHTML);
	removeItem(this, 'done');
};

var addTodo = function(text){
	var items = document.getElementById('todo');
	var toAdd = document.createElement('li');
	toAdd.innerHTML = text;
	items.appendChild(toAdd);
	toAdd.addEventListener('click', finish);
};

var removeItem = function(element, id){
	document.getElementById(id).removeChild(element);
};

var addDone = function(text) {
	var items = document.getElementById('done');
	var toAdd = document.createElement('li');
	toAdd.innerHTML = text;
	items.appendChild(toAdd);
	toAdd.addEventListener('click', restart);
};

var buttonCallBack = function(e) {
	var input = document.getElementById('user_input').value;
	addTodo(input);
};

var button = document.getElementById('add');
button.addEventListener('click', buttonCallBack);

