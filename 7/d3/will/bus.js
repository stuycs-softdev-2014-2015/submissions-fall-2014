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

    var infot = body.append("span")
	.text('Vehicle Reference: ')
	.append('span')

    var color = "#000000";
    
    var display = function(d) {
	var txmax = 0, tymax = 360, tsmax = 0;
	var tval;
	var va = d[0].VehicleActivity;
	for (i in va) {
	    tval = va[i].MonitoredVehicleJourney.MonitoredCall.Extensions.Distances.DistanceFromCall;
	    if (tval > txmax)
		txmax = tval;
	    tval = va[i].MonitoredVehicleJourney.MonitoredCall.Extensions.Distances.CallDistanceAlongRoute;
	    if (tval > tsmax)
		tsmax = tval;
	}

	var xScale = d3.scale.linear()
	    .domain([0, txmax])
	    .range([0, width - 10]);

	var yScale = d3.scale.linear()
	    .domain([0, tymax])
	    .range([30, height - 30]);

	var sScale = d3.scale.linear()
	    .domain([0, tsmax])
	    .range([10, 50])

	var xAxis = d3.svg.axis()
	    .scale(xScale)
	    .orient('bottom');

	svg.selectAll('g').remove();

	svg.append('g')
	    .attr('class', 'axis')
	    .call(xAxis);

	var buses = svg.selectAll('.buses')
	    .data(va, function(dat) {return dat.MonitoredVehicleJourney.VehicleRef;});

	buses.transition()
	    .duration(5000)
	    .attr('r', function(dat) {return sScale(dat.MonitoredVehicleJourney.MonitoredCall.Extensions.Distances.CallDistanceAlongRoute);})
	    .attr('cx', function(dat) {return xScale(dat.MonitoredVehicleJourney.MonitoredCall.Extensions.Distances.DistanceFromCall);})
	    .attr('cy', function(dat) {return yScale(dat.MonitoredVehicleJourney.Bearing);})

	buses.enter()
	    .append('circle')
	    .attr('r', function(dat) {return sScale(dat.MonitoredVehicleJourney.MonitoredCall.Extensions.Distances.CallDistanceAlongRoute);})
	    .attr('cx', function(dat) {return xScale(dat.MonitoredVehicleJourney.MonitoredCall.Extensions.Distances.DistanceFromCall);})
	    .attr('cy', function(dat) {return yScale(dat.MonitoredVehicleJourney.Bearing);})
	    .attr('fill', color)
	    .attr('class', 'buses')
	    .attr('stroke', 'black')
	    .on("mouseover", function(dat) {
		infot.text(dat.MonitoredVehicleJourney.VehicleRef);
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
