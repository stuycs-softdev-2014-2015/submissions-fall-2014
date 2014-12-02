var todo = document.getElementById("todo");
var done = document.getElementById("done");


var addToList = function(e) {
    var i = document.getElementById("input");
    var input  = document.createElement("li");
    input.innerHTML = i;
    input.addEventListener("click",moveFromList);
    todo.appendChild(input);
}
var moveFromList = function(e) {
    done.appendChild(this);
    todo.remove(this);
    this.addEventListener("click",addToList);
    this.addEventListener("dbclick",deleteEntirely);
}
var deleteEntirely = function(e){
    done.remove(this);
}

var button = document.getElementById("button");
button.addEventListener("click",addToList);
