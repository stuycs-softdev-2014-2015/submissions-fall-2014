var move = function(e) {
        if (this.parentNode.id === "todo")
                done.appendChild(this);
        else if (this.parentNode.id === "done")
                todo.appendChild(this);
}

var items = document.getElementsByTagName("li");
for (var i = 0; i < items.length; i++) {
        items[i].addEventListener('click', move);
}

var addItem = function(id) {
        var textBox = document.getElementById(id);
        var text = textBox.value;
        textBox.value = "";

        if (text === "")
                return;

        var li = document.createElement("li");
        li.appendChild(document.createTextNode(text));
        li.addEventListener('click', move);
        todo.appendChild(li);
}