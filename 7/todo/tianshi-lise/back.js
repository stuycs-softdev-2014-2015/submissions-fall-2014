var ToDoList = document.getElementById("todo");
var titems = ToDoList.children;

var funct = function(e){
    for (var i = 0; i<titems.length; i++){
	titems[i].addEventListener('click',  addItem );
    }
};


var bb = document.getElementById("b");

var addItem = function(){
    console.log("yups");
    var list = document.getElementById("todo");
    var inputs = document.getElementById("t");
    var newitem = document.createElement("li");
    console.log(inputs.value);
    newitem.innerHTML = inputs.value;
    list.appendChild(newitem);  
};

bb.addEventListener('click',addItem);       


var add = function(text){
    var list = document.getElementById("todo");
    var newitem = document.createElement("li");
    newitem.innerHTML = text;
    list.appendChild(newitem);
};

