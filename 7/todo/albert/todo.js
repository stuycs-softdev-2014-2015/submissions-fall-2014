var removeItem = function(text){
	t = text.innerHTML;
	var items = document.getElementsByTagName('li');
	for (var i = 0;i<items.length;i++){
		if (items[i].innerHTML==text){
			items[i].remove();
		}
	}
	return t;
}

var addItem = function(text,id){
    var list = document.getElementById(id);
    var newItem = document.createElement("li");
    newItem.innerHTML = text;
    if (id=="todo"){
	    newItem.addEventListener('click',function(e){
	    	removeItem(text);
	    	addItem(text,"done");
	    });
	} else {
		newItem.addEventListener('click',function(e){
			removeItem(text);
		});
	}
    list.appendChild(newItem);
}

var doStuff = function(form){
	addItem(form.inputtext.value,"todo");
}

var form = document.getElementById("form")
var button = document.getElementById("submitbutton");
button.addEventListener('click',function(e){
	doStuff(form);
});
