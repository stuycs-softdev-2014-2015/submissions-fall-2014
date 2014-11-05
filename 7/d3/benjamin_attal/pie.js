var width = 700,
    height = 700,
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
    var chart = svg.selectAll(".arc")
        .data(pie(data), function(d) {return d.data.city;})
        .enter().append("g")
            .attr("class", "arc");

    //Paths will inherit pie chart data from the parent, which automatically fills in the size of the arc based on the data
    chart.append("path")
        .attr("d", arc)
        .style("fill", function(d) { return color(d.data.city); });

    //Append the text
    chart.append("text")
        .attr("transform", function(d) { return "translate(" + arc.centroid(d) + ")"; })
        .attr("dy", ".35em")
        .style("text-anchor", "middle")
        .text(function(d) { return d.data.city; });

    chart.on('click', function(d, i) {
        var a;
        for(a = 0; a < data.length; a++) {
            if (a !== i)
                data[a].number = "0";
        }

        console.log(data);

        var path = chart.selectAll("path");
        chart.selectAll("text")
            .text("");

        path.each(function(d) { this._lastDatum = d; })
            .data(pie(data), function(d) {return d.data.city;})
            .transition()
                .duration(500)
                .attrTween("d", arcTween);

        var message = "";
        path.each(function(d) {
            if (d.data.number != 0)
                message = d.data.city + ", " + d.data.number;
        });

        d3.select("svg").append("text")
            .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")")
            .attr("dy", ".35em")
            .style("text-anchor", "middle")
            .text(function(d) { return message; });
    });
});

//Help from Edric Huang
function arcTween(d) {
    var i = d3.interpolate(this._lastDatum, d);
    this._lastDatum = i(0);
    return function(t) { return arc(i(t)); };
}
