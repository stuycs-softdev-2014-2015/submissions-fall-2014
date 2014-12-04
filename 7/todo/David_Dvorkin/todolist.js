var jobs = [];
var complete = [];
var newJob = "";

function remove(x){
document.getElementById("CompletedList").innerHTML += newJob.splice(x,1);
}

function addtoComplete(x){
var addJob = document.getElementById(x).innerHTML;
complete.push(addJob);
    for (y = 0; y < complete.length; y++){
	newJob = "<div id="+y+" onClick = remove(" + y + ",'CompletedList');>" + complete[y] + "</div>"
    };
    document.getElementById('CompletedList').innerHTML += newJob;
     if (complete.length == jobs.length && 'chores'.length != 0){
    	 window.alert("Chores done!");
     }
}

function addtolist(){
    var addJob = document.getElementById("addchore").value
    console.log(addJob)
    jobs.push(addJob);
    for (x = 0; x < jobs.length; x++){
	newJob = "<div id="+x+" onClick = addtoComplete(" + x + ");>" + jobs[x] + "</div>"
    };
document.getElementById('chores').innerHTML += newJob;
}
