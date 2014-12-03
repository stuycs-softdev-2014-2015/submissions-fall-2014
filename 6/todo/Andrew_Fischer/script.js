var todolist = document.getElementById('todo');
var todo = todolist.children;

var donelist = document.getElementById('completed');
var done = donelist.children;

var removeItem = function(e){
    donelist.removeChild(this);
};

var markComplete = function(e){
    todolist.removeChild(this);
    this.removeEventListener('click',markComplete);
    this.addEventListener('click',removeItem);
    donelist.appendChild(this);
};

var add = function(e){
    var input = document.getElementById('addme').value;
    var newItem = document.createElement('li')
    newItem.innerHTML = input;
    newItem.addEventListener('click',markComplete);
    todolist.appendChild(newItem);
};

var button = document.getElementById("submit");
button.addEventListener('click',add);
