var todo = document.getElementById("todo");
var done = document.getElementById("done");
var b = document.getElementById("b");

var del = function() {
	done.removeChild(this);
}

var turnRed = function() {
	console.log(this);
	this.classList.toggle('red');
}

var moveDone = function() {
	this.removeEventListener("click", turnRed);
	this.removeEventListener("dblclick", moveDone);
	this.addEventListener("click", del);
	done.appendChild(this);
}

var newToDo = function() {
	var newli = document.createElement("li");
	newli.innerHTML = document.getElementById("td").value;
	newli.addEventListener("click", turnRed);
	newli.addEventListener("dblclick", moveDone);
	todo.appendChild(newli);
	document.getElementById("td").value='';
} 

b.addEventListener('click', newToDo); 