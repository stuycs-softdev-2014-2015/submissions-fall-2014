var item = document.getElementById("item");
var add = document.getElementById("add");
var todo = document.getElementById("todo");
var done = document.getElementById("done");


var reItem = function() {
    console.log(this);
    todo.removeChild(this);
    done.appendChild(this);
    //this.removeEventListener("click", reItem);
};

var addItem = function() {
    var newItem = document.createElement("li");
    newItem.innerHTML = item.value;
    console.log(item.value);
    newItem.addEventListener("click", reItem);
    todo.appendChild(newItem);
};

add.addEventListener("click", addItem);
