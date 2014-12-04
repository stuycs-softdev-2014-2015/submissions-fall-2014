var thluffyX = 50+Math.floor(Math.random()*(window.innerWidth-100));
var thluffyY = 50+Math.floor(Math.random()*(window.innerHeight-100));
var pos = document.querySelector(".pos");
pos.style.left = (thluffyX-50)+"px";
pos.style.top = (thluffyY-50)+"px";

var C4 = document.getElementById("C4");

var notes = ['C3','C#3','D3','D#3','E3','F3','F#3','G3','G#3','A3','A#3','B3','C4','C#4','D4','D#4','E4','F4','F#4','G4','G#4','A4','A#4','B4','C5']
var tones = []
for(i=0; i<25; i++){
    tones[i]=document.getElementById(notes[i]);
}

mozart = [tones[0],tones[7],tones[12],tones[16],tones[19],tones[24]];
stravinsky = [tones[0],tones[4],tones[7],tones[3],tones[6],tones[11]];
wagner = [tones[0],tones[0],tones[6],tones[6],tones[10],tones[15]];
bach = [tones[0],tones[0],tones[7],tones[7],tones[14],tones[21]];
glass = [tones[0],tones[0],tones[0],tones[0],tones[0],tones[0]];
composers = [mozart,stravinsky,wagner,bach,glass];
names = ['mozart','stravinsky','wagner','bach','glass'];
index = Math.floor(Math.random()*composers.length);
composer = composers[index];
compName = names[index];

var distance=100000;
var image = '<center><img id="thluffy" class="thluffy" imageMode="center" src="composers/'+compName+'.jpg"><h3>You found the invisible '+compName.toUpperCase()+'!</h3></center>';
var div = document.getElementById('div');

window.addEventListener('mousemove',function(e){
    var text = document.getElementById('dist');
    var dist = ((thluffyX-e.pageX)*(thluffyX-e.pageX))+((thluffyY-e.pageY)*(thluffyY-e.pageY));
    text.innerHTML = dist;
    distance = dist;
});

window.addEventListener('click',function(e){
    if(distance<1000){
	window.clearInterval(interval);
	div.innerHTML=image;
    }
});



var makeTone = function(tone){
    tone.play();
    setTimeout(function(){
	tone.currentTime=0;
	tone.pause();
    },1000);
};

var makeNoise = function(){
    if (distance<1000){
	makeTone(composer[5]);
    }if (distance<3000){
	makeTone(composer[4]);
    }if (distance<9000){
	makeTone(composer[3]);
    }if (distance<27000){
	makeTone(composer[2]);
    }if (distance<81000){
	makeTone(composer[1]);
    }
    makeTone(mozart[0]);
};

interval=window.setInterval(makeNoise,500);

