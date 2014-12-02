var todoCallback = function(e) {
    console.log(this);
    //this.classList.add('red');
}

var todolist = document.getElementById("todolist");
var todoitems = todolist.children;
for(var i = 0; i < todoitems.length; i++) {
    todoitems[i].addEventListener('click',todoCallback);
}


var doneCallback = function(e) {
    console.log(this);
    //this.classList.add('red');
}

var donelist = document.getElementById("donelist");
var doneitems = donelist.children;
for(var i = 0; i < doneitems.length; i++) {
    doneitems[i].addEventListener('click',doneCallback);
}
