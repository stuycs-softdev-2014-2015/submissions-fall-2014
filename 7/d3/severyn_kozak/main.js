/*
 *  D3 script to render the countries of the world using the
 *  `countries.geo.json` GeoJSON file, with a randomized fill color.
*/

width = 1500;
height = 500;

path = d3.geo.path().projection(d3.geo.mercator());

svg = d3.select("#center")
	.append("svg")
	.attr("width", width)
	.attr("height", height);

d3.json("countries.geo.json", function(geoJson){

	svg.selectAll("path")
		.data(geoJson.features)
		.enter()
		.append("path")
		.attr("d", path)
		.attr("stroke", "black")
		.style("fill", function(data){
			return "#" + Math.floor(Math.random() * 16777215).toString(16);
		});
});
