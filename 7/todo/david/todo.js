var todo = document.getElementById('todo');
var done = document.getElementById('done');
var button = document.getElementById("b");

var remove = function(e){
    done.removeChild(this);
}

var doneStuff = function(e){
    todo.removeChild(this);
    this.removeEventListener('click', doneStuff);
    this.addEventListener('click',remove);
    this.removeEventListener('mouseout', turn_purple);
    this.addEventListener('mouseout', turn_green);
    done.appendChild(this);
}

var addStuffToDo = function(e){
    var input = document.getElementById('stuff').value;
    var stuff = document.createElement('li')
    stuff.innerHTML = input;
    stuff.addEventListener('click', doneStuff);
    stuff.addEventListener('mouseout', turn_purple);
    todo.appendChild(stuff);
}


var turn_green = function(e){
    this.classList.toggle('green');
}

var turn_purple = function(e){
    this.classList.toggle('purple');
}

button.addEventListener('click', addStuffToDo);
