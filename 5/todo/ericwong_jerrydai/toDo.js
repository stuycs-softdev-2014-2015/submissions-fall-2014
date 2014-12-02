var button = document.getElementById("b");
var input = document.getElementById("input");
var todo = document.getElementById("yes");
var complete = document.getElementById("no");

var addItem = function() {
    var list = document.getElementsByTagName('ol')[0];
    var newitem = document.createElement('li');
    newitem.innerHTML = input.value;
    newitem.addEventListener("click", completed);
    list.appendChild(newitem);
}

var completed = function() {
    this.parentNode.removeChild(this);
    complete.appendChild(this);
    this.removeEventListener("click", completed);
    this.addEventListener("click", do_this);
}

var do_this = function() {
    this.parentNode.removeChild(this);
    todo.appendChild(this);
    this.removeEventListener("click", do_this);
    this.addEventListener("click", completed);
}

button.addEventListener("click", addItem);

