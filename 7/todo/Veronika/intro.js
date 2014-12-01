var todoCallback = function(e) {
		console.log(this);
		#this.classList.add('red');
}

var todolist = document.getElementById("todolist");
var todoitems = todolist.children;
for(var i = 0; i < litems.length; i++) {
		litems[i].addEventListener('click',todoCallback);
}
