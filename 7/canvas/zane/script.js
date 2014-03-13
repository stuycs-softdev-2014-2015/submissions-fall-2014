var fps = 60;
var frameLength = 1000 / fps;
var canvas = document.getElementById("canvas");
var ctx = canvas.getContext("2d");
var textureAtlas = document.createElement("canvas");
var txctx = textureAtlas.getContext("2d");

var lines = [];
var rects = [];
var depths = [];
var ratios = []; //how far along the wall it is
var columns = 600;
var columnWidth = Math.floor((canvas.width / columns) + 0.5);
var depthConstant = 9000000;
var wallHeight = 20;

var speed = 3;
var turnSpeed = Math.PI / 50;
var pangle = 0;
var px = canvas.width/2;
var py = canvas.height/2;
var visionCone = Math.PI;
var visionHeight = Math.PI / 4;
var screenLength = canvas.width;
var screenHeight = 100;
var screenDist = (screenLength / 2) * Math.sin(visionCone / 2);

var keys = {
	 w : false,
	 a : false,
	 s : false,
	 d : false,
	 q : false,
	 e : false
}

var debugGraphics = false;
var pixelByPixel = true;

var wallTexture;

setup();
run();

function setup() {
	setupLevel();
	
	for (var i=0; i<columns; i++)
		depths.push(1000000);

	canvas.focus();

	textureAtlas.width = 10;
	textureAtlas.height = 10;

	wallTexture = new Image();
	wallTexture.onload = function() {
		txctx.drawImage(wallTexture, 0, 0);
	}
	wallTexture.src = "textures/wall.png";
}

function run() {
	update();
	draw();
	setTimeout(run, frameLength);
}

function update() {
	if(keys.w) {
		px += Math.cos(pangle) * speed;
		py += Math.sin(pangle) * speed;
	}

	if(keys.s) {
		px -= Math.cos(pangle) * speed;
		py -= Math.sin(pangle) * speed;
	}

	if(keys.e) {
		px -= Math.sin(pangle) * speed;
		py += Math.cos(pangle) * speed;
	}

	if(keys.q) {
		px += Math.sin(pangle) * speed;
		py -= Math.cos(pangle) * speed;
	}

	if (keys.a)
		pangle -= turnSpeed;
	if (keys.d)
		pangle += turnSpeed;
}

function draw() {

	clearCanvas();

	if (debugGraphics) {

		ctx.strokeStyle = "rgb(0,0,0)";
		for (var i=0; i<lines.length; i++)
			drawLine(lines[i]);

		//drawVisionLines();
		ctx.fillStyle = "rgb(255,0,0)";
		ctx.moveTo(px + Math.cos(pangle),
				   py + Math.sin(pangle));
		for (var dt = Math.PI / 4; dt < Math.PI * 9 / 4; dt += Math.PI / 2)
			ctx.lineTo(px + 5*Math.cos(pangle + dt),
					   py + 5*Math.sin(pangle + dt));

		ctx.fill();

	} else {
		rayCast();

		//scale color with depth
		for (var i=0; i<columns; i++) {
			drawRay(i);
		}
	}

	drawBorder();
}

