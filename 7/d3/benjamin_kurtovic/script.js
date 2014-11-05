var width = 1004,
    height = 608;

var svg, projection;

var time = moment.utc().subtract("minutes", "5");

var geolocate = function(ip) { return "http://freegeoip.net/json/" + ip + "?callback=?"; };

function load_from_api() {
    var url = "https://en.wikipedia.org/w/api.php";
    url += "?action=query&list=recentchanges&rcprop=user&rcshow=anon&rctype=edit&rcnamespace=0&rcstart="
    url += time.format("YYYYMMDDhhmmss") + "&rcdir=newer&rclimit=50&format=json&callback=?"

    $.getJSON(url, function(data) {
        if (data.query !== undefined && data.query.recentchanges !== undefined) {
            for (var i in data.query.recentchanges) {
                var ip = data.query.recentchanges[i].user;
                if (ip.indexOf(":") != -1)
                    continue;
                $.getJSON(geolocate(ip), function(data) {
                    svg.append("circle")
                       .attr("transform", function() {return "translate(" + projection([data.longitude, data.latitude]) + ")";})
                       .attr("r", 20)
                       .attr("fill-opacity", 0.5)
                       .attr("fill", "#8B0000")
                       .transition()
                       .duration(2000)
                       .attr('r', 5)
                       .attr("fill-opacity", 1)
                       .attr("fill", "#483D8B");
                });
            }
        }

        time = moment.utc();
        setTimeout(load_from_api, 2000);
    });
}

$(document).ready(function() {
    svg = d3.select("#content").append("svg").attr("width", width).attr("height", height);
    projection = d3.geo.winkel3().scale(200).translate([width / 2, height / 2]);
    var path = d3.geo.path().projection(projection);

    d3.json("world.json", function(error, world) {
        var land = topojson.feature(world, world.objects.land),
            ocean = topojson.feature(world, world.objects.ocean),
            coast = topojson.feature(world, world.objects.coast);

        svg.append("path").datum(ocean).attr("d", path).style("fill", "lightblue");
        svg.append("path").datum(land).attr("d", path).style("fill", "blanchedalmond");
        svg.append("path").datum(coast).attr("d", path).style("fill-opacity", "0").attr("stroke", "#998D7B");
    });

    load_from_api();
});
