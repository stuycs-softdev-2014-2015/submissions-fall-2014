/*
 *  game_of_life.js contains an SVG implementation of Conway's Game of Life.
*/

svg = document.getElementById("svg");
svgNS = "http://www.w3.org/2000/svg";

mapHeight = 30;
mapWidth = 30;

cellHeight = parseInt(svg.getAttribute("height")) / mapHeight;
cellWidth = parseInt(svg.getAttribute("width")) / mapWidth;

tickPause = 1e3 / 30;
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
		for(var col = 0; col < mapWidth; col++){
			cells[row][col] = {
				alive : Math.floor(Math.random() * 10) % 2,
				aliveNeighbors : 0
			};
			drawPixel(row, col, "black");
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

			drawPixel(col, row, (cells[row][col].alive?"green":"black"));
			if(cells[row][col].alive){
				if(aliveNeighbors < 2 || 3 < aliveNeighbors)
					cells[row][col].alive = 0;
			}

			else if(aliveNeighbors == 3)
				cells[row][col].alive = 1;
		});
};

function drawPixel(x, y, color){
	var cell = document.createElementNS(svgNS, "rect");
	cell.setAttributeNS(null, "x", x * cellWidth);
	cell.setAttributeNS(null, "y", y * cellHeight);
	cell.setAttributeNS(null, "width", cellWidth);
	cell.setAttributeNS(null, "height", cellHeight);
	cell.setAttributeNS(null, "fill", color);
	cell.setAttributeNS(null, "stroke", "none");
	svg.appendChild(cell);
};

function clearScreen(){
	while(svg.firstChild)
		svg.removeChild(svg.firstChild);
};

gameOfLife();
