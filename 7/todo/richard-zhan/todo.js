console.log("HI");


var td = document.getElementById("td");
var text = document.getElementById("Text");
//var tasks = td.children;

var adding = function(x){
    //console.log(x);
    var newTask=document.createElement("li");
    var newText=text.value;
    console.log(newText);
    newTask.innerHTML = newText;
    td.appendChild(newTask);
}
var b = document.getElementById('Button');
b.addEventListener('click',adding);
