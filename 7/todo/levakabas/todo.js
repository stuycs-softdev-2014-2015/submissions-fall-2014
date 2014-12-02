var removeItem = function (e) {
    var done = document.getElementById('done');
    done.removeChild(this);
};

var moveItem = function(e) {
    var done = document.getElementById('done');
    this.addEventListener('click', removeItem);
    done.appendChild(this);
    
};

var addItem = function(text) {
    var list = document.getElementById('todo');
    var item = document.createElement('li');
    item.innerHTML = text;
    list.appendChild(item);
    item.addEventListener('click', moveItem);
};


var buttonCallback = function(e) {
    var input = document.getElementById('input').value;
    if (input != ""){
	addItem(input);
    };
};

var keyCallback = function(e){
    var input = document.getElementById('input').value;
    if (e.keyCode == 13 && input != ""){
        addItem(input);
    };
};

var clearCallback = function(e){
    var done = document.getElementById('done');
    var litems = done.children;
    for(var i = litems.length - 1; i >= 0; i--) {
	done.removeChild(litems[i]);
    }
};


var submit = document.getElementById('submit');
var input = document.getElementById('input');
var clear = document.getElementById('clear');
submit.addEventListener('click', buttonCallback);
input.addEventListener('keypress', keyCallback);
clear.addEventListener('click', clearCallback);