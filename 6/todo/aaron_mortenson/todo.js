console.log("HELLO");

var x,y;
var i = "hello";
console.log(i);

var removeItem = function(num) {
    this.parentNode.removeChild(this);
};

var addItem = function(text) {
    var list = document.getElementsByTagName('ol')[0];
    var newitem = document.createElement('li');
    newitem.innerHTML=text;
    list.appendChild(newitem);
};

var moveItem = function(num) {
    var source = document.getElementById("ToDo")
    var dest = document.getElementById("Done");
    item = this.parentNode.removeChild(this);
    console.log(item);
    dest.appendChild(item);
    item.addEventListener('click',removeItem);
};

var buttonCallback = function(e){
    console.log(e);
    console.log(this);
};
var button = document.getElementById("b");
button.addEventListener('click',buttonCallback);

var todo = document.getElementById("ToDo");
var litems = todo.children;
for (var i = 0 ; i < litems.length ; i++ ){
    litems[i].addEventListener('click',moveItem);
}