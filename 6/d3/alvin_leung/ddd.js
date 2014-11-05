var draw = function(data){
    
    var svg = d3.select("svg");
    var boxes = svg.selectAll("rect").data(data);
    
    boxes.enter()
	.append("rect")
	.attr("width",function(d,i){return 500/data.length;})
	.attr("height",function(d,i){return d*20;})
	.attr("x",function(d,i){return (500/data.length) * i;})
	.attr("y",function(d,i){return 0;})


    boxes.transition()
	.duration(750)
	.attr("width",function(d,i){return 500/data.length;})
	.attr("height",function(d,i){return d*20;})
	.attr("x",function(d,i){return (500/data.length) * i;})
	.attr("y",function(d,i){return 500-d*10;})

    boxes.exit()
	.transition()
	.duration(750)
	.remove();
    
}

var dat = [1];
setInterval(function(){
    if(dat.length < 30)
	dat.push(Math.random()*dat.length);
    draw(dat);},
	    1000);
