/*
 *  D3 script to render the countries of the world using the
 *  `countries.geo.json` GeoJSON file, with a randomized fill color.
*/

var width = 1500;
var height = 500;

var path = d3.geo.path().projection(d3.geo.mercator());

var svg = d3.select("#center").append("svg").attr("width", width).
	attr("height", height);

d3.json("countries.geo.json", function(json) {

	svg.selectAll("path")
		.data(json.features)
		.enter()
		.append("path")
		.attr("d", path)
		.attr("stroke", "black")
		.style("fill", function(data){
			return "#" + Math.floor(Math.random() * 16777215).toString(16);
		});
});
