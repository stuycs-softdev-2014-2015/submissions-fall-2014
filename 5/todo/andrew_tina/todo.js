var toAdd = String(prompt("Anything to add?",""));
var add = document.getElementById("add");
var temptext = ''

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
	//var list = document.getElementsByTagName('ol')[0];
	var newitem = document.createElement('li');
	newitem.innerHTML = addMore;
	//list.appendChild(newitem);
	dolist.appendChild(newitem);
    }
}

//moving form do list
var doClick = function() {
    var list = document.getElementsByTagName('ol')[1];
    var newitem = document.createElement('li');
    newitem.innerHTML= temptext;
    //list.appendChild(newitem);
    console.log(temptext);
    console.log(newitem);
    console.log(newitem.innerHTML);
    list.appendChild(newitem);
    var list = document.getElementsByTagName('ol')[0];	
    list.removeChild(this);
}

var doClick2 = function(num){
    var list = document.getElementsByTagName('ol')[0];
    console.log(list);

    //list[num].remove();
    
}

//moving from done list
var doneClick = function(text) {
    var list = document.getElementsByTagName('ol')[0];
    var newitem = document.createElement('li');
    newitem.innerHTML=text;
    list.appendChild(newitem);
}

var doneClick2 = function(num){
    var list = document.getElementsByTagName('ol')[1];
    list[num].remove();
}

console.log(toAdd);

if (toAdd != 'null' && toAdd != ''){
    //console.log('check')
    var list = document.getElementsByTagName('ol')[0];
    var newitem = document.createElement('li');
    newitem.innerHTML=toAdd;
    list.appendChild(newitem);
}


if (typeof dolistitems != "undefined"){
    for (var i = 0; i < dolistitems.length; i++){
	console.log(dolistitems[i]);
	temptext = dolistitems[i];
	dolistitems[i].addEventListener('click',doClick); 
	//dolistitems[i].addEventListener('click',doClick2);
    }
}

if (typeof donelistitems != "undefined"){
    for (var i = 0; i < donelistitems.length; i++){
	donelistitems[i].addEventListener('click',doneClick);
//	donelistitems[i].addEventListener('click',doneClick2);
    }
}

add.addEventListener('click',addAgain);



