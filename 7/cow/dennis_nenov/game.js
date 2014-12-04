var height = window.innerHeight * .89- (window.innerHeight*.89 * Math.random());
var width = window.innerWidth *.89 - (window.innerWidth*.89 * Math.random());

function resetGame()
{
    var chicken = document.getElementById("chicken");
    chicken.style.top = height + "px";
    chicken.style.left= width + "px";
    play();
}

window.onload = resetGame();

var verylow = document.getElementById("verylow")
var low = document.getElementById("low")
var med = document.getElementById("med")
var high = document.getElementById("high")

var xcormouse;
var ycormouse;

window.addEventListener('mousemove',function(e)
{
    xcormouse = e.pageX;
    ycormouse = e.pageY;
});


function get_distance()
{
    return Math.sqrt(Math.pow(xcormouse-(width+40),2) + Math.pow(ycormouse-(height+40),2));
};

function playMusic()
{
    var dist = get_distance();
    console.log(dist);
    if (dist < 40)
    {
	   high.play();
    }
    else if (dist < 100)
    {
	   med.play();
    }
    else if (dist < 200)
    {
       low.play();
    }
    else
    {
	   verylow.play();
    }
}

function play()
{
    setInterval("playMusic()",1400);
}