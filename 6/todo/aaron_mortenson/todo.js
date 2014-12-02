var input = document.getElementById("item");
var todo = document.getElementById("ToDo");
var done = document.getElementById("Done");


var removeItem = function(num) {
    this.parentNode.removeChild(this);
};

var addItem = function(e) {
    var newitem = document.createElement('li');
    newitem.innerHTML=input.value;
    todo.appendChild(newitem);
    newitem.addEventListener('click',moveItem);
};

var moveItem = function(num) {
    item = this.parentNode.removeChild(this);
    console.log(item);
    done.appendChild(item);
    item.addEventListener('click',removeItem);
};

var button = document.getElementById("b");
button.addEventListener('click',addItem);


var litems = todo.children;
for (var i = 0 ; i < litems.length ; i++ ){
    litems[i].addEventListener('click',moveItem);
}