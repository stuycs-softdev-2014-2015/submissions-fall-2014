var width = 300;
var height = 210;

var header = d3.select("body")
    .append("h1")
    .text("France");

var canvas = d3.select("body")
    .append("svg")
    .attr("width", width)
    .attr("height", height);

var red = canvas.append("rect")
    .attr("width", width/3)
    .attr("height", height)
    .attr("x",0)
    .attr("fill", "red");

red.transition()
    .delay(1500)
    .duration(1500)
    .attr("x", width*2/3);

var white = canvas.append("rect")
    .attr("width", width/3)
    .attr("height", height)
    .attr("x",0)
    .attr("fill", "white");


white.transition()
    .delay(3000)
    .duration(1500)
    .attr("x", width/3);

var blue = canvas.append("rect")
    .attr("width", width/3)
    .attr("height", height)
    .attr("fill", "blue");

red.transition()
    .delay(4000)
    .duration(1500)
    .attr("width", 0)
    .attr("height", 0);

blue.transition()
    .delay(4000)
    .duration(1500)
    .attr("width", 0)
    .attr("height", 0);

header.transition()
    .delay(4500)
    .duration(2000)
    .text("Japan");

white.transition()
    .delay(4500)
    .duration(1500)
    .attr("stroke", "black")
    .attr("x", 0)
    .attr("width", width);

var circle = canvas.append("circle")
    .attr("cy", 0)
    .attr("cx", 0)
    .attr("r",0);

circle.transition()
    .delay(4500)
    .duration(1500)
    .attr("cx", 150)
    .attr("cy", 105)
    .attr("r", 63)
    .attr("fill", "red");