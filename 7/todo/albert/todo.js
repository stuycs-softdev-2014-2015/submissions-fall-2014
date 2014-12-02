var addItem = function(t,id){
    var list = document.getElementById(id)
    var newItem = document.create("li")
    newItem.innerHTML = t
    list.appendChild(newItem)
}
