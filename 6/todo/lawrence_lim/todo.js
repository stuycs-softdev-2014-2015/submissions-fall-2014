var todolist = document.getElementById("todolist");
var donelist = document.getElementById("donelist");
var newtodo = document.getElementById("newtodo");
var addtodo = document.getElementById("addtodo");

var toggleblue = function() {
    this.toggle("blue");
}
var togglered = function() {
    this.toggle("red");
}

var killTask = function() {
  donelist.removeChild(this);
}

var doTask = function() {
  this.className = "doneentry";
  this.removeEventListener("click",doTask);
  this.addEventListener("click",killTask);
  donelist.appendChild(this);
}

var addToDo = function(text) {
  var newentry = document.createElement("li");
  newentry.className = "todoentry";
  newentry.innerHTML = newtodo.value;
  newentry.addEventListener("click",doTask);
  todolist.appendChild(newentry);
};

addtodo.addEventListener("click",addToDo);