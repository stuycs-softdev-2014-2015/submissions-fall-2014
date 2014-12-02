var item = document.getElementById('item')
var button = document.getElementById('add')
var list = document.getElementById('list')

var add = function() {
    if (item.value=='') { return }
    var newitem = document.createElement('li');
    newitem.innerHTML = item.value;
    list.appendChild(newitem);
}

button.addEventListener("click", add)
