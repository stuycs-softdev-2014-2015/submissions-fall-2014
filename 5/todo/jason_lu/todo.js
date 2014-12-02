var removeItem = function(num){
		var list = document.getElementsByTagName('li');
		list[num].remove();

}

var addItem = function(text) {
		var list = document.getElementsByTagName('ol')[0];
		var newitem = document.createElement('li');
		newitem.innerHTML=text;
		list.appendChild(newitem);
}

for (var i = 0; i < litems.length; i++){
		litems[i].addEventListener('click',liCallback);
}

b.addEventListener('click',buttonCallback);
