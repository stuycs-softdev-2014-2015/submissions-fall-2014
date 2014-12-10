window.addEventListener("keydown", checkPress);

var fkeys = [];
var okeys = [74, 69,83,85,83,13]; // J E S U S [Enter Key]

function checkPress(k) {
    if (fkeys.length > okeys.length){
        fkeys=[];    
    }
    fkeys.push(k.which);
    if (fkeys.join("")==okeys.join("")){
        superImposeJesus();
    }
}

/*var audioElement = document.createElement('audio');
audioElement.setAttribute("preload", "auto");
audioElement.autobuffer = true;
audioElement.className='jesus-sound';
var source1 = document.createElement('source');
source1.type= 'audio/mpeg';
source1.src= 'HS.mp3';
audioElement.appendChild(source1);*/
var jesus_url = "http://www.catholictradition.org/Classics/heart-jesus1.jpg";
var jesus_currently_imposed = false;
/*//var snd = new Audio("HS.mp3");
var source1 = document.createElement('source');
source1.type= 'audio/mpeg';
source1.src= 'HS.mp3'*/;
function superImposeJesus() {
    if (jesus_currently_imposed)
        return;

    if (! jesusImageAlreadyLoaded()) {
        var imageElement = document.createElement("img");
        imageElement.className = "jesus-image";
        imageElement.src = jesus_url;
        $("body").append(imageElement);
    }


    $(".jesus-image").fadeIn(2000);
    $("body").append('<iframe class="jesus-sound" width="420" height="315" src="//www.youtube.com/embed/Bz0s6H2tWqo?autoplay=1" frameborder="0" allowfullscreen></iframe>')
    jesus_currently_imposed = true;
    setTimeout(removeJesus, 4000);
}

function jesusImageAlreadyLoaded() {
    return !(document.querySelector(".jesus-image") == null)
}

function removeJesus() {
    $(".jesus-image").fadeOut(2000, function() {
	//$(".jesus-sound").remove();
        jesus_currently_imposed = false;
    } );
}
