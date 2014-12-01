var ToDoList = document.getElementById("todo");
var titems = ToDoList.children;

var funct = function(e){
    for (var i = 0; i<titems.length; i++){
	titems[i].addEventListener('click',   );
    }
};




var addItem = function(){
    var todo = document.getElementById("todo");
    var newtodo = document.getElementById("t");

    var newitem = document.createElement("li");
    newitem.innerHTML = newtodo;
    list.appendChild(newitem);  
    console.log("yups");
};
var bb = document.getElementbyId("b");
bb.addEventListener('click',addItem);       



