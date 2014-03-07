var tileWidth = 20;
var tileHeight = 20;
var worldWidth = 60;
var worldHeight = 40;

var WALL_ID = 0;

function setupLevel() {
	var canvas = document.createElement("canvas");
	var ctx = canvas.getContext("2d");

	var level = new Image();
	level.onload = function() {
		ctx.drawImage(level, 0, 0);

		var world = ctx.getImageData(0, 0, worldWidth, worldHeight);

		for (var i=0; i<worldHeight; i++)
			for (var j=0; j<worldWidth; j++)
				if (world.data[(i * worldWidth + j)*4] == WALL_ID)
					addRect(newTile(j, i));
	}
	level.src = "textures/level.png";
}

function newTile(x, y) {
	return newRect(x * tileWidth, y * tileHeight,
				   tileWidth, tileHeight);
}
