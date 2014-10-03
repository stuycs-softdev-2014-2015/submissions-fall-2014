var data = "";
var key = "";
var freq = {};
var freqt= {};
function getData(){
    console.log("runing getData()");
    var url = "https://data.cityofnewyork.us/resource/4vkw-7nck.json";
    var d = d3.csv("data.csv",function(error,csv){
	if (error) return console.log(error); 
	else{
	    data = csv;
	    k();
	}
    });
    var k = function(){
	d3.csv("Cuisine.csv",function(error,csv){
	    if (error) return console.log(error);
	    else{
		key = csv;
		org();
	    }
	});
    }

    var org = function(){
	console.log("running org");
	var TYPES = {};
	for (var i in key){
	    var code = key[i].CUISINECODE;
	    TYPES[code] = key[i].CODEDESC;
	}
	freqt.scr = 0;
	freqt.lowest = parseInt(data[0].SCORE);
	freqt.A = 0;
	freqt.B = 0;
	freqt.C = 0;
	for(var i = 0;i<data.length;i++){
//	for(var i = 0;i<1;i++){
	    var gr = data[i].CURRENTGRADE;
	    var rating = parseInt(data[i].SCORE);	    
	    var type = TYPES[data[i].CUISINECODE];
	    if (gr==="A" || gr==="B" || gr==="C"){
		freqt[gr] = freqt[gr]+1; }
	    if (rating > freqt.scr) {
		freqt.scr = rating;
	    }
	    else if (rating < freqt.lowest){
		freqt.lowest = rating;
	    }
	    if (Object.keys(freq).indexOf(type) < 0){
		freq[type] = [];		
		freq[type].n = type;
		freq[type].A = 0;
		freq[type].B= 0;
		freq[type].C = 0;
		freq[type].scr = rating;		
	    }
	    
	    if (gr==="A" || gr==="B" || gr==="C"){
		freq[type][gr] = freq[type][gr] + 1;
	    }
	    
	    if (!isNaN(rating)){
		freq[type].scr = (freq[type].scr + rating)/2;
	    }
	    
	}
	console.log("out of loop");
	setup();
    };    

    var setup = function (){
	console.log("in setup");
	var world = d3.select("#world");
	var svg = world.append("svg").attr('width','600').attr('height','200');
	var grdA = svg.append("rect").attr("width","500").attr("height",'25')
	    .attr("x","10").attr("y","20").attr("fill","white")
	    .attr("stroke","black");
	var grdB = svg.append("rect").attr("width","500").attr("height",'25')
	    .attr("x","10").attr("y","65").attr("fill","white")
	    .attr("stroke","black");
	
	var grdC = svg.append("rect").attr("width","500").attr("height",'25')
	    .attr("x","10").attr("y","110").attr("fill","white")
	    .attr("stroke","black");
	var scr = svg.append("rect").attr("width","500").attr("height",'25')
	    .attr("x","10").attr("y","155").attr("fill","white")
	    .attr("stroke","black");
	var A = svg.append("text").text("Grade A").attr("x","525").attr("y","40")
	    .attr("font-size","20px");
	var B = svg.append("text").text("Grade B").attr("x","525").attr("y","85")
	    .attr("font-size","20px");
	var C = svg.append("text").text("Grade C").attr("x","525").attr("y","130")
	    .attr("font-size","20px");
	var S = svg.append("text").text("Score").attr("x","525").attr("y","175")
	    .attr("font-size","20px");
	
	/**********************************************************************/
	var getAX = getX("A");
	var barA = svg.selectAll(".A").data(d3.entries(freq)).enter().append("rect").attr("class","A").attr("y","21").attr("x",function(d){return getAX(d);}).attr("width",function(d){return getW(d,"A");}).attr("height","23").attr("fill",function(){return rC();});

	var getBX = getX("B");
	var barB = svg.selectAll(".B").data(d3.entries(freq)).enter().append("rect").attr("class","B").attr("y","66").attr("x",function(d){return getBX(d);}).attr("width",function(d){return getW(d,"B");}).attr("height","23").attr("fill",function(){return rC()});

	var getCX = getX("C");
	var barC = svg.selectAll(".C").data(d3.entries(freq)).enter().append("rect").attr("class","C").attr("y","111").attr("x",function(d){return getCX(d);}).attr("width",function(d){return getW(d,"C");}).attr("height","23").attr("fill",function(){return rC();});

	var getSX = getX("scr");
	var barS = svg.selectAll(".S").data(d3.entries(freq)).enter().append("line").attr("class","S").attr("y1","156").attr("x1",function(d){return sX(d);}).attr("x2",function(d){return sX(d);}).attr("stroke-width","1").attr("y2","179").attr("stroke",function(){return rC();});
	
    };        
    
    var sX = function(d){
	var r = d.value.scr;
	if(!isNaN(r)){
	    return (r/freqt.scr)*500;
	}
	return freqt.scr;
    }
    
    function rC() {
	var letters = '0123456789ABCDEF'.split('');
	var color = '#';
	for (var i = 0; i < 6; i++ ) {
            color += letters[Math.floor(Math.random() * 16)];
	}
	return color;
    };

    var getW = function(d,n){
	var ans = Math.floor((d.value[n] / freqt[n])*500);
	return ans;
    }
    
    var getX = function(z){
	var x = 10;
	var inner = function(n){
	    var old = x;
	    var delta = Math.floor((n.value[z] / freqt[z])*500);
	    x = x + delta;
	    return old;
	}
	return inner;
    }

    

}


getData();

