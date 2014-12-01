var addItem = function(name,text) {
    var list = document.getElementById(name);
    var newitem = document.createElement("li");
    newitem.innerHTML = text;
    list.appendChild(newitem);
};

var removeItem = function(name,n) {
    var list = document.getElementById(name);
    var listitems = list.children
    listitems[n].remove();
};

var buttonCallback = function(e) {
    var text = document.getElementById("add").value;
    addItem("todo", text);
}

var b = document.getElementById("submit");
b.addEventListener("click",buttonCallback);

var todo = document.getElementById("todo");
var todoitems = todo.children;
for(var i = 0; i < todoitems.length; i++) {
    todoitems[i].addEventListener("click", function(e) {
	var text = todoitems[i].innerHTML;
	removeItem("todo", i);
	addItem("done", text);
    } );
}
