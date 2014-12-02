var button = document.getElementById("add_item");
var header = document.getElementsByClassName("red");

var turnRed=function(e){
    this.classList.toggle('red');
};

var wishes = [];

var moveBack=function(e){
    var wish_list = document.getElementById("wish_list");
    var dreams = document.getElementById("dreams");
    this.classList.remove("active");
    wish_list.appendChild(this);
} // This doesn't quite work

var wishComeTrue=function(e){
    var wish_list = document.getElementById("wish_list");
    var dreams = document.getElementById("dreams");
    this.classList.remove("active");
    stripe;
    dreams.appendChild(this);
};

var addToWishList=function(e){
    console.log("add wish")
    var wish_list = document.getElementById("wish_list");
    var new_wish = document.createElement('li');
    if(wishes.length%2==0){
	new_wish.classList.add("green");
    }
    else{
	new_wish.classList.add("red");
    }
    wishes.push(new_wish);
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
// header.addEventListener('mouseover', turnColor);

for (var i = 0 ; i < header.length ; i++ ){
    header[i].addEventListener('mouseover', turnColor);
}
