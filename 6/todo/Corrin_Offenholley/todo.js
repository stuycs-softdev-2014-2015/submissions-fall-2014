console.log("HELLO");

var todoList = document.getElementById('todo');
var doneList = document.getElementById('done');

var doneCallBack = function(e){
		console.log('boo');
		this.classList.toggle('red');
};

var addItemDone = function(text) {
		var list = document.getElementById('done');
		
		var entry = document.createElement('li');
		entry.appendChild(document.createTextNode(text));
		entry.addEventListener('click',doneCallBack);
		list.appendChild(entry);
};

var todoCallBack = function(e){
		addItemDone(this.innerHTML);
		this.remove();
}
var addItemTodo = function(text) {
		var list = document.getElementById('todo');
		
		var entry = document.createElement('li');
		entry.appendChild(document.createTextNode(text));
		entry.addEventListener('click',todoCallBack);
		list.appendChild(entry);
};



var buttonCallback = function(e){
		var text = document.getElementById('input').value;
		console.log(text);
		addItemTodo(text);
};
/*var todoCallback = function(e){
		var text = document.getElementById('input').value;
		console.log(text);
		addItemTodo(text);
};
var doneCallback = function(e){
		var text = document.getElementById('input').value;
		console.log(text);
		addItemTodo(text);
};*/
var button = document.getElementById("b");
button.addEventListener('click',buttonCallback);

var litems = todoList.children;

for (var i = 0 ; i < litems.length ; i++ ){
		litems[i].addEventListener('click',todoCallBack);
		
}
var litemstwo = doneList.children;
for (var i = 0 ; i < litemstwo.length ; i++ ){
		litemstwo[i].addEventListener('click',doneCallback);
		
}
/*
<ol id="done">
			
	</ol>

*/
