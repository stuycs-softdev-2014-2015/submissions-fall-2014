var myFunction = function() {
    var x = document.getElementById("new");
    var str = "" +  x.elements[0].value
    var list = document.getElementsByTagName('ol')[0];
    var newitem = document.createElement('li');
    newitem.innerHTML=str;
    list.appendChild(newitem);
  
}
