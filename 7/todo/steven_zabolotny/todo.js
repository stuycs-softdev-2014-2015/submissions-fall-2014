var counter = 0; // This is necessary to distinguish each added value

var removeItem = function(n) {
    var li = document.getElementById(n);
    li.remove();
};

var addItemDone = function(text) {
    var list = document.getElementById("done");
    var newitem = document.createElement("li");
    newitem.id = counter.toString();
    newitem.innerHTML = text;
    newitem.addEventListener("click", function(e) {
	removeItem(newitem.id);
    } );
    counter++;
    list.appendChild(newitem);
}

var addItemToDo = function(text) {
    var list = document.getElementById("todo");
    var newitem = document.createElement("li");
    newitem.id = counter.toString();
    newitem.innerHTML = text;
    newitem.addEventListener("click", function(e) {
	var text = newitem.innerHTML;
	removeItem(newitem.id);
	addItemDone(text);
    } );
    counter++;
    list.appendChild(newitem);
};

var buttonCallback = function(e) {
    var text = document.getElementById("add").value;
    addItemToDo(text);
    document.getElementById("add").value = "";
}

var b = document.getElementById("submit");
b.addEventListener("click",buttonCallback);
