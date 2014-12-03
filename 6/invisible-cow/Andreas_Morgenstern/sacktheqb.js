
var qb = document.getElementById("QB");
qb.addEventListener("click", function() {
    sacked(qb);});
function sacked(e){
    window.alert("REKT THE " + e.id);
    e.style.left = "" + Math.random() * window.innerWidth + "px";
    e.style.top = "" + Math.random() * window.innerHeight + "px";
};
