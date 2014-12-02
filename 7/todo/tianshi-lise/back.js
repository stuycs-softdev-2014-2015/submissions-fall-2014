//to do list id: todo
//done list id: done
//text field id: comment
//button id: b

var buttonCallback = function(e){
    console.log(e);
    console.log(this);
}

var button = document.getElementById("b");
button.addEventListener('click',buttonCallback);

var toDoList = document.getElementById("todo");
var toDoItems = toDoList.children;

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




