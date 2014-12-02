var button = document.getElementById("button");

var moveItem = function(){
    var todo = document.getElementById("list");
    var done = document.getElementById("dlist");
    if (this.classList.contains('red')) {
	todo.removeChild(this);
	this.classList.remove('red');
	this.classList.add('green');
	done.appendChild(this);
    }
    else{
	done.removeChild(this);
	this.classList.remove('green');
	this.classList.add('red');
	todo.appendChild(this);
    }
};


var addItem = function(){
    var todo = document.getElementById("list");
    var newitem = document.createElement('li');
    var text = document.getElementById("text").value;
    newitem.innerHTML = text;
    newitem.classList.add('red');
    newitem.addEventListener('click', moveItem);
    todo.appendChild(newitem);
};

button.addEventListener("click", addItem);
