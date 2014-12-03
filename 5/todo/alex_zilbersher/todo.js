var todo = document.getElementById("todo");
var done = document.getElementById("done");
var button = document.getElementById("input");
button.addEventListener('click',append);

var append = function(e){
    var task = document.createElement('li');
    task.innerHTML=document.getElementById("task").value;
    task.addEventListener('click',completed);
    todo.appendChild(task);
    console.log(task);
}
    
var completed = function(e){
    var task = todo.removeChild(this);
    task.removeEventListener('click',completed);
    done.appendChild(task);
}

