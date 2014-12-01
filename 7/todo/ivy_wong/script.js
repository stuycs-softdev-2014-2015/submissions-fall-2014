var removeTask = function(e){
    var complete = document.getElementById("completed");
    complete.removeChild(this);
};

var completeTask = function(e){
    var inprog = document.getElementById("in-progress");
    var complete = document.getElementById("completed");
    var old = inprog.removeChild(this);
    old.removeEventListener("click",completeTask);
    old.addEventListener("click",removeTask); 
    complete.appendChild(old);
};

var addTask = function(e){
    input = document.getElementById("todo");
    var name = input.value;
    input.value = "";
    if(name != ""){
        var task = document.createElement("li");
        task.innerHTML = name; 
        task.addEventListener("click",completeTask); 
        document.getElementById("in-progress").appendChild(task);
    }
};

var keyCallback = function(e){
    //on ENTER key
    if(e.keyCode == 13){
        addTask(e);
    }
};

var b = document.getElementById("add");
var input = document.getElementById("todo");

b.addEventListener("click", addTask);
input.addEventListener("keypress",keyCallback);
