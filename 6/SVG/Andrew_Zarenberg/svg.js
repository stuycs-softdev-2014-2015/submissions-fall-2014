var draw = !location.href.match(/\?/);
var t = 0;
//var r=68,g=68,b=68;
var r=255,g=255,b=255;

var stick;
var fadeToBlack;
var wreckingBallItem;
var faces = [];


var lyricsX = 450, lyricsY = 50;
var lyricsItem;
var lyrics = [
	      ["We clawed, we chained",590,730],
	      ["Our hearts in vain",730,820],
	      ["We jumped, never asking why",820,1070],
	      ["We kissed, I fell under your spell",1070,1300],
	      ["A love no one could deny",1300,1600],
	      ["Don't you ever say I just walked away",1600,1800],
	      ["I will always want you",1800,2060],
	      ["I can't live a lie, running for my life",2060,2300],
	      ["I will always want you",2300,2420],
	      ["I",2600,2615],
	      ["CAME",2615,2630],
	      ["IN",2630,2645],
	      ["LIKE",2645,2660],
	      ["A",2660,2680],
	      ["WRECKING BALL",2680,2820],
	      ["I never hit so hard in love",2820,3070],
	      ["All I wanted was to break your walls",3070,3310],
	      ["All you ever did was",3310,3460],
	      ["Wre",3460,3480],
	      ["-e",3480,3500],
	      ["-eck me",3500,3620]
	       ];

var createSVG = function(elm,attr){
    var a = document.createElementNS("http://www.w3.org/2000/svg",elm);
    for(var x=0;x<attr.length;x+=2){
	a.setAttribute(attr[x],attr[x+1]);
    }
    return a;
};    


var wreckingBall = function(x,y,rot){
    return {
	x:x,
	y:y,
	chainWidth:6,
	chainHeight:14,
	ballRadius:100,
	ballCenterX:-1,
	ballCenterY:-1,
	rot:rot,
	mom:0,
	speed:0,
	person:"",
	generate:function(){
	    var curX = x, curY = y, a;

	    for(var z=0;z<16;z++){
		if(z != 0){
		    a = createSVG("rect",[
			"class","wrecking-ball chain",
			"x",curX-this.chainWidth/2,
			"y",curY,
			"width",this.chainWidth,
			"height",this.chainHeight
		    ]);
		    document.getElementById("s").appendChild(a);
		}

		a = createSVG("line",[
		    "class","wrecking-ball chain",
		    "x1",curX,
		    "y1",curY+this.chainHeight*2/3,
		    "x2",curX,
		    "y2",curY+this.chainHeight*(1/2+4/3)
		]);
		document.getElementById("s").appendChild(a);

		curY += this.chainHeight*3/2;
	    }
	    a = createSVG("circle",[
		"class","wrecking-ball",
		"cx",curX,
		"cy",curY+this.ballRadius,
		"r",this.ballRadius
	    ]);
	    this.ballCenterX = curX;
	    this.ballCenterY = curY+this.ballRadius;
	    document.getElementById("s").appendChild(a);
	    this.rotate(0);
	},

	generatePerson:function(){
	    var bx = this.ballCenterX, by = this.ballCenterY;
	    var a = createSVG("line",[
		"class","wrecking-ball ball-person",
		"x1",bx-43,
		"y1",by-110,
		"x2",bx+47,
		"y2",by-110,
		"stroke-width",20
	    ]);
	    document.getElementById("s").appendChild(a);

	    a = createSVG("line",[
		"class","wrecking-ball ball-person",
		"x1",bx-110,
		"y1",by-44,
		"x2",bx-38,
		"y2",by-114,
		"stroke-width",16
	    ]);
	    document.getElementById("s").appendChild(a);

	    a = createSVG("path",[
		"class","wrecking-ball ball-person",
		"d","M"+(bx+40)+","+(by-96)+" C"+(bx+80)+","+(by-206)+" "+(bx+90)+","+(by-206)+" "+(bx+140)+","+(by-226),
		"stroke-width",30
	    ]);
	    document.getElementById("s").appendChild(a);


	    a = createSVG("line",[
		"class","wrecking-ball ball-person",
		"x1",bx+80,
		"y1",by-200,
		"x2",bx-20,
		"y2",by-230,
		"stroke-width",12
	    ]);
	    document.getElementById("s").appendChild(a);

	    a = createSVG("g",[
		"class","wrecking-ball",
		"x",518,
		"y",200
	    ]);

	    this.person.setAttribute("x",bx+100);
	    this.person.setAttribute("y",by-300);
	    this.person.setAttribute("transform","rotate(60 "+(bx+90+this.person.getAttribute("width")/2)+" "+(by-300+this.person.getAttribute("y")/2)+")");
	    var tmpG = createSVG("g",["class","wrecking-ball"]);
	    tmpG.innerHTML = this.person.parentNode.innerHTML;
	    this.person.parentNode.parentNode.appendChild(tmpG);

	},

	rotate:function(n){
	    this.rot += n;
	    var a = document.querySelectorAll(".wrecking-ball");
	    for(var x=0;x<a.length;x++){
		a[x].setAttribute("transform","rotate("+this.rot+" "+this.x+" "+(this.y+10)+")");
	    }
	},

	release:function(sp){
	    this.speed = sp;
	},

	move:function(){
	    var n = Math.abs(this.rot)-Math.pow(Math.sqrt(Math.abs(this.rot))-this.speed/40000.0,2);
	        
	    if(this.rot%360 > 0) n = -n;
	        this.mom += n

	    if(this.mom > 0) this.mom -= this.speed/20000.0;
	    else this.mom += this.speed/20000.0;
	        
	    this.rotate(this.mom);
	},

	setPerson:function(n){
	    this.person = document.getElementById(n);
	}
    };
};


