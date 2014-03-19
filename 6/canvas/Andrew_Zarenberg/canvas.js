var c = document.getElementById("c");
var ctx = c.getContext("2d");
ctx.font = "40px Arial";
var heads = [];

var START_TIME = 250,
REPEAT_TIME = 2400;
var t = 0;

var r=68,g=68,b=68;

var car = document.createElement("img");
car.src = "car.png";

var carDisplay = true;


var lyrics = [
    ["What is Love?",200,320],
    ["Yeah ahh",700,820],
    ["Ohhhh ohh",1030,1150],
    ["I don't know, why you're not there",1230,1450],
    ["I give you my love, but you don't care",1450,1690],
    ["So what is right and what is wrong",1690,1900],
    ["Give a sign",1920,2070],
    ["What is love?",2070,2170],
    ["Baby don't hurt me",2170,2300],
    ["Don't hurt me",2300,2400],
    ["No more",2400,2550]
];

var titles = [
    ["10:00 PM","",250,400],
    ["The Club","10:20 PM",850,1000],
    ["10:45 PM","",2350,2500]
];

var animloop = function(){


    //ctx.fillStyle = "#444444";
    ctx.fillStyle = "rgb("+r+","+g+","+b+")";
    r = (r+Math.floor(Math.random()*6)-2)%255;
    g = (g+Math.floor(Math.random()*6)-2)%255;
    b = (b+Math.floor(Math.random()*6)-2)%255;
    if(r < 40) r = 42;
    if(g < 40) g = 42;
    if(b < 40) b = 42;
    ctx.fillRect(0,0,900,600);
    
    if(carDisplay) ctx.drawImage(car,130,80);

    for(var x=0;x<heads.length;x++){
	if(t > START_TIME) heads[x].move();
	heads[x].draw();
    }


    if(titles.length && t > titles[0][2]){
	ctx.fillStyle = "#ffffff";
	ctx.fillText(titles[0][0],400-titles[0][0].length*5,540);
	ctx.fillText(titles[0][1],400-titles[0][1].length*5,590);
	ctx.lineWidth = 1;
	ctx.strokeStyle = "#000000";
	ctx.strokeText(titles[0][0],400-titles[0][0].length*5,540);
	ctx.strokeText(titles[0][1],400-titles[0][1].length*5,590);
	if(t == titles[0][3]) titles.shift();
    }

    if(lyrics.length && t > lyrics[0][1]){
	ctx.fillStyle = "#ffff00";
	ctx.fillText(lyrics[0][0],350-lyrics[0][0].length*5,60);
	ctx.lineWidth = 1;
	ctx.strokeStyle = "#000000";
	ctx.strokeText(lyrics[0][0],350-lyrics[0][0].length*5,60);
	if(t == lyrics[0][2]) lyrics.shift();
    }

//    document.getElementById("timer").innerHTML = t;
    t++;

    if(t%REPEAT_TIME == 850){
	carDisplay = false;
	for(var x=0;x<heads.length;x++) heads[x].mode = 2;
    } else if(t%REPEAT_TIME == 1150){
	for(var x=0;x<heads.length;x++) heads[x].mode = 3;
    } else if(t%REPEAT_TIME == 1400){
	for(var x=0;x<heads.length;x++) heads[x].moveDir = -1;
    } else if(t%REPEAT_TIME == 1650){
	for(var x=0;x<heads.length;x++) heads[x].mode = 2;
    } else if(t%REPEAT_TIME == 1750){
	for(var x=0;x<heads.length;x++) heads[x].mode = 3;
    } else if(t%REPEAT_TIME == 2000){
	for(var x=0;x<heads.length;x++) heads[x].moveDir = 1;
    } else if(t%REPEAT_TIME == 2250){
	for(var x=0;x<heads.length;x++) heads[x].mode = 2;
    } else if(t%REPEAT_TIME == 2350){
	carDisplay = true;
	for(var x=0;x<heads.length;x++) heads[x].mode = 1;
    }

    window.requestAnimationFrame(animloop);
}


var head = function(x,y,w,h,img,ctx){
    /* mode:
     * 1 = head only
     * 2 = stick figure, arms moving
     * 3 = stick figure, arms moving, walking
     */

    var temp = document.createElement("img");
    temp.src = img;

    return {
	mainX:x,
	mainY:y,
	leftLeg:-40,
	rightLeg:40,
	legMove:true,
	moveDir:1,
	x:x,
	y:y,
	w:w,
	h:h,
	headRotate:0,
	img:temp,
	mode:1,
	ctx:ctx,

	draw:function(){


	        // stick figure mode
	    if(this.mode == 2 || this.mode == 3){
		ctx.lineWidth = 10;
		ctx.strokeStyle = "#ffffff";
		ctx.beginPath();
		var xx = this.mainX+this.w/2,
		yy = this.mainY+this.h;
		ctx.moveTo(this.x+this.w/2,this.y+this.h);
		ctx.lineTo(xx,yy+20);
		ctx.lineTo(xx,yy+140); // body
		ctx.lineTo(xx+this.leftLeg,yy+220); // left leg
		ctx.moveTo(xx,yy+140); // right leg
		ctx.lineTo(xx+this.rightLeg,yy+220); // cont.

		ctx.moveTo(xx,yy+60); // left arm
		ctx.lineTo(xx-40+this.mainX-this.x,yy+20-this.mainY+this.y); // cont.
		ctx.moveTo(xx,yy+60); // right arm
		ctx.lineTo(xx+40-this.mainX+this.x,yy+20-this.mainY+this.y); // cont.
		ctx.stroke();
	    }
	        // draw head
	    var buffer = document.createElement("canvas");
	    buffer.height = buffer.width = 120;
	    var btx = buffer.getContext("2d");
	    btx.rotate(this.headRotate);
	    btx.drawImage(this.img,40,0);
	    ctx.drawImage(buffer,this.x-30,this.y);

        },
	move:function(){
	    var d = Math.sin((t-START_TIME)/4.6)*3;

            this.x += d*1.5;
            this.y += d/10;
	    this.headRotate += d/90;

	    if(this.mode == 3){
		if(this.legMove){
		    this.leftLeg += this.moveDir;
		    this.rightLeg -= this.moveDir;
		    if(Math.abs(this.leftLeg) >= 50) this.legMove = false;
		} else {
		    this.rightLeg += this.moveDir;
		    this.leftLeg -= this.moveDir;
		    if(Math.abs(this.rightLeg) >= 50) this.legMove = true;
		}
		this.x += this.moveDir;
		this.mainX += this.moveDir;
	    }

        },
    }
}

heads.push(head(280,120,70,90,"dw.jpg",ctx));
heads.push(head(505,120,62,90,"z.jpg",ctx));


window.requestAnimationFrame(animloop);

