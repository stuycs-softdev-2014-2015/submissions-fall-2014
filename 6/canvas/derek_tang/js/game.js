var g;
var THICK = 5, ELASTICITY = 0.1;
var isq2 = 1/Math.sqrt(2), dir = [[-1,0],[0,-1],[1,0],[0,1]];

var G = {
	m : [],
	cm : null,
	
	start : function() {
		g = document.getElementById("cv").getContext("2d");
		G.reset();
		P.reset();
		G.cm = "outside";
		G.loadMap("outside");
	},
	reset : function() {
		
	},
	
	loadMap : function(mapn) {
		var m = G.m[mapn] = new M();
		var map = maps[mapn];
		for(i in map.walls) {
			var w = map.walls[i];
			for(var j=2;j<w.length;j+=2) {
				var x1 = w[j-2], y1 = w[j-1], x2 = w[j], y2 = w[j+1];
				if (x1 > x2) {x1^=x2;x2^=x1;x1^=x2;}
				if (y1 > y2) {y1^=y2;y2^=y1;y1^=y2;}
				m.w.push({x:x1-THICK,y:y1-THICK,w:x2-x1+2*THICK,h:y2-y1+2*THICK});
			}
		}
		
		P.x = map.start.x;
		P.y = map.start.y;
	},
	
	step : function() {
		
		P.step();
		
	},
	draw : function() {
		g.clearRect(0,0,800,500);
		var offx = 400-P.x, offy = 250-P.y;
		g.translate(offx, offy);
		
		G.drawMap();
		
		P.draw();
		
		g.translate(-offx, -offy);
	},
	drawMap : function() {
		var m = G.m[G.cm];
		g.fillStyle = "rgb(0,0,0)";
		for(var i=0;i<m.w.length;i++) {
			g.fillRect(m.w[i].x,m.w[i].y,m.w[i].w,m.w[i].h);
		}
	}
	
	
};


$(function() {
	G.start();
	setInterval(function() {
		G.step();
		G.draw();
	});
});

function inBox(mx,my,x,y,w,h) {
	return mx>=x&&mx<=x+w&&my>=y&&my<=y+h;
}
function col(obj1x,obj1y,obj1w,obj1h,obj2x,obj2y,obj2w,obj2h) {
	return obj1x<=obj2x+obj2w&&obj1x>=obj2x-obj1w&&obj1y<=obj2y+obj2h&&obj1y>=obj2y-obj1h 
}
function col2(obj1x,obj1y,obj1w,obj1h,obj2x,obj2y,obj2w,obj2h) {
	return obj1x<obj2x+obj2w&&obj1x>obj2x-obj1w&&obj1y<obj2y+obj2h&&obj1y>obj2y-obj1h 
}
function DBP(x1,y1,x2,y2) {
	return Math.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1));
}
function testBounds(ox,oy,w,h,ovx,ovy) {
	x = ox, y = oy, vx = ovx, vy = ovy;
	we = ELASTICITY;
	var m = G.m[G.cm];
	for(var j=0;j<m.w.length;j++) {
		r = getResult(m.w[j].x,m.w[j].y,m.w[j].w,m.w[j].h,x,y,w,h,vx,vy);
		x = r[0]; y = r[1]; vx = r[2]; vy = r[3];
	}
	return {x:x,y:y,vx:vx,vy:vy};
}
function getResult(lx,ly,lw,lh,ox,oy,w,h,ovx,ovy) {
	var x=ox,y=oy,vx=ovx,vy=ovy;
	we = ELASTICITY;
	if (col(lx,ly,lw,lh,x,y,w,h)) {
		// GENERATE THE CLOSEST POINTS TO MOVE THE OBJECTS OUTSIDE
		pdes = [[lx-w/2,y+h/2,0],[lx+lw+w/2,y+h/2,2],
				[x+w/2,ly-h/2,1],[x+w/2,ly+lh+h/2,3]];
		dist=9999999; pdesi = -1;
		for(jkk in pdes) {
			pdis=DBP(x+w/2,y+h/2,pdes[jkk][0],pdes[jkk][1]);
			if (pdis < dist) {
				dist = pdis;
				pdesi = jkk;
			}
		}
		x = pdes[pdesi][0] - w/2;
		y = pdes[pdesi][1] - h/2;
		switch (pdes[pdesi][2]) {
			case 0: vx=-Math.abs(vx) *we; break;
			case 1: vy=-Math.abs(vy) *we; break;
			case 2: vx=Math.abs(vx) *we; break;
			case 3: vy=Math.abs(vy) *we; break;
		}
	}
	return [x,y,vx,vy];
}



