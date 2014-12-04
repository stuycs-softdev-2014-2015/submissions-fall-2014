var deleteTask = function(e) {
    var done = document.getElementById('completed')
    done.removeChild(this);
}

var moveDone = function(e) {
    var done = document.getElementById('completed');
    this.addEventListener('click', deleteTask );
    this.addEventListener('mouseover', function(e) {
	this.classList.toggle('red')
	});
    this.addEventListener('mouseout', function(e) {
	this.classList.toggle('black')
	});
    done.appendChild(this);
}

var addTask = function(e) {
    console.log("HOLA")
    var task = document.getElementById('newT').value;
    document.getElementById('newT').placeholder = "";
    document.getElementById('newT').value = "";
    var toDo = document.getElementById('todo');
    var list = document.createElement("li");

    list.innerHTML = task;
    list.addEventListener('click', moveDone);
    list.addEventListener('mouseover', function(e) {
	this.classList.toggle('green')
	});
    list.addEventListener('mouseout', function(e) {
	this.classList.toggle('black')
	});
    toDo.appendChild(list);
}

var b = document.getElementById('b');
b.addEventListener('click', addTask);
