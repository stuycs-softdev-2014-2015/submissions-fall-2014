
var add_ToDoList = function(e) {
		var entry = document.createElement('li');
		entry.appendChild(document.createTextNode(input.value));
		input.value = '';
		entry.addEventListener('click', moveToDone);
		thelist.appendChild(entry);
}

var moveToDone = function(e) {
	//console.log(this);
	console.log('problem');
	this.parentNode.removeChild(this);
	donelist.appendChild(this);
	this.addEventListener('click', moveToStuff);
}

var moveToStuff = function(e) {
	//console.log(this);
	this.parentNode.removeChild(this);
	thelist.appendChild(this);
	this.addEventListener('click', moveToDone);
}


var input = document.getElementById('new_item');
var butt = document.getElementById("add");
butt.addEventListener('click', add_ToDoList);


var donelist = document.getElementById("done");
var thelist = document.getElementById("stuff");
var litems = thelist.children;
for (var i = 0; i < litems.length; i++){
		litems[i].addEventListener('click', moveToDone);
}




