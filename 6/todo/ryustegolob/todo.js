var todolist = document.getElementById('ToDo');
var donelist = document.getElementById('Done');

var removeItem = function(){
    donelist.removeChild(this);
};

var makeDone = function(){
    todolist.removeChild(this);
    this.removeEventListener('click',makeDone);
    this.addEventListener('click',removeItem);
    donelist.appendChild(this);
};

var addItem = function(){
    var input = document.getElementById('newItem').value;
    var newItem = document.createElement('li')
    newItem.innerHTML = input;
    todolist.appendChild(newItem);
    newItem.addEventListener('click',makeDone);
  
};

var button = document.getElementById("button");
button.addEventListener('click',addItem);
