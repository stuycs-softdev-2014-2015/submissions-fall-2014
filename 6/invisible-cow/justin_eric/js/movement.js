
/*
 * how angle is defined
 *
 * North - 0 Degrees
 * East - 90 Degrees
 * South - 180 Degrees
 * West - 270 Degrees
 */

/*
 * input: angle - Number
 * returns: random angle based on the possible trajectory the object can take
 * returns -1 if the angle is larger than 360 degrees
 *
 * call this when the object hits the wall (the edge of browser)
 */
var generateAngleWall = function(angle) {
    if (angle < 90) {
        return 270 + Math.random() * 90;
    } else if (angle < 180) {
        return 180 + Math.random() * 90;
    } else if (angle < 270) {
        return 90 + Math.random() * 90;
    } else if (angle < 360) {
        return Math.random() * 90;
    } else {
        return -1;
    }
}

/*
 * input: angle - Number
 * returns: random angle based on the possible trajectory the object can take
 * returns -1 if the angle is larger than 360 degrees
 *
 * call this when the object hits floor/ceiling
 */
var generateAngleFloor = function(angle) {
    if (angle < 90) {
        angle = 90 + Math.random() * 90;
    } else if (angle < 180) {
        angle = Math.random() * 90;
    } else if (angle < 270) {
        angle = 270 + Math.random() * 90;
    } else if (angle < 360) {
        angle = 180 + Math.random() * 90;
    } else {
        angle = -1;
    }
    return angle;
}

/*
 * inputs: moveDiv - div to be moved
 *         angle - Number, current angle of object
 * returns: no return value
 *
 * handles collision detection of the walls of browser
 */
var checkWalls = function(moveDiv, angle) {
    var x = (moveDiv.style.left);
    var y = (moveDiv.style.top);
    x=x.substring(0,x.length-2);
    x=parseInt(x);
    y=y.substring(0,y.length-2);
    y=parseInt(y);
    var height = window.innerHeight;
    var width = window.innerWidth;;

    if (x < 0 || x > width) {
        if (x < 0) {
            x = 2;
        }
        if (x > width) {
            x = width - 2;
        }

        // object is probably past boundaries, therefore move it back
        // in boundaries so other functions work properly
        moveDiv.style.left = x+"px";
        return generateAngleWall(angle);
    } else if (y < 0 || y > height) {
        if (y < 0) {
            y = 2;
        }
        if (y > width) {
            y = width - 2;
        }

        // object is probably past boundaries, therefore move it back
        // in boundaries so other functions work properly
        moveDiv.style.top = y+"px";
        return generateAngleFloor(angle);
    } else {
        return angle;
    }
}

var setXVelocity = function(angle, max) {
    if (angle < 180) {
        // should always be positive
        var xVel = Math.abs(Math.sin(angle * (180 / Math.PI)) * max);
        return xVel;
    } else {
        // should always be negative
        return -Math.abs(Math.sin(angle * (180 / Math.PI)) * max);
    }
}

var setYVelocity = function(angle, max) {
    if (angle < 270 && angle > 90) {
        // should always be negative
        var yVel = Math.abs(Math.cos(angle * (180 / Math.PI)) * max);
        return yVel;
    } else {
        // should always be positive
        return -Math.abs(Math.cos(angle * (180 / Math.PI)) * max);
    }
}


// start angle of duck
var angles = [];
var moveDivs = document.getElementsByClassName("move");
console.log(moveDivs.length);

var populateArray = function(length) {
    for (var i = 0; i < length; i++) {
        angles.push(360 * Math.random());
    }
}
populateArray(moveDivs.length);
console.log(angles);

var moveDuck = function(e) {
    var max = 5;

    for (var i = 0; i < moveDivs.length; i++) {
        var moveDiv = moveDivs[i];
        angles[i] = checkWalls(moveDiv, angles[i]);

        var x = (moveDiv.style.left);
        var y = (moveDiv.style.top);
        x=x.substring(0,x.length-2);
        x=parseInt(x);
        y=y.substring(0,y.length-2);
        y=parseInt(y);

        if (isNaN(x)) x=200;
        if (isNaN(y)) y=200;

        x = x + setXVelocity(angles[i], max);
        y = y + setYVelocity(angles[i], max);

        moveDiv.style.left = x + "px";
        moveDiv.style.top = y + "px";
    }

    checkMouse();
}

var myevent;
function startit() {
     myevent = setInterval(moveDuck,10);
}

function stopit() {
        window.clearTimeout(myevent);
}
