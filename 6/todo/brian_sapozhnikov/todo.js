var todolist = document.getElementById("todolist");
var donelist = document.getElementById("donelist");
var button = document.getElementById("add");

var deleteitem = function(){
    donelist.removeChild(this);
};

var markdone = function(){
    this.removeEventListener("click", markdone);
    this.addEventListener("click",deleteitem);
    donelist.appendChild(this);
};

var addTask = function(){
    var newitem = document.createElement('li');
    newitem.innerHTML=document.getElementById("newentry").value;
    newitem.addEventListener('click',markdone);
    todolist.appendChild(newitem);
    document.getElementById("newentry").value='';
    document.getElementById("newentry").focus();
};

button.addEventListener('click',addTask);



