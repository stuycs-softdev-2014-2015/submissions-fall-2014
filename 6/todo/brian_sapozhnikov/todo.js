var todolist = document.getElementById("todolist");
var donelist = document.getElementById("donelist");
var button = document.getElementById("add");

var markdone = function(){
    this.removeEventListener("click", markdone);
    donelist.appendChild(this);
}

var addTask = function(){
    var newitem = document.createElement('li');
    newitem.innerHTML=document.getElementById("newentry").value;
    newitem.addEventListener('click',markdone);
    todolist.appendChild(newitem);
    console.log(newitem);
    
};

button.addEventListener('click',addTask);