var face = function(x,y,w,h,img){
    return {
	x:x,
	y:y,
	width:w,
	height:h,
	leftEye:w/3,
	rightEye:w*2/3,
	eyeY:h/2,
	img:document.getElementById(img),
	mode:0,
	tear:0,
	dh:0,
	dw:0,
	stopZoom:-1,
	
	setEyes:function(left,right,height){
	    this.leftEye = left;
	    this.rightEye = right;
	    this.eyeY = height;
	},
	
	generate:function(){
	    this.img.setAttribute("x",this.x);
	    this.img.setAttribute("y",this.y);
	    this.img.setAttribute("width",this.width);
	    this.img.setAttribute("height",this.height);
	    this.tear = tear(this.x+this.leftEye,this.y+this.eyeY,500);
	    this.tear.y = 5000;
	    this.tear.generate();
	},

	center:function(){
	    this.x = 450-this.width/2;
	    this.y = 300-this.height/2;
	    //this.img.setAttribute("x",450-this.img.getAttribute("width")/2);
	    //this.img.setAttribute("y",300-this.img.getAttribute("height")/2);
	},

	zoom:function(a,b){
	    this.mode = 1;
	    this.dw = this.width*(a-1.0)/b;
	    this.dh = this.height*(a-1.0)/b;
	    this.stopZoom = t+b;
	},

	cry:function(eye,callback){
	    if(eye) this.tear.x = this.x+this.rightEye;
	    else this.x+this.leftEye;
	    this.tear.y = this.y+this.eyeY;
	    this.tear.cryCallback = callback;
	},

	move:function(){
	    if(this.mode == 1){ // zoom
		this.height += this.dh;
		this.y -= this.dh/2;
		this.img.setAttribute("height",this.height);
		
		this.width += this.dw;
		this.x -= this.dw/2;
		this.img.setAttribute("width",this.width);

		if(this.stopZoom <= t) this.mode = 0;
	    } else if(this.mode == 2){ // cry
		this.tear.move();
	    }

	    this.img.setAttribute("x",this.x);
	    this.img.setAttribute("y",this.y);
	}
    }
}

