// remove the element from the list
var deleteTask = function(e){
  var doneItems = document.getElementById('done');
  doneItems.removeChild(this);
}

// Move item to done list, it retains coloring listeners
var doneItem = function(e){
  var doneItems = document.getElementById('done');
  this.addEventListener('click', deleteTask);
  doneItems.appendChild(this);
}

// Move item to the not done list, make it moveable to done list through click, give coloring properties
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
  var curList = document.getElementById('not-done');
  curList.appendChild(list);
}


var b = document.getElementById("but");
b.addEventListener('click', addTask);
