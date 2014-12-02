var addTask = function(e){
  var task = document.getElementById("task").value;
  var list = document.createElement("li");
  list.innerHTML = task;
  listItem.addEventListener('click', done);
  listItem.addEventListener('mouseover', this.classList.toggle("red"));
  listItem.addEventListener('mouseout', this.classList.toggle("black"));
  var curList = document.getElemenentById("not_done");
  curList.appendChild(list);
}

var done = function(e){
  var doneItems = document.getElementById("done").value;
  var notDoneItems = document.getElementById("task").value;
  this.removeEventListener('click', done);
  this.addEventListener('click', delete);
  this.addEventListener('mouseover', this.classList.toggle("red"));
  this.addEventListener('mouseout', this.classList.toggle("black"));
  doneItems.appendChild(this);
  notDoneItems.removeChild(this);
}

var delete = function(e){
  var doneItems = document.getElementById("done").value;
  doneItems.removeChild(this);
}

var b = document.getElementById("b");
b.addEventListener('click', addTask);
