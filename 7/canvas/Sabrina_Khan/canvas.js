$(document).ready(function(){

var canvas = $("#canvas")[0];;
 var ctx = canvas.getContext("2d");
  var w = $("#canvas").width();
  var h = $("#canvas").height;
  
  var food;
  var direction;
  var cellw= 10;

  var snake;
  function init()
  {
  d = "right";
  createsnake();
  createfood();
  if(typeof game_loop != "undefined") 
  clearInterval(game_loop);
  game_loop = setInterval(paint, 60);
  }
  init();
  function createsnake()
  {
  var length = 5;
  snake=[]
  for(var i=length-1;i>=0;i--)
  {snake.push({x,i,y:0});}
  }
  }
  function createfood()
  {food = {x: Math.round(Math.random()*(w-cellw)/cellw), 
  y: Math.round(Math.random()*(h-cellw)/cellw),};
  }
  function paint()
  {ctx.fillStyle = "white";
  ctx.fillRect(0, 0, w, h);
  ctx.strokeStyle = "black";
  ctx.strokeRect(0, 0, w, h);
  var nx = snake[0].x;
  var ny = snake[0].y;
  if(d == "right") nx++;
  else if(d == "left") nx--;
  else if(d == "up") ny--;
  else if(d == "down") ny++;
  if(nx == -1 || nx == w/cellw || ny == -1 || ny == h/cellw || check_collision(nx, ny, snake_array))
  {init();
  return;
  }
  if(nx == food.x && ny == food.y)
  {var tail = {x: nx, y: ny};
  create_food();}
  else{var tail = snake_array.pop();
  tail.x = nx; tail.y = ny;}
  snake.unshift(tail); 
  for(var i = 0; i < snake_array.length; i++){
	var c = snake_array[i];
	paint_cell(c.x, c.y);}
paint_cell(food.x, food.y);}
function paint_cell(x, y)
	{ctx.fillStyle = "blue";
	ctx.fillRect(x*cellw, y*cellw, cellw, cellw);
	ctx.strokeStyle = "white";
	ctx.strokeRect(x*cellw, y*cellw, cellw, cellw);}

function check_collision(x, y, array)
	{for(var i = 0; i < array.length; i++)
	{if(array[i].x == x && array[i].y == y)
	return true;}
	return false;}

	$(document).keydown(function(e){
		var key = e.which;
		if(key == "37" && d != "right") d = "left";
		else if(key == "38" && d != "down") d = "up";
		else if(key == "39" && d != "left") d = "right";
		else if(key == "40" && d != "up") d = "down";
	})
})
