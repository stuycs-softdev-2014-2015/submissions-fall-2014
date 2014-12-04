var addItem = function(text, list){
    var list = document.getElementById(list);
    var newitem = document.createElement("li");
    newitem.innerHTML = text;

    if(list == "done"){
	newitem.removeEventListener("click", moveDone);
	newitem.addEventListener("click", moveNotDone);
    }
    else{
	newitem.removeEventListener("click", moveNotDone);
	newitem.addEventListener("click", moveDone);
    }
    list.appendChild(newitem);
};

var removeItem = function() {
    console.log(this);
    this.remove();
};

var moveDone = function(){
    var item = this;
    this.remove();
    console.log(this);
    addItem(this.innerHTML, "done");
}

var moveNotDone = function(){
    var item = this;
    this.remove();
    addItem(item.innerHTML, "todo");
}

var buttonCallBack = function(){
    console.log(enqueue.value);
    addItem(enqueue.value, "todo");
}


var todo = document.getElementById("todo");
var litems = todo.children;
//console.log(list);
for(var i = 0; i < litems.length; i++){
    litems[i].addEventListener("click", moveDone);
}

var done = document.getElementById("done");
litems = done.children;
for(var i = 0; i < litems.length; i++){
    litems[i].addEventListener("click", moveNotDone);
}
var button = document.getElementById("button");
button.addEventListener("click", buttonCallBack);
var enqueue = document.getElementById("enqueue");
