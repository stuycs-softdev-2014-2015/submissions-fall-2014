console.log("Hello");

var data = {};
var svg = d3.select("body").append("svg")
    .attr("width",400)
    .attr("height",400)
    .attr("id","svg");

d3.csv("USArrests.csv")
    .row(function(d) {
	return {State : d.State, Murder: d.Murder, Assault: d.Assault,
		UrbanPop : d.UrbanPop, Rape : d.Rape};
    })
    .get(function(error, rows) {
	data = rows;
	console.log(data);
	svg.selectAll("circle")
	    .data(data)
	    .enter()
	    .append("circle")
	    .attr("cx",function(d) {return d.UrbanPop * 4;})
	    .attr("cy",function(d) {return -1 * d.Assault + 400;})
	    .attr("fill","#ff0000")
	    .attr("r",5);
	});
