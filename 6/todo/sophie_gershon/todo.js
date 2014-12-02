
var todo = document.getElementById("todo");
var titems = todo.children;
var done = document.getElementById("done");

var removeitem = function(){
    this.remove();
}

var green = function(){
    this.classList.toggle('green');
    this.removeEventListener('click', green);
    this.addEventListener('click', removeitem);
}

var move = function(){
    done.appendChild(this);
    this.removeEventListener('click',move);
    this.addEventListener('click',green);
}

for (var i = 0; i < titems.length; i++){
    titems[i].addEventListener('click', move)
}


var addItem = function(){
    var newli = document.createElement("li");
    newli.innerHTML = document.getElementById("newtodo").value;
    document.getElementById("newtodo").value = "";
    newli.addEventListener('click', move);
    todo.appendChild(newli);
}

var tester = function(){
    console.log(document.getElementById("newtodo").value);
}

var button = document.getElementById("submit");

button.addEventListener('click', addItem);
button.addEventListener('click', tester);