var tear = function(x,y,killY){
    return {
	x:x,
	y:y,
	height:20,
	width:10,
	killY:killY,
	cryCallback:null,
	
	generate:function(){
	    var a = createSVG("ellipse",[
		"id","tear",
		"cx",this.x,
		"cy",this.y,
		"rx",this.width,
		"ry",this.height
	    ]);
	    document.getElementById("s").appendChild(a);
	},

	move:function(){
	    this.y += .4;
	    
	    if(this.y >= this.killY){
		this.y = 5000;
		if(typeof this.cryCallback == "function") this.cryCallback();
	    }
	    document.getElementById("tear").setAttribute("cx",this.x);
	    document.getElementById("tear").setAttribute("cy",this.y);
	},
    }
};


var stickFigure = function(x,y,img){
    return {
	x:x,
	y:y,
	dr:1.2,
	imgX:-1,
	imgY:-1,
	rot:5,
	curLeg:false,
	height:140,
	img:document.getElementById(img),
	leftLeg:-50,
	rightLeg:50,
	leftArm:[[-65,30],[-25,70]],
	rightArm:[[65,40],[25,-25]],
	
	generate:function(){

	    stickLine(this.x,this.y-this.height/2+10,this.x,this.y+this.height/2,50); // body
	    stickLine(this.x-12,this.y+this.height/2-10,this.x+this.leftLeg,this.y+this.height,20); // left leg
	    stickLine(this.x+12,this.y+this.height/2-10,this.x+this.rightLeg,this.y+this.height,20); // right leg
	    
	    // left arm
	    stickLine(this.x-12,this.y-this.height/4,this.x-12+this.leftArm[0][0],this.y-this.height/4+this.leftArm[0][1],12);
	    stickLine(this.x-12+this.leftArm[0][0],this.y-this.height/4+this.leftArm[0][1],this.x-12+this.leftArm[1][0],this.y-this.height/4+this.leftArm[1][1],12);

	    // right arm
	    stickLine(this.x+12,this.y-this.height/4,this.x+12+this.rightArm[0][0],this.y-this.height/4+this.rightArm[0][1],12);
	    stickLine(this.x+12+this.rightArm[0][0],this.y-this.height/4+this.rightArm[0][1],this.x+12+this.rightArm[1][0],this.y-this.height/4+this.rightArm[1][1],12);

	    // hammer
	    var a = createSVG("line",[
				      "class","stick-figure",
				      "x1",this.x-12+this.leftArm[1][0]-25,
				      "y1",this.y-this.height/4+this.leftArm[1][1]+10,
				      "x2",this.x+12+this.rightArm[1][0]+25,
				      "y2",this.y-this.height/4+this.rightArm[1][1]-10,
				      "stroke","#F79F81",
				      "stroke-width",10
				      ]);
	    document.getElementById("s").appendChild(a);

	    a = createSVG("line",[
				  "class","stick-figure",
				  "x1",this.x+12+this.rightArm[1][0]+10,
				  "y1",this.y-this.height/4+this.rightArm[1][1]-35,
				  "x2",this.x+12+this.rightArm[1][0]+45,
				  "y2",this.y-this.height/4+this.rightArm[1][1]+10,
				  "stroke","#cccccc",
				  "stroke-width",20
				  ]);
	    document.getElementById("s").appendChild(a);

	    this.imgX = this.x-this.img.getAttribute("width")/2;
	    this.imgY = this.y-this.height/2-this.img.getAttribute("height")+20;
	    this.img.setAttribute("x",this.imgX);
	    this.img.setAttribute("y",this.imgY);

	    this.img.parentNode.appendChild(this.img);
	},

	move:function(){
	    this.rot += this.dr;
	    if(Math.abs(this.rot) >= 35) this.dr = -this.dr;

	    this.img.setAttribute("transform","rotate("+this.rot+" "+this.x+" "+(this.y-this.height/2+20)+")");
	}
    }
};


