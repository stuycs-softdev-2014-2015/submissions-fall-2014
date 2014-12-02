var complete = function(e) {
    var in_progress = document.getElementById("in-progress");
    var complete = document.getElementById("completed");
    var completed = in_progress.removeChild(this);
    completed.removeEventListener("click", complete);
    complete.appendChild(completed);
};

var add = function(e) {
    input = document.getElementById("input");
    var text = input.value;
    var item = document.createElement("li");
    item.innerHTML = text;
    item.addEventListener("click", complete);
    document.getElementById("in-progress").appendChild(item);
};


var button = document.getElementById("submit");
button.addEventListener("click", add);
