var addItemToToDo = function(text)
{
		var list = document.getElementById("to-do");
		var newitem = document.createElement("li");
		newitem.innerHTML = document.getElementById("textfield").value;
		list.appendChild(newitem);
};

var button = document.getElementById("submitbutton");
button.addEventListener('click',addItemToToDo);