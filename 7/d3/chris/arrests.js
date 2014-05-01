console.log("Hello");

var data = {};
var svg = d3.select("body").append("svg")
    .attr("width",500)
    .attr("height",500)
    .attr("id","svg");

var firstData = true;

var dataSwitchMaker = function(s, scale) {
    var f = function() {
	if (!firstData) {
	    svg.selectAll("circle")
		.data(data)
		.transition()
		.duration(1000)
		.attr("cx",function(d) {return d.UrbanPop * 4 + 50;})
		.attr("cy",function(d) {return -1 * scale * d[s] + 450;})
		.attr("fill","#ff0000")
		.attr("r",5);
        } else {
	    svg.selectAll("circle")
		.data(data)
		.enter()
		.append("circle")
		.attr("cx",function(d) {return d.UrbanPop * 4 + 50;})
		.attr("cy",function(d) {return -1 * scale * d[s] + 450;})
		.attr("fill","#ff0000")
		.attr("r",5);
	    firstData = false;
	}
	svg.selectAll(".yaxis").remove();
	var yScale = d3.scale.linear().domain([0,450/scale]).range([450,50]);
	var yAxis = d3.svg.axis().scale(yScale).orient("left");
	svg.append("g").attr("class","yaxis")
	.attr("transform","translate(60,0)")
	    .call(yAxis);
	svg.selectAll(".yaxis")
	    .append("text")
	    .attr("transform","rotate(-90)")
	    .attr("x",-225)
	    .attr("y",-45)
	    .style("text-anchor", "middle")
	    .text("Arrests Per 100,000 Residents");
    }
    return f;
}

var xScale = d3.scale.linear().domain([0,100]).range([50,450]);
var xAxis = d3.svg.axis().scale(xScale).orient("bottom");
svg.append("g").attr("class","xaxis")
    .attr("transform","translate(0,440)")
    .call(xAxis);

svg.selectAll(".xaxis")
    .append("text")
    .attr("x",225)
    .attr("y",40)
    .style("text-anchor", "middle")
    .text("Urban Percentage of Population");

var assault = dataSwitchMaker("Assault", 1);
var murder = dataSwitchMaker("Murder", 20);
var rape = dataSwitchMaker("Rape", 8);
var total = dataSwitchMaker("Total", 1);

d3.csv("USArrests.csv")
    .row(function(d) {
	return {State : d.State, Murder: d.Murder, Assault: d.Assault,
		UrbanPop : d.UrbanPop, Rape : d.Rape, Total : parseInt(d.Murder) + parseInt(d.Assault) + parseInt(d.Rape)};
    })
    .get(function(error, rows) {
	data = rows;
	console.log(data);
	assault();
	});


document.getElementById("a").addEventListener("click",assault);
document.getElementById("m").addEventListener("click",murder);
document.getElementById("r").addEventListener("click",rape);
document.getElementById("t").addEventListener("click",total);

