var todo = document.getElementById("list");
var done = document.getElementById("dlist");

var todone = function(e){
    todo[e].remove();
    done.appendChild(e);
}
var totodo = function(e){
    done[e].remove();
    todo.appendChild(e);
}
for(var i=0;i <todo.length; i++){
    todo[i].addEventListener('click',todone);
}
for(var i=0;i <done.length;i++){
    done[i].addEventListener('click',totodo);
}
