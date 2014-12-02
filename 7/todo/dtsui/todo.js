console.log("Hello");

var doitem = function(e){
  var todo = document.getElementById('todo');
  var done = document.getElementById('done');
  done.appendChild(this);
  this.addEventListener('click', removeitem);
  todo.removeChild(this);
};

var removeitem = function(e){
  var done = document.getElementById('done');
  done.removeChild(this);
}

var additem = function(item){
  var todo = document.getElementById('todo');
  var newitem = document.createElement('li');
  newitem.innerHTML = item;
  todo.appendChild(newitem);
  newitem.addEventListener('click', doitem);
};

var onSubmit = function(e){
  var item = document.getElementById('item').value;
  if(item != ""){
    additem(item);
  };
};

var b = document.getElementById('b');
b.addEventListener('click', onSubmit);
