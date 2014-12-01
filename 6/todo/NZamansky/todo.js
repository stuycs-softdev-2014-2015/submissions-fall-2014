var todolist = document.getElementById('todo');
var todo = todolist.children;
var donelist = document.getElementById('done');
var done = donelist.children;

var removeItem = function(e){
    donelist.removeChild(this);
};

var makeDone = function(e){
    todolist.removeChild(this);
    this.removeEventListener('click',makeDone);
    this.addEventListener('click',removeItem);
    donelist.appendChild(this);
};

var addItem = function(e){
    var input = document.getElementById('newItem').value;
    var newItem = document.createElement('li')
    newItem.innerHTML = input;
    newItem.addEventListener('click',makeDone);
    todolist.appendChild(newItem);
};

var button = document.getElementById("b");
button.addEventListener('click',addItem);
