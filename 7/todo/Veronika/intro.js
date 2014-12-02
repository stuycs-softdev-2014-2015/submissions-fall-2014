var todolist = document.getElementById("todolist");

var buttonCallback = function(e){
    var text = document.getElementById("newItem").value;
    var newitem = document.createElement("li");
    newitem.classList.add("active");
    newitem.innerHTML = "<input type='checkbox''> "+text;
    newitem.addEventListener('click',remove)
    todolist.appendChild(newitem);
}
button.addEventListener('click',buttonCallback);

var remove = function(e){
    var done = document.getElementById("donelist");
    this.classList.add("grey");
    this.classList.remove("active");
    this.children[0].disabled=true;
    this.children[0].checked=true;
    this.addEventListener('click',add)
    done.appendChild(this);
}

var add = function(e){
    this.classList.add("active");
    this.classList.remove("grey");
    this.children[0].disabled=false;
    this.children[0].checked=false;
    this.addEventListener('click',remove)
    todolist.appendChild(this);
}

