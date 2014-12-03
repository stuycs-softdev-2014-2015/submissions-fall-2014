var deleteEntirely = function(e){
    var done = document.getElementById("done");
    done.removeChild(this);

}

var moveFromList = function(e) {
    var todo = document.getElementById("todo");
    var done = document.getElementById("done");
    done.appendChild(this);
    this.addEventListener("click",deleteEntirely);
    
}

var addToList = function(e) {
    var todo = document.getElementById("todo");
    var i = document.getElementById("input").value;
    var input  = document.createElement("li");
    input.innerHTML = i;
    todo.appendChild(input);
    input.addEventListener("click",moveFromList);
}


var button = document.getElementById("button");
button.addEventListener("click",addToList);
