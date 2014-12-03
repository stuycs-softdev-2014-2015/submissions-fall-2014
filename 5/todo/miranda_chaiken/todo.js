var button =document.getElementById("add");

var removeItem =function(e){
	var todo = document.getElementById("to_do");
	var done = document.getElementById("done");
	this.classList.add("grey");
	this.classList.remove("active");
	this.children[0].disabled=true;
	this.children[0].checked=true;
	done.appendChild(this);

};

var addItem = function(e){
	console.log("add item")
    var todo = document.getElementById("to_do");
	var newitem = document.createElement('li');
	newitem.classList.add("active");
	newitem.innerHTML= "<input type='checkbox''> "+document.getElementById("new item").value
	newitem.addEventListener('click',removeItem)
	todo.appendChild(newitem);
};

button.addEventListener('click',addItem);
