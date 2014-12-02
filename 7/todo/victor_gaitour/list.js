var deleteTask = function(e){
  var doneItems = document.getElementById('completed');
  doneItems.removeChild(this);
}
var doneItem = function(e){
  var doneItems = document.getElementById('completed');
  this.addEventListener('click', deleteTask);
  doneItems.appendChild(this);
}

var addTask = function(e){
  var task = document.getElementById('task').value;
  document.getElementById('task').placeholder = 'Enter Another!';
  document.getElementById('task').value = '';
  var list = document.createElement('li');
  list.innerHTML = task;
  list.addEventListener('click', doneItem);
  list.addEventListener('mouseover', function(e) {
		this.classList.toggle('red');
	});
  list.addEventListener('mouseout', function(e) {
		this.classList.toggle('black');
	});
  var curList = document.getElementById('todo');
  curList.appendChild(list);
}


var b = document.getElementById("but");
b.addEventListener('click', addTask);
