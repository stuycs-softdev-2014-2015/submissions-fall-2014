var todolist = document.getElementById('toDo');
var todo = todolist.children;
var donelist = document.getElementById('done');
var done = donelist.children;


var myFunction = function() {
    var list = document.getElementsByTagName('ol')[0];
    var x = document.getElementById("new");
    var str = "" +  x.elements[0].value;
    var newitem = document.createElement('li');
    newitem.innerHTML = str;
    newitem.addEventListener('click',DoneItem);
    newitem.classList.toggle('red');
    list.appendChild(newitem);
};

var DoneItem = function(e){
    todolist.removeChild(this);
    this.removeEventListener('click', DoneItem);
    this.classList.toggle('green');
    donelist.appendChild(this);
    
};