function drawRay(i) {
	ctx.fillStyle = "rgb(0,0,0)";
	if (depths[i] == 0) {
		ctx.fillStyle = "rgb(0,0,60)";
		ctx.fillRect(i*columnWidth+1, 1,
					 columnWidth, canvas.height/2);

		ctx.fillStyle = "rgb(20,20,20)";
		ctx.fillRect(i*columnWidth+1, canvas.height/2 + 1,
					 columnWidth, canvas.height/2);
	} else {
		var heightFraction = wallHeight / (depths[i] * Math.tan(visionHeight));
		var apparentHeight = (canvas.height / 2) * heightFraction;

		//ceiling
		ctx.fillStyle = "rgb(0,0,60)";
		ctx.fillRect(i*columnWidth+1, 1,
					 columnWidth, canvas.height / 2 - apparentHeight);
		//floor
		ctx.fillStyle = "rgb(20,20,20)";
		ctx.fillRect(i*columnWidth+1, canvas.height / 2 + apparentHeight,
					 columnWidth, canvas.height / 2 - apparentHeight);

		//figure
		var px = txctx.getImageData(0, 0, 10, 10);

		if (pixelByPixel) {
			for (var j=0; j<10; j++) {
				var index = (Math.floor(ratios[i] * 10) + j * 10) * 4;
				ctx.fillStyle = "rgb(" + px.data[index] + "," +
								px.data[index + 1] + ","  + 
								px.data[index + 2] + ")";
				ctx.fillRect(i*columnWidth + 1, canvas.height / 2 - apparentHeight + apparentHeight * j / 5,
					 	 	 columnWidth, apparentHeight / 5 + 1);
			}
		} else
			ctx.drawImage(wallTexture, Math.floor(ratios[i] * 10), 0, 1, 10,
						  i*columnWidth + 1, canvas.height / 2 - apparentHeight,
						  columnWidth, apparentHeight * 2 + 1);
	}
}

function rayCast() {
	for (var i=0; i<columns; i++)
		depths[i] = 0;

	for (var i=0; i<columns; i++) {
		var columnWidth = screenLength / columns;
		var displacement = columnWidth * i - screenLength / 2;
		var angleToPix = Math.atan2(displacement, screenDist);
		var theta = pangle + angleToPix;

		var q = [px, py];
		var s = [1000 * Math.cos(theta),
				 1000 * Math.sin(theta)];

	 	for (var j=0; j<lines.length; j++) {
			var p = lines[j][0]; //p is the first point of the segment
			var r = pointSum(lines[j][1], negative(p)); //p+r is the second

			var t = crossProduct(pointSum(q, negative(p)), s) /
					crossProduct(r, s);
			var u = crossProduct(pointSum(q, negative(p)), r) /
					crossProduct(r, s);

			if (0 <= t && t <= 1 &&	0 <= u && u <= 1) {
				var point = pointSum(p, [t*r[0], t*r[1]]);
				var l = Math.sqrt((point[0] - px) * (point[0] - px) +
								  (point[1] - py) * (point[1] - py));

				//tweak depth based on distance from center
				var alpha = Math.PI/2 - Math.abs(theta - pangle);
				var c = Math.sin(alpha) * l;

				if (c < depths[i] || depths[i] == 0) {
					ratios[i] = t;
					depths[i] = c;
				}
			}
		}

		theta += visionCone / columns;
	}
}

function pointQuotient(point1, point2) {
	return [point1[0] / point2[0],
			point1[1] / point2[1]];
}

function pointSum(point1, point2) {
	return [point1[0] + point2[0],
			point1[1] + point2[1]];
}

function negative(point) {
	return [-point[0], -point[1]];
}

function crossProduct(point1, point2) {
	return point1[0] * point2[1] - point1[1] * point2[0];
}

function keyDown() {
	if (event.keyCode == 87 || event.keyCode == 75) {
		keys.w = true;
	} else if (event.keyCode == 65 || event.keyCode == 72) {
		keys.a = true;
	} else if (event.keyCode == 83 || event.keyCode == 74) {
		keys.s = true;
	} else if (event.keyCode == 68 || event.keyCode == 76) {
		keys.d = true;
	} else if (event.keyCode == 81) {
		keys.q = true;
	} else if (event.keyCode == 69) {
		keys.e = true;
	}

	if (event.keyCode == 80)
		debugGraphics = !debugGraphics;
}

function keyUp() {
	if (event.keyCode == 87 || event.keyCode == 75) {
		keys.w = false;
	} else if (event.keyCode == 65 || event.keyCode == 72) {
		keys.a = false;
	} else if (event.keyCode == 83 || event.keyCode == 74) {
		keys.s = false;
	} else if (event.keyCode == 68 || event.keyCode == 76) {
		keys.d = false;
	} else if (event.keyCode == 81) {
		keys.q = false;
	} else if (event.keyCode == 69) {
		keys.e = false;
	}
}
