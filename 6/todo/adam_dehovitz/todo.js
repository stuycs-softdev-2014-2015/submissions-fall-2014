var removeItem = function(e){
    var list = document.getElementsByTagName('ol')[0];
    var todo = document.getElementsByTagName('ol')[1];
    this.remove();
    this.removeEventListener('click',removeItem)
    this.removeEventListener('mouseover',function(e){
	this.classList.toggle('red');
    });
    this.addEventListener('mousover',function(e){
	this.classList.toggle('green');
    });
    todo.appendChild(this)
    

};

var addItem = function(e) {
    var list = document.getElementsByTagName('ol')[0];
    var newitem = document.createElement('li');
    newitem.innerHTML= document.getElementById("new item").value
    newitem.addEventListener('click',removeItem)
    newitem.addEventListener('mouseover',function(e){
				this.classList.toggle('red');
		});
    list.appendChild(newitem);
};
var button =document.getElementById("b");
button.addEventListener('click',addItem);