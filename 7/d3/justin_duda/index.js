

var data = [10,29,39,8,13,49]

d3.select(".canvas")
	.selectAll("div")
	.data(data)
	.enter()
	.append("div")
	.style("width", function(d) { return d * 10 + "px"; })
	.text(function(d) {return d;});
