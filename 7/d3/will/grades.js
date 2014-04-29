
console.log("HELLO");

var height=400, width=900;
var yPadding=10;
var xPadding=10;


function getRandomColor() {
    var letters = '0123456789ABCDEF'.split('');
    var color = '#';
    for (var i = 0; i < 6; i++ ) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}



d3.csv("grades.csv",function(d) {MakeSVG(d);});

var xScale = d3.scale.linear() 
	.domain([0,850])
	.range([0,width]);


var yScale = d3.scale.linear() 
	.domain([0,100])
	.range([height,0]);

var MakeSVG = function(d) {

    var svg = d3.select("body").append('svg')
	    .attr('width',width)
	    .attr('height',height)
	    .attr('id','svg')
	    .style('border','solid px');
    var yAxis = d3.svg.axis()
	    .scale(yScale)
	    .orient('left');

    var c = svg.selectAll('grades')
	    .data(d)
	    .enter()
	    .append('circle')
	    .attr('r',5)
	    .attr('cx',function(d,i) { return xScale(i)+40;})
	    .attr('cy',function(d) {return yScale(d.overall);})
    .attr('fill',function() {return getRandomColor();})


svg.append('g')
    .attr('class','axis')
    .attr('transform','translate(30,0)')
    .call(yAxis);

/*
    c.transition()
	.duration(5000)
	.delay(5000)
	.attr('cy',function(d) { return yScale(d.english);})
*/
}
