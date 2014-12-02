console.log("TODOLIST");

var todolist = document.getElementById('todo');
var completed = document.getElementById('completed');

var undoTask = function(){
    var info = this.innerHTML;
    var newitem = document.createElement('li');
    newitem.innerHTML=info;
    newitem.addEventListener('click',completeTask);
    todolist.appendChild(newitem);
    this.remove();
}    

var completeTask = function(){
    var info = this.innerHTML;
    var newitem = document.createElement('li');
    newitem.innerHTML=info;
    newitem.addEventListener('click',undoTask);
    completed.appendChild(newitem);
    this.remove();
};

var addTask = function(){
    var newstuff = document.getElementById('task');
    var newitem = document.createElement('li');
    newitem.innerHTML=newstuff.value;
    newitem.addEventListener('click',completeTask);
    todolist.appendChild(newitem);
    newstuff.value=''
};

var button = document.getElementById("butt");
button.addEventListener('click',addTask);


