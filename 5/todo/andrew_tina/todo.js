var toAdd = String(prompt("Anything to add?",""));
var add = document.getElementById("add");

//var dolist = document.getElementById("dolist");
var dolist = document.getElementsByTagName('ol')[0];
var dolistitems = dolist.children;

//var donelist = document.getElementById("donelist");
var donelist = document.getElementsByTagName('ol')[1];
var donelistitems = donelist.children;


var addAgain = function(){
    var addMore = String(prompt("Adding more?",""));
    if (addMore != 'null' && addMore != ''){
	console.log(addMore)
	var newitem = document.createElement('li');
	newitem.innerHTML = addMore;
	newitem.addEventListener('click',doClick);
	dolist.appendChild(newitem);
    }
}

//moving form do list
var doClick = function() {
    this.removeEventListener('click',doClick);
    this.addEventListener('click',doneClick);
    donelist.appendChild(this);
}

//moving from done list
var doneClick = function(text) {
    this.removeEventListener('click',doneClick);
    this.addEventListener('click',doClick);
    dolist.appendChild(this);
}


console.log(toAdd);

if (toAdd != 'null' && toAdd != ''){
    var newitem = document.createElement('li');
    newitem.innerHTML=toAdd;
    newitem.addEventListener('click',doClick);
    dolist.appendChild(newitem);
}

add.addEventListener('click',addAgain);



