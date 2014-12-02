//to do list id: todo
//done list id: done
//text field id: comment
//button id: b

<<<<<<< HEAD
var buttonCallback = function(e){
    console.log(e);
    console.log(this);
}
=======
var funct = function(e){
    for (var i = 0; i<titems.length; i++){
	titems[i].addEventListener('click',  addItem );
    }
};
>>>>>>> fc5c02c53466b88ede01395d5e20aa7b1c37c1cb

var button = document.getElementById("b");
button.addEventListener('click',buttonCallback);

var toDoList = document.getElementById("todo");
var toDoItems = toDoList.children;

<<<<<<< HEAD
var doneList = document.getElementById("done");
var doneItems = doneList.children;

var addItem = function(text){
    var todo = document.getElementById("todo");
    var input = document.getElementById('comment').value
    var newtodo = document.createElement("li");
    newtodo.innerHTML=input;
    todo.appendChild(newtodo);
    console.log("yups");
};    

var moveToDone = function(e){
    console.log(this);
    doneList.appendChild(this);
    console.log(doneItems.children);
    this.parentNode.removeChild(this);
}

for(var i=0;i<toDoItems.length;i++){
    toDoItems[i].addEventListener('click',moveToDone);
    toDoItems[i].addEventListener('mouseover',function(e){
	this.classList.toggle("b");
    });
    toDoItems[i].addEventListener('mouseout',function(e){
	this.classList.toggle("b");
    });
}

=======
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
>>>>>>> fc5c02c53466b88ede01395d5e20aa7b1c37c1cb



//button functionality
var bb = document.getElementById("b");
bb.addEventListener("click",addItem);       
//enter functionality
var inputbox = document.getElementById("t");
inputbox.addEventListener("keyup",enterItem);
