
function remove (list, element){
	var deletelist = document.getElementById(list);
	deletelist.removeChild(element);
}

function add (list , element){
	var entry = document.createElement('li');
	entry.innerHTML = element;
	entry.addEventListener('click', remove(list, this));
	if (list == "todo"){
		//var task = document.getElementById("text").value;
		//document.getElementById('text').placeholder = "Anything Else?";
		//document.getElementById('text').value = '';
		var currentList = document.getElementById("todo");
		currentList.appendChild(entry);
	}
	else{
		var currentList = document.getElementById("completed");
		currentList.appendChild(entry);
	}
}

function addTodo () {
	var list = "todo";
	var element = document.getElementById('text');
	add(list, element)
}