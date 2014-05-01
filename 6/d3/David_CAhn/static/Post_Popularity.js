// var favorite_vals = "{{ favorite_vals | tojson | safe}}";
//console.log( favorite_vals)
// Graphs your posts to tell you how popular they have been using d3.js

var height=400, width=400;
var yPadding=10;
var xPadding=40;

var svg = d3.select("body").append('svg')
    .attr('width',width)
    .attr('height',height)
    .attr('id','svg')
    .style('border','1px solid');

d1 = []

// Nikhil Goyal's favorite values for recent posts
favorite_vals = [0, 0, 0, 0, 0, 0, 1, 2, 17, 3, 0, 2, 1, 2, 1, 2, 2, 3, 1, 0, 0, 0, 0, 2, 0, 3, 2, 1, 2, 0, 0, 1, 3, 4, 34, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 2, 0, 1, 1, 3, 2, 2, 2, 0, 0, 2, 0, 2, 1, 0, 7, 0, 2, 4, 4, 10, 4, 4, 5, 1, 1, 2, 0, 2, 0, 3, 5, 3, 5, 0, 3, 6, 1, 12, 18, 0, 3, 6, 1, 0, 5, 3, 1, 12, 1, 1, 2, 0, 0, 1, 0, 2, 0, 0, 1, 0, 0, 2, 1, 1, 0, 3, 6, 0, 2, 0, 0, 1, 0, 0, 0, 0, 3, 0, 4, 0, 0, 0, 0, 2, 0, 3, 5, 2];

for (i=0; i<favorite_vals.length; i++) {
    d1.push ({
	'label':i,
	'x':i,
	'y':favorite_vals[i]
    })
    console.log(favorite_vals[i])
}

var yScale = d3.scale.linear()
	.domain([-2, d3.max(d1,function(d){return d.y;}) ])
	.range([height,0]);

var xScale = d3.scale.linear()
    .domain([d3.max(d1,function(d){return d.x;})+20,-9 ])
    .range([width,0]);

var c = svg.selectAll("circle")
    .data(d1)
    .enter()
    .append("circle")
    .attr('r',5)
    .attr('cx',function(d) {return xScale (d.x);})
    .attr('cy',function(d) {return yScale (d.y);})
    .attr('fill','steelblue');


var yAxis = d3.svg.axis()
	.scale(yScale)
	.ticks(10)
	.orient('left')

var xAxis = d3.svg.axis()
	.scale(xScale)
	.ticks(10)
	.orient('')

svg.append("g")
    .attr('class','axis')
    .attr('transform','translate (25,-20)')
    .call(yAxis);

svg.append("g")
    .attr('class','axis')
    .attr('transform','translate (0,375)')
    .call(xAxis);
