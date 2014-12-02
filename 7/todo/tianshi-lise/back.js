//to do list id: todo
//done list id: done
//text field id: comment
//button id: b

var toDoList = document.getElementById("todo");
var toDoItems = toDoList.children;

var doneList = document.getElementById("done");
var doneItems = doneList.children;

var moveToDone = function(){
    doneList.appendChild(this);
}
var addmovelistener = function(){
    for(var i=0;i<toDoItems.length;i++){
	toDoItems[i].addEventListener('click',moveToDone);
/*	toDoItems[i].addEventListener('mouseover',function(e){
	    this.classList.toggle("big");
	});
	toDoItems[i].addEventListener('mouseout',function(e){
	    this.classList.toggle("big");
	});
*/
    }
}

var addItem = function(){
    var inputs = document.getElementById("t");
    var newitem = document.createElement("li");
    console.log(inputs.value);
    newitem.innerHTML = inputs.value;
    toDoList.appendChild(newitem);
    addmovelistener(); //readds all move listeners
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

addmovelistener(); //adds beginning move listener