var todo = document.getElementById('todo');
var done = document.getElementById('done');

var removeItem = function(e){
    done.removeChild(this);
};

var makeDone = function(e){
    todo.removeChild(this);
    this.removeEventListener('click',makeDone);
    this.addEventListener('click',removeItem);
    done.appendChild(this);
};

var addItem = function(e){
    var input = document.getElementById('newItem').value;
    var newItem = document.createElement('li')
    newItem.innerHTML = input;
    newItem.addEventListener('click',makeDone);
    todo.appendChild(newItem);
};

var button = document.getElementById("b");
button.addEventListener('click',addItem);
