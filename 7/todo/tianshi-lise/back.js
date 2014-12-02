var ToDoList = document.getElementById("todo");
var titems = ToDoList.children;

var funct = function(e){
    for (var i = 0; i<titems.length; i++){
	titems[i].addEventListener('click',  addItem );
    }
};



var addItem = function(){
    var list = document.getElementById("todo");
    var inputs = document.getElementById("t");
    var newitem = document.createElement("li");
    console.log(inputs.value);
    newitem.innerHTML = inputs.value;
    list.appendChild(newitem);
};
var enterItem = function(e){
    var x = event.which || event.keyCode; //differs from which and keyCode depending on browswer
    if (x == 13){
	addItem();
    }
};



//button functionality
var bb = document.getElementById("b");
bb.addEventListener("click",addItem);       
//enter functionality
var inputbox = document.getElementById("t");
inputbox.addEventListener("keyup",enterItem);
