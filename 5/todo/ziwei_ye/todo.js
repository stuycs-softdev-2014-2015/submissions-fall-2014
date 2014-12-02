var addtodo = function(){
    var newli = document.createElement("li");
    newli.innerHTML = document.getElementById("newtask").value;
    document.getElementById("todo").appendChild(newli);
    newli.addEventListener('click', move);
};

var move = function(){
    document.getElementById("done").appendChild(this);
    this.removeEventListener('click', move);
    this.addEventListener('click', remove);
}

var remove = function(){
    this.remove();
}

var submit = document.getElementById("button");
submit.addEventListener('click', addtodo);
