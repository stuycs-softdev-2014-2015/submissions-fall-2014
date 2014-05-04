d3.selectAll("div")
    .data([170,225])
    .transition()
    .duration(2500)
    .style("width", function(d) { return  d + "px"; })
    .style("background-color","white")
    .style("color","#6495ED");

var draw_data = function(data){
    var svg=d3.select("svg");
    var circle=svg.selectAll("circle").data(data);

    circle.enter().append("circle")
	.attr("cx",function(d,i){return 100*(i+1);})
	.attr("cy",function(d,i){return 200})
	.attr("r",0);
    
    circle.transition()
	.duration(750)
	.attr("r",function(d){return Math.sqrt(d);})
	.attr("cx",function(d,i){return 100*(i+1);})
	.attr("cy",function(d,i){return 100;})
	.attr("r", function(d){return i*2;});

    circle.exit()
	.transition()
	.duration(750)
	.attr("r",0)
	.remove();
};


var change_color = function(data){
    var svg=d3.select("svg");
    var circle=svg.selectAll("circle").data(data);

    circle.transition()
	.duration(1000)
	.attr("fill",function(d){return d;});

    circle.exit()
	.transition()
	.duration(750)
	.attr("r",0)
	.remove();
};


setTimeout(function(){draw_data([500,300]);},3000);
setTimeout(function(){draw_data([1000,1500,3000]);},4500);
setTimeout(function(){draw_data([100,1000,1000,400]);},6000);
setTimeout(function(){draw_data([1000,400,1500,800,300,]);},7500);
setTimeout(function(){draw_data([1200,1000,800,600,400,200]);},9000);

setTimeout(function(){change_color([red,orange,yellow,green,blue,purple]);},10000);

setTimeout(function(){draw_data([]);},11000);
