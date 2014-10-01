

var height = 500, width = 500;




console.log("HELLO");

var height=400, width=400;
var yPadding=10;
var xPadding=40;

var d1 = [ {'label':'a','y':Math.floor(Math.random()*100)},
	   {'label':'b','y':Math.floor(Math.random()*100)},
	   {'label':'c','y':Math.floor(Math.random()*100)},
	   {'label':'d','y':Math.floor(Math.random()*100)},
	   {'label':'e','y':Math.floor(Math.random()*100)},
	   {'label':'f','y':Math.floor(Math.random()*100)},
	   {'label':'g','y':Math.floor(Math.random()*100)}
	 ]


var data = [];
for(var x=0;x<10;x++){
    data[x] = {"r":Math.floor(Math.random()*20)+5,"x":Math.floor(Math.random()*(width-100)+100),"y":Math.floor(Math.random()*(height-100))};
}


var svg = d3.select("body").append("svg")
    .attr("width",width)
    .attr("height",height)
    .attr("id","svg");


var k = svg.selectAll("circle")
    .data(data)
    .enter()
    .append("circle")
    .attr("r",function(d){ return d.r })
    .attr("cx",function(d){ return d.x })
    .attr("cy",function(d){ return d.y; })
    .attr("fill","red");


var yScale = d3.scale.linear()
	.domain([0, d3.max(data,function(d){return d.y;}) ])
	.range([height,0]);

var yAxis = d3.svg.axis()
	.scale(yScale)
	.ticks(5)
	.orient("left")



svg.append("g")
    .attr('class','axis')
    .attr('transform','translate (30,-20)')
    .call(yAxis);
