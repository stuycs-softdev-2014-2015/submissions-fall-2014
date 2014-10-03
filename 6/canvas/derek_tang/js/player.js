

var P = {
	reset : function() {
		P.x = 0;
		P.y = 0;
		P.vx = 0;
		P.vy = 0;
		P.speed = 0.14;
		P.speed = 0.34;
		P.friction = 0.91;
	},
	step : function() {
		var dir = [0,0];
		if (ak[0]) dir = [-1,0];
		if (ak[1]) dir = [0,-1];
		if (ak[2]) dir = [1,0];
		if (ak[3]) dir = [0,1];
		if (ak[0] && ak[1]) dir = [-isq2,-isq2];
		if (ak[1] && ak[2]) dir = [isq2,-isq2];
		if (ak[2] && ak[3]) dir = [isq2,isq2];
		if (ak[3] && ak[0]) dir = [-isq2,isq2];
		P.vx += dir[0] * P.speed;
		P.vy += dir[1] * P.speed;
		{
			var r = testBounds(P.x-20,P.y-20,40,40,P.vx,P.vy);
			P.vx = r.vx;
			P.vy = r.vy;
			P.x = r.x + 20;
			P.y = r.y + 20;
		}
		
		P.vx *= P.friction;
		P.vy *= P.friction;
		P.x += P.vx;
		P.y += P.vy;
	},
	draw : function() {
		g.fillStyle = "rgb(0,0,255)";
		g.fillRect(P.x-20,P.y-20,40,40);
	}
};







