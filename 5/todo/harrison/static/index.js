//FUNCTION HEADERS:

var doneCallback = function()
{
    console.log("doneCallback called...");
    this.remove();
}

var todoCallback = function()
{
    console.log("todoCallback called...");
    var done = document.getElementById("done");
    var child = document.createElement("li");
    child.innerHTML=this.innerHTML;
    child.addEventListener("click", doneCallback);
    done.appendChild(child);
    this.remove();
}

var buttCallback = function()
{
    console.log("buttCallback called...");
    var todo = document.getElementById("todo");
    var child = document.createElement("li");
    var text = document.getElementById("text");
    child.innerHTML=text.value;
    child.addEventListener("click", todoCallback);
    todo.appendChild(child);
}

var butt = document.getElementById("butt");
butt.addEventListener("click", buttCallback);
