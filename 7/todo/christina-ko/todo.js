var list = document.getElementById("todo");
var newItem = document.getElementById("newItem")
var done = document.getElementById("done")
var addToDo = function(e) {    
    var x = newItem.value;
    if(x != ""){
	var newitem = document.createElement("li");
	newitem.innerHTML = x;
	newitem.addEventListener('click', moveDone)
	list.appendChild(newitem);
	document.getElementById('newItem').value = '';
    }
};
var moveDone = function(e) {
    done.appendChild(this);
    this.addEventListener('click', afterDone)
    
};
var afterDone = function(e){
    console.log(this)
    this.classList.add('red')
};
var keyCallback = function(e){
    if (e.keyCode==13){
	addToDo(e);
	}
};    
var b = document.getElementById('b');
b.addEventListener('click', addToDo);
newItem.addEventListener('keypress', keyCallback);

