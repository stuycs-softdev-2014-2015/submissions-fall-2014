var button = document.getElementById("add_item");
var header = document.getElementsByName("heads");

var wishComeTrue=function(e){
    var wish_list = document.getElementById("wish_list");
    var dreams = document.getElementById("dreams");
    this.classList.add("red");
    this.classList.remove("active");
    dreams.appendChild(this);
};

var addToWishList=function(e){
    console.log("add wish")
    var wish_list = document.getElementById("wish_list");
    var new_wish = document.createElement('li');
    new_wish.classList.add("active");
    new_wish.innerHTML=document.getElementById("item").value;
    new_wish.addEventListener('click',wishComeTrue);
    wish_list.appendChild(new_wish);
};

var turnColor=function(e){
    if (this.style="color:red"){
	this.classList.toggle('green');
    }
    else{
	this.classList.toggle('red');
    }
};

button.addEventListener('click', addToWishList);
header.addEventListener('mouseover', turnColor);

