console.log("Hi Mike")

var addItem = function(text,d){
    var table = document.getElementsByTagName("tbody")[d]
    var row = table.createElement("tr")
    var item = row.createElement("td")
    item.innerHTML=text;
    
    