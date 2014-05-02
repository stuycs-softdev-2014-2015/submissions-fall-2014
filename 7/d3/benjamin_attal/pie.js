var width = 900,
    height = 900,
    radius = height / 2;

var color = d3.scale.ordinal()
    .range(["#98abc5", "#8a89a6", "#7b6888", "#6b486b", "#a05d56", "#d0743c", "#ff8c00"]);

//Pie chart layout, will convert data from the csv to arc length data
var pie = d3.layout.pie()
    .sort(null)
    .value(function(d) { return d.number; });

//An arc, will be given arc length from the pie chart layout
var arc = d3.svg.arc()
    .outerRadius(radius - 10)
    .innerRadius(0);

//Main svg element
var svg = d3.select("body").append("svg")
    .attr("width", width)
    .attr("height", height)
    .append("g")
    .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");

//Iterate over the data
d3.csv("carts.csv", function(error, data) {

    //Bind the pie chart data to the parent of the paths
    var g = svg.selectAll(".arc")
        .data(pie(data))
        .enter().append("g")
            .attr("class", "arc");

    //Paths will inherit pie chart data from the parent, which automatically fills in the size of the arc based on the data
    g.append("path")
        .attr("d", arc)
        .style("fill", function(d) { return color(d.data.city); });

    //Append the text
    g.append("text")
        .attr("transform", function(d) { return "translate(" + arc.centroid(d) + ")"; })
        .attr("dy", ".35em")
        .style("text-anchor", "middle")
        .text(function(d) { return d.data.city; });

});
