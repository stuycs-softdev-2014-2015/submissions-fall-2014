//CTRL-SHIFT-J TO OPEN CONSOLE (in chrome, on linux)

var move_element = function(text){
    var done_list = document.getElementById("done");
    this.removeEventListener("click", move_element);
    done_list.appendChild(this);
    this.addEventListener("click", delete_element);
}

var add_element = function(text){
    text.preventDefault();//prevents autorefresh
    var todo_list = document.getElementById("todo");
    var input = document.getElementById("textbx").value;
    var newitem = document.createElement("li");
    //console.log(input);
    newitem.innerHTML = input;
    todo_list.appendChild(newitem);
    newitem.addEventListener("click", move_element);
    document.getElementById("textbx").value = "";
    
}

var delete_element = function(text){
    var done_list = document.getElementById("done");
    this.removeEventListener("click", move_element);
    done_list.removeChild(this);
}

var button = document.getElementById("sub");
//console.log(button);
button.addEventListener("click", add_element);

