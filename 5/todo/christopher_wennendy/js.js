var todo = document.getElementById("do");
var not = document.getElementById("not");

var add = function(e){
    var item = document.createElement('li');
    item.innerHTML=document.getElementById("item").value;
    item.addEventListener('click',done);
    todo.appendChild(item);
    console.log(item);
}
    
var done = function(e){
    var item = todo.removeChild(this);
    item.removeEventListener('click',done);
    not.appendChild(item);
}

var button = document.getElementById("b");
button.addEventListener('click',add);
