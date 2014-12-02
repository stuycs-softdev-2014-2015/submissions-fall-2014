var removing = function(e){
    var dd = document.getElementById("dd");
    dd.removeChild(this);
}
//prob should have factored those funcs
var makeCheck = function(e){
    var td = document.getElementById("td");
    var doNow = td.children;
    doNow[doNow.length-1].addEventListener("click",function(){
	var newTask = document.createElement("li");
	//console.log(this);
	newTask.innerHTML = this.innerHTML;
	var dd = document.getElementById("dd");
	dd.appendChild(newTask);
	dd.children[dd.children.length-1].addEventListener("click",removing);
	dd.children[dd.children.length-1].addEventListener("mouseover",function(e){
	    this.classList.toggle('red')
	});

	dd.children[dd.children.length-1].addEventListener("mouseout",function(e){
	    this.classList.toggle('black')
	});
	var td = document.getElementById("td");
	td.removeChild(this);
    });
    doNow[doNow.length-1].addEventListener("mouseover",function(e){
	this.classList.toggle('green');
    });
    doNow[doNow.length-1].addEventListener("mouseout",function(e){
	this.classList.toggle('black');
    });
}
var clear = function(e){
    document.getElementById("Text").value="";
}
var adding = function(e){
    var td = document.getElementById("td");
    var text = document.getElementById("Text");
    var newTask=document.createElement("li");
    var newText=text.value;
    newTask.innerHTML = newText;
    td.appendChild(newTask);
    clear();
    makeCheck();
}
var b = document.getElementById('Button');
b.addEventListener('click',adding);