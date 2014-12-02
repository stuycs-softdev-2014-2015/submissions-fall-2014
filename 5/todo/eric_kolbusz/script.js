var todo = document.getElementById("todo_list");
var done = document.getElementById("done_list");
var input = document.getElementById("item");

var add_todo = function(e) {
    var todo_item = document.createElement('li');
    todo_item.innerHTML = input.value;
    todo_item.addEventListener('click',move_to_done);
    todo_item.addEventListener('mouseover', turn_green);
    todo_item.addEventListener('mouseout', turn_black);
    todo_list.appendChild(todo_item);
}

var move_to_done = function(e) {
    var done_item = todo_list.removeChild(this);
    //done_item.removeEventListener('',move_to_done);
    done_item.addEventListener('click',remove);
    done_item.addEventListener('mouseout', turn_black);
    done_list.appendChild(done_item);
}

var remove = function(e) {
    this.parentNode.removeChild(this);
}

var turn_green = function(e) {
    this.classList.toggle('green');
}
var turn_black = function(e) {
    this.classList.toggle('black');
}

b.addEventListener('click',add_todo);
