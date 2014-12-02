var buttonCallback = function(){
    var txt = document.getElementById("txt");
    addText(txt.value, "todo");
    txt.value = "";
};
var button = document.getElementById("b");
button.addEventListener('click',buttonCallback);

var todoCallback = function(){
    var item = this;
    this.remove();
    addItem(item, "done");
};
var todoItems = document.getElementById("todo").children;
for (var i = 0; i < todoItems.length; i++){
    todoItems[i].addEventListener('click',todoCallback);
};

var doneCallback = function(){
    this.classList.toggle('red');
};
var doneItems = document.getElementById("done").children;
for (var i = 0; i < doneItems.length; i++){
    doneItems[i].addEventListener('mouseover',doneCallback);
    doneItems[i].addEventListener('click', function(e){
	this.remove();
    });
};

var eventListeners = function(newitem, id) {
    console.log(id);
    if (id=="todo"){
	newitem.addEventListener('click',todoCallback);
    }else if (id=="done"){
	newitem.addEventListener('mouseover',doneCallback);
	newitem.addEventListener('click', function(e){
	    this.remove();
	});
    };
};

var addText = function(text, id) {
    var list = document.getElementById(id);
    var newitem = document.createElement('li');
    eventListeners(newitem, id);
    newitem.innerHTML=text;
    list.appendChild(newitem);
};

var addItem = function(item, id) {
    var list = document.getElementById(id);
    eventListeners(item, id);
    list.appendChild(item);
};

