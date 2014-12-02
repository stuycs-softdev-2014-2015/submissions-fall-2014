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
    this.removeEventListener("click",moveToDone);
    //when you move something to done, all the alert done event listeners are reentered
//re-adds all alert listeners in done
    for(var j=0;j<doneItems.length;j++){
	doneItems[j].addEventListener('click',alertDone);
    }
}

var alertDone = function(){
    console.log("hi");
    alert(this.innerHTML + " is moved to the bottom of the list");
}

var addmovelistener = function(){
    for(var i=0;i<toDoItems.length;i++){
	toDoItems[i].addEventListener("click",moveToDone);
    }
}

var addItem = function(){
    var inputs = document.getElementById("t");
    var newitem = document.createElement("li");
    newitem.innerHTML = inputs.value;
    toDoList.appendChild(newitem);
    addmovelistener(); //re-adds all move listeners
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