var stickLine = function(x1,y1,x2,y2,stroke){
    a = createSVG("line",[
			  "class","stick-figure",
			  "x1",x1,
			  "y1",y1,
			  "x2",x2,
			  "y2",y2,
			  "stroke-width",stroke,
			  "stroke","#F6E3CE"
			  ]);
    document.getElementById("s").appendChild(a);
}

			     
	    



var animloop = function(){


    if(lyrics.length && t > lyrics[0][1]){
	
	lyricsItem.innerHTML = lyrics[0][0];
	if(t >= 2600 && t < 2680) lyricsItem.setAttribute("x",lyricsX-lyrics[0][0].length*60);
	else if(t >= 2680 && t <= 2820) lyricsItem.setAttribute("x",100);
	else lyricsItem.setAttribute("x",lyricsX-lyrics[0][0].length*11);

	if(t >= lyrics[0][2]){
	    lyrics.shift();
	    lyricsItem.innerHTML = "";
	}
    }

    if(t >= 1600){
	document.getElementById("s").style.background = "rgb("+r+","+g+","+b+")";
	if(fadeToBlack){
	    if(r > 0) r-=2;
	    if(g > 0) g-=2;
	    if(b > 0) b-=2;
	} else if(draw){
	    r = (r+Math.floor(Math.random()*6)-2)%255;
	    g = (g+Math.floor(Math.random()*6)-2)%255;
	    b = (b+Math.floor(Math.random()*6)-2)%255;
	    if(r < 40) r = 42;
	    if(g < 40) g = 42;
	    if(b < 40) b = 42;
	}
    }

    if(t == 620){
	faces[0].mode = 2;
	faces[0].cry(false,function(){
		setTimeout(function(){
			faces[0].cry(true);
		    },200);
	    });
	
    } else if(t == 1600){
	for(var x=0;x<faces.length;x++){
	    faces[x].y = 5000;
	}

	stick = stickFigure(400,300,"zzz");
	stick.generate();
	
    } else if(t == 2450){
	var a = document.querySelectorAll(".stick-figure");
	for(var x=0;x<a.length;x++){
	    a[x].parentNode.removeChild(a[x]);
	};

	fadeToBlack = true;
    } else if(t == 2598){
	lyricsItem.setAttribute("font-size","200px");
	lyricsItem.setAttribute("y","300");
	lyricsItem.setAttribute("fill","#FFFF00");
    } else if(t == 2680){
	lyricsItem.setAttribute("font-size","90px");
	lyricsItem.setAttribute("y","450");
	fadeToBlack = false;
	r = g = b = 255;

	wreckingBall.generate();
	wreckingBall.generatePerson();
	wreckingBall.release(10);
    } else if(t == 2820){
	lyricsItem.setAttribute("font-size","50px");
	lyricsItem.setAttribute("fill","#ffffff");
	lyricsItem.setAttribute("y","550");
    }



    for(var x=0;x<faces.length;x++){
	faces[x].move();
    }
    if(stick) stick.move();

    wreckingBall.move();

    t++;
    document.getElementById("timer").innerHTML = t;
    window.requestAnimationFrame(animloop);
};


lyricsItem = createSVG("text",[
			       "x",lyricsX,
			       "y",lyricsY,
			       "fill","#ffffff",
			       "stroke","#000000",
			       "stroke-width",2,
			       "font-size","50px",
			       "font-family","Arial"
			       ]);
document.getElementById("s").appendChild(lyricsItem);
			       

wreckingBall = wreckingBall(400,-10,-90);
wreckingBall.setPerson("zz");
wreckingBall.move();

bigText = createSVG("text",[
    "id","bigText",
    "x",0,
    "y",0,
    "fill","#000000"
]);
    

window.requestAnimationFrame(animloop);

var fa = face(50,0,310,450,"z");
faces.push(fa);
fa.setEyes(fa.leftEye-30,fa.rightEye+85,fa.eyeY+120);
fa.center();
fa.generate();
fa.move();
fa.zoom(1.4,600);



