var height = 400, width = 900;

var bigt;

var MakeSVG = function() {

    if (bigt) clearTimeout(bigt);

    var body = d3.select('body');

    var svg = body.append("svg")
	.attr('width', width)
	.attr('height', height)
	.attr('id', 'svg');

    body.append('br');

    body.append("em")
	.text('Vehicle Information: ')

    var infot = body.append('div')

    var color = "#000000";
    
    var display = function(d) {
	var va = d[0].VehicleActivity;
 	var txmin = va[0].MonitoredVehicleJourney.VehicleLocation.Latitude;
	var tymin = va[0].MonitoredVehicleJourney.VehicleLocation.Longitude;
	var tsmin = va[0].MonitoredVehicleJourney.MonitoredCall.Extensions.Distances.DistanceFromCall;
 	var txmax = va[0].MonitoredVehicleJourney.VehicleLocation.Latitude;
	var tymax = va[0].MonitoredVehicleJourney.VehicleLocation.Longitude;
	var tsmax = va[0].MonitoredVehicleJourney.MonitoredCall.Extensions.Distances.DistanceFromCall;
	var tval;
	for (i in va) {
	    tval = va[i].MonitoredVehicleJourney.VehicleLocation.Latitude;
	    if (tval > txmax)
		txmax = tval;
	    if (tval < txmin)
		txmin = tval;

	    tval = va[i].MonitoredVehicleJourney.VehicleLocation.Longitude;
	    if (tval > tymax)
		tymax = tval;
	    if (tval < tymin)
		tymin = tval;

	    tval = va[i].MonitoredVehicleJourney.MonitoredCall.Extensions.Distances.DistanceFromCall;
	    if (tval > tsmax)
		tsmax = tval;
	    if (tval < tsmin)
		tsmin = tval;
	}

	var xScale = d3.scale.linear()
	    .domain([txmin, txmax])
	    .range([10, width - 10]);

	var yScale = d3.scale.linear()
	    .domain([tymin, tymax])
	    .range([30, height - 30]);

	var sScale = d3.scale.linear()
	    .domain([tsmin, tsmax])
	    .range([1, 50])

	svg.selectAll('g').remove();

	var buses = svg.selectAll('.buses')
	    .data(va, function(dat) {return dat.MonitoredVehicleJourney.VehicleRef;});

	buses.transition()
	    .duration(7000)
	    .attr('r', function(dat) {return sScale(dat.MonitoredVehicleJourney.MonitoredCall.Extensions.Distances.DistanceFromCall);})
	    .attr('cx', function(dat) {return xScale(dat.MonitoredVehicleJourney.VehicleLocation.Latitude);})
	    .attr('cy', function(dat) {return yScale(dat.MonitoredVehicleJourney.VehicleLocation.Longitude);})
	    .attr('fill-opacity', function(dat){
		if (dat.MonitoredVehicleJourney.ProgressRate == "noProgress")
		    return .5;
		return 1;
	    })

	buses.enter()
	    .append('circle')
	    .attr('r', function(dat) {return sScale(dat.MonitoredVehicleJourney.MonitoredCall.Extensions.Distances.DistanceFromCall);})
	    .attr('cx', function(dat) {return xScale(dat.MonitoredVehicleJourney.VehicleLocation.Latitude);})
	    .attr('cy', function(dat) {return yScale(dat.MonitoredVehicleJourney.VehicleLocation.Longitude);})
	    .attr('fill', color)
	    .attr('class', 'buses')
	    .attr('stroke', 'black')
	    .attr('stroke-width', 2)
	    .on("mouseover", function(dat) {
		var t = '<br/>Vehicle Ref: ';
		t += dat.MonitoredVehicleJourney.VehicleRef;
		t += '<br/>Next Stop: ';
		t += dat.MonitoredVehicleJourney.MonitoredCall.StopPointName;
		t += '<br/>Distance From Stop: ';
		t += dat.MonitoredVehicleJourney.MonitoredCall.Extensions.Distances.PresentableDistance;
		t += ' (' + dat.MonitoredVehicleJourney.MonitoredCall.Extensions.Distances.DistanceFromCall + 'm)';
		t += '<br/>Bearing: ' + dat.MonitoredVehicleJourney.Bearing;
		infot.html(t);
	    }).on("mouseout", function(){infot.text('');})

	buses.exit().remove()
    }
    
    var lid = '';

    var go = function() {
	var address = 'http://162.243.244.8:9000/route/';
	d3.json(address+'info/'+lid+'.json',
		  function(data) {color = '#'+data.color;});
	d3.json(address+'monitor/'+lid+'.json', display)
	console.log('Fetching: ' + lid);
    }
    d3.selectAll('#go').on('click', function() {
	clearTimeout(bigt);
	lid = d3.selectAll('#lid')[0][0].value;
	go();
	var timer = function() {
	    var t = 10;
	    return function() {
		d3.selectAll('#sec').text(t);
		bigt = setTimeout(timer, 1000);
		if (t <= 0) {
		    t = 10;
		    go();
		}
		t--;
	    }
	}();
	timer();
    });
}

MakeSVG();
