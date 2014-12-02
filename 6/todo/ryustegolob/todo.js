var todolist = document.getElementById('ToDo');
var donelist = document.getElementById('Done');

var remove = function(){
    donelist.removeChild(this);
};

var done = function(){
    todolist.removeChild(this);
    this.removeEventListener('click',makeDone);
    this.addEventListener('click',remove);
    donelist.appendChild(this);
};

var add = function(){
    var input = document.getElementById('newItem').value;
    var newItem = document.createElement('li');
    newItem.innerHTML = input;
    newItem.addEventListener('click',done);
    todolist.appendChild(newItem);

  
};

var button = document.getElementById("button");
button.addEventListener('click', add);
