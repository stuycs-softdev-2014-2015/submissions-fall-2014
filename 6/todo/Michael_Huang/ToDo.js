

var addItem = function(text,ID){
    var list= document.getElementsByTagName("ol")[ID];
    var newitem=document.createElement('li');
    newitem.innerHTML=text;
    list.appendChild(newitem);
    
    };


    
	  
var removeItem = function(num){
    
    var list = document.getElementsByTagName('li');
    
    list[num].remove();

};
var hover = function(e){
    this.classList.toggle('green');
    };
var change= function(num){
    addItem(document.getElementById("dolist").children[num].innerHTML,1)
    removeItem(num)
    }
var setup = function(){
     thelist = document.getElementById("dolist");

    
    for ( i = 0 ; i < thelist.children.length ; i++ ){
	var x = i;
	thelist.children[x].addEventListener('click',function(){change(x);setup()});
	console.log(document.getElementById("dolist").children[i].innerHTML);
	thelist.children[i].addEventListener('mouseover',hover);
	x =0;
    };
    for (var d =0;d <document.getElementById("donelist").children.length;d++){
	var xz = d;
	var xy = thelist.children.length
	document.getElementById("donelist").children[d].addEventListener('click',function(){removeItem(xz+xy);setup()})};
        xz =0;
}
setup();
