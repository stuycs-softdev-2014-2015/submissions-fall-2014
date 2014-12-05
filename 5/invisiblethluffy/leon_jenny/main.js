//mouse tracking
var mouseX, mouseY;
window.addEventListener( 'mousemove',
    function(e) {
        mouseX = e.pageX;
        mouseY = e.pageY;
        changeBackground();
    }
);

var play = true;

//randomize pic location
//pic must be within a div
var w = window.innerWidth;
var h = window.innerHeight;

var pX = Math.random() * w - 150; //- 150 to make sure image doesnt spawn past edge of screen
var pY = Math.random() * h - 125; //- 125 to make sure image doesnt spawn past edge of screen

if ( pX < 60 && pY < 25 ) {
    pX = pX + 70;
    pY = pY + 25;
}
if ( pX > ( w - 150 ) ) {
    pX = pX - 150;
}
if ( pY > ( h - 125 ) ) {
    pY = pY - 125;
}


var image = document.getElementById( "image" );
image.style.marginLeft = pX;
image.style.marginTop = pY;

var audio = new Audio( "03bison.mp3" );
var sound = false;

var square = function( x ) {
    return x * x;
}

var absDist = function( x1, y1, x2, y2 ) {
    return Math.sqrt( square( x1 - x2 ) + square( y1 - y2 ) );
}

var changeBackground = function( e ) {
    if ( play ) {
        var d = absDist( mouseX, mouseY, pX + 75, pY + 62 ); //so we're looking at middle of image
        if ( d >= 510 ) {
            document.body.style.backgroundColor = "white";
        }
        else {
            console.log( "" + pX + " " + pY );
            document.body.style.backgroundColor = 'rgb(' + Math.floor(d/2) + ',' + Math.floor(d/2) + ',' + Math.floor(d/2) + ')';
        }
    }
}

setInterval( function() { if( play ) { sound = true; } }, 5000 );
setInterval( function() { if( sound ) { audio.play(); } }, 3000 );

window.addEventListener( 'click',
    function(e){
        if(absDist( mouseX, mouseY, pX + 75, pY + 62 ) <= 50 ) {
            image.style.visibility = "visible";
            button.style.visibility = "visible";
            play = false;
            sound = false;
        }
    }
);
