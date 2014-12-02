var todo = document.getElementById("todo");
var done = document.getElementById("done");

var fun_add = fun_add(list, text)
{
    var child = document.createElement('li');
    child.innerHTML = text;
    list.appendChild(child);
}


