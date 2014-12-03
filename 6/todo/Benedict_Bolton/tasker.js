console.log("Hello Santa, we have begun it seems.");



var addTask = function(){
  console.log(this);
  var newTask = document.getElementById("newTask").value;
  console.log(newTask);
  var toDo = document.getElementById("doList");
  var next = document.createElement('li');
  next.innerHTML = newTask;
  console.log(next);
  toDo.appendChild(next);
}

var taskDone = function() {
  console.log(this)
  var done = document.getElementById("doneList");
  var num = document.getElementById("moveTask").value;
  var toDo = document.getElementById("doList").children;
  var move = toDo[num - 1];
  console.log(move);
  move.remove();
  done.appendChild(move);
}

var itemDel = function () {
  console.log(this);
  var done = document.getElementById("doneList").children;
  var num = document.getElementById("delTask").value;
  var remove = done[num - 1];
  remove.remove();
}


var button = document.getElementById("addNew");
var buttonTwo = document.getElementById("move");
var buttonThree = document.getElementById("delete");

button.addEventListener("click", addTask);
buttonTwo.addEventListener("click", taskDone);
buttonThree.addEventListener("click", itemDel);

var colorfy = function (elem, num) {
  var done = document.getElementById("doneList").children;
  console.log(done);
  var toDo = document.getElementById("doList").children;
  if ('red' in elem.classList){
    elem.classList.remove('red');
    elem.classList.add('green');
  }
  else if ('green' in elem.classList){
    elem.classList.remove('green');
    elem.classList.add('red');
  }
  else if(num%2 == 0) {
    elem.classList.toggle('red');
  }
  else if (num%2 == 1) {
    elem.classList.toggle('green');
  }
}

var listItems = document.getElementsByTagName("li");
console.log(listItems);

for (var c = 0; c < listItems.length; c++ ){
  listItems[c].addEventListener('keypress', colorfy(listItems[c], c));
}
