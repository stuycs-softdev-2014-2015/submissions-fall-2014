/*
 *  game_of_life.js contains a Canvas implementation of Conway's Game of Life.
*/

canvas = document.getElementById("canvas");
ctx = canvas.getContext("2d");

mapHeight = 200;
mapWidth = 200;
tickPause = 1e3 / 60;
numTicks = 2000;

cells = [];

function gameOfLife(){
	initializeCells();
	for(var tick = 0; tick < numTicks; tick++)
		setTimeout(lifeCycle, tickPause * tick);
};

function initializeCells(){
	for(var row = 0; row < mapHeight; row++){
		cells[row] = [];
		for(var col = 0; col < mapWidth; col++)
			cells[row][col] = {
				alive : Math.floor(Math.random() * 10) % 2,
				aliveNeighbors : 0
			};
	};
};

function iterateCells(func){
	for(var row = 1; row < mapHeight - 1; row++)
		for(var col = 1; col < mapWidth - 1; col++)
			func(row, col);
};

function countNeighbors(){
	iterateCells(function(row, col){
			cells[row][col].aliveNeighbors =
				cells[row][col - 1].alive +
				cells[row][col + 1].alive +
				cells[row - 1][col].alive +
				cells[row + 1][col].alive +
				cells[row + 1][col + 1].alive +
				cells[row + 1][col - 1].alive +
				cells[row - 1][col + 1].alive +
				cells[row - 1][col - 1].alive;
		}
	);
}

function lifeCycle(){
	countNeighbors();
	clearScreen();
	iterateCells(function(row, col){
			var aliveNeighbors = cells[row][col].aliveNeighbors;
			if(cells[row][col].alive){
				drawPixel(row, col);

				if(aliveNeighbors < 2 || 3 < aliveNeighbors)
					cells[row][col].alive = 0;
			}

			else if(aliveNeighbors == 3)
				cells[row][col].alive = 1;
		});
};

function drawPixel(x, y){
	xRatio = canvas.width / mapWidth;
	yRatio = canvas.height / mapHeight;
	ctx.fillStyle = "#00FF00";
	ctx.fillRect(x * xRatio, y * yRatio, xRatio, yRatio);
};

function clearScreen(){
	ctx.fillStyle = "#000";
	ctx.fillRect(0, 0, canvas.width, canvas.height);
};

gameOfLife();
