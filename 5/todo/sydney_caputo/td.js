//looked at aidas code
//very confused about this and didnt have a lot of time last night 

var remove = function(e) {
    var finished = document.getElementbyId('completed');
    finished.removeChild(this);

}


var addCompleted = function(e){
    var completedL = document.getElementById('completed');
    //getting the element to then add to the finished pile
    this.addEventListener('click',remove);
//this does it for when you click it 
    completedL.appendChild(this);


}



var addToDo = function(e) {
	var newToDo = document.getElementById("todo").value;
	var toDoList = document.getElementById("lefttodo");
	var listItem = document.createElement("li");
	listItem.innerHTML = newTask;
	listItem.addEventListener('click', addCompleted);
	toDoList.appendChild(listItem);
}


var b = document.getElementById('b');
b.addEventListener('click',addToDo);

var toDoListItems = document.getElementById('lefttodo').children;
