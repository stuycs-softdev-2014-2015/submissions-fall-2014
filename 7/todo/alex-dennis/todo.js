var moveToDone = function(e){
	var done = document.getElementById("completed");
	done.appendChild(this);
	this.addEventListener('click',wipeAway);
};

var wipeAway = function(e){
	var done = document.getElementById("completed");
	done.removeChild(this);
};

var addItemToToDo = function(text)
{
	var list = document.getElementById("to-do");
	var newitem = document.createElement("li");
	newitem.innerHTML = document.getElementById("textfield").value;
	list.appendChild(newitem);
	newitem.addEventListener('click',moveToDone);
};

var button = document.getElementById("submitbutton");
button.addEventListener('click',addItemToToDo);









