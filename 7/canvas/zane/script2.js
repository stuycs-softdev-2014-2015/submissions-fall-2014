function drawLine(line) {
	ctx.beginPath();
	ctx.moveTo(line[0][0], line[0][1]);
	ctx.lineTo(line[1][0], line[1][1]);
	ctx.stroke();
}

function newLine(x1, y1, x2, y2) {
	return [[x1,y1], [x2,y2], Math.floor(Math.random()*3)];
}

function clearCanvas() {
	ctx.fillStyle = "rgb(255,255,255)";
	ctx.fillRect(1,1, canvas.width-2, canvas.height-2);
}

function drawBorder() {
	var canvas = document.getElementById("canvas");
	var ctx = canvas.getContext("2d");

	ctx.strokeStyle = "rgb(0,0,0)";

	ctx.beginPath();

	ctx.moveTo(0, 0);
	ctx.lineTo(canvas.width, 0);
	ctx.lineTo(canvas.width, canvas.height);
	ctx.lineTo(0, canvas.height);
	ctx.lineTo(0, 0);

	ctx.stroke();
}

function randomLine() {
	var x1 = Math.random() * canvas.width;
	var y1 = Math.random() * canvas.height;
	var x2 = x1 + Math.random()*200 - 100;
	var y2 = y1 + Math.random()*200 - 100;

	return newLine(x1, y1, x2, y2);
}

function newRect(x, y, w, h) {
	points = []

	points.push([x,   y]);
	points.push([x+w, y]);
	points.push([x+w, y+h]);
	points.push([x,   y+h]);

	return points;
}

function randomRect() {
	var x = canvas.width * Math.random();
	var y = canvas.height * Math.random();
	var w = 100 * Math.random();
	var h = 100 * Math.random();

	return newRect(x, y, w, h);
}

function addRect(rect) {
	rects.push(rect);
	lines.push([rect[0], rect[1]]);
	lines.push([rect[1], rect[2]]);
	lines.push([rect[2], rect[3]]);
	lines.push([rect[3], rect[0]]);
}
