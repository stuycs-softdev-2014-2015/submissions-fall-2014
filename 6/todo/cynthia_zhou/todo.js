console.log("HI");

var addToDo = function(text) {
    var list = document.getElementsById("todo");
    var newitem = document.createElement('li');
    newitem.innerHTML=text;
    list.appendChild(newitem);
};
