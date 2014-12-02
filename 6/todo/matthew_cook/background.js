var done = function() {
    var source = document.getElementById("todo")
    var dest = document.getElementById("done");
    newI = this.parentNode.removeChild(this);
    console.log(newI);
    dest.appendChild(newI);
    var litems = dest.children;
    for (var i = 0 ; i < litems.length ; i++ ){
	litems[i].addEventListener('click',trash);

    }

}

var trash = function() {
    newI = this.parentNode.removeChild(this);
}

var buttonCallback = function(e){
    var dest = document.getElementById("todo")
    var newitem = document.createElement('li');
    newitem.innerHTML=document.getElementById("toadd").value;
    newitem.addEventListener('click',done);
    dest.appendChild(newitem);
    
};
var button = document.getElementById("b");
button.addEventListener('click',buttonCallback);

var thelist = document.getElementById("todo");
var litems = thelist.children;
for (var i = 0 ; i < litems.length ; i++ ){
		litems[i].addEventListener('click',done);

}
