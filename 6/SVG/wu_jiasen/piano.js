var r1 = document.createElementNS("http://www.w3.org/2000/svg","rect");
r1.setAttribute('id','r1');
r1.setAttribute('width',100);
r1.setAttribute('height',300);
r1.setAttribute('x',0);
r1.setAttribute('rx',10);
r1.setAttribute('ry',10);
r1.setAttribute('fill','white');
r1.setAttribute('stroke','black');

var r2 = document.createElementNS("http://www.w3.org/2000/svg","rect");
r2.setAttribute('id','r2');
r2.setAttribute('width',100);
r2.setAttribute('height',300);
r2.setAttribute('x',100);
r2.setAttribute('rx',10);
r2.setAttribute('ry',10);
r2.setAttribute('fill','white');
r2.setAttribute('stroke','black');

var r3 = document.createElementNS("http://www.w3.org/2000/svg","rect");
r3.setAttribute('id','r3');
r3.setAttribute('width',100);
r3.setAttribute('height',300);
r3.setAttribute('x',200);
r3.setAttribute('rx',10);
r3.setAttribute('ry',10);
r3.setAttribute('fill','white');
r3.setAttribute('stroke','black');

var r4 = document.createElementNS("http://www.w3.org/2000/svg","rect");
r4.setAttribute('id','r4');
r4.setAttribute('width',100);
r4.setAttribute('height',300);
r4.setAttribute('x',300);
r4.setAttribute('rx',10);
r4.setAttribute('ry',10);
r4.setAttribute('fill','white');
r4.setAttribute('stroke','black');

var r5 = document.createElementNS("http://www.w3.org/2000/svg","rect");
r5.setAttribute('id','r5');
r5.setAttribute('width',100);
r5.setAttribute('height',300);
r5.setAttribute('x',400);
r5.setAttribute('rx',10);
r5.setAttribute('ry',10);
r5.setAttribute('fill','white');
r5.setAttribute('stroke','black');

var r6 = document.createElementNS("http://www.w3.org/2000/svg","rect");
r6.setAttribute('id','r6');
r6.setAttribute('width',100);
r6.setAttribute('height',300);
r6.setAttribute('x',500);
r6.setAttribute('rx',10);
r6.setAttribute('ry',10);
r6.setAttribute('fill','white');
r6.setAttribute('stroke','black');

var r7 = document.createElementNS("http://www.w3.org/2000/svg","rect");
r7.setAttribute('id','r7');
r7.setAttribute('width',100);
r7.setAttribute('height',300);
r7.setAttribute('x',600);
r7.setAttribute('rx',10);
r7.setAttribute('ry',10);
r7.setAttribute('fill','white');
r7.setAttribute('stroke','black');

var rt1 = document.createElementNS("http://www.w3.org/2000/svg","rect");
rt1.setAttribute('id','rt1');
rt1.setAttribute('width',50);
rt1.setAttribute('height',200);
rt1.setAttribute('x',75);
rt1.setAttribute('rx',5);
rt1.setAttribute('ry',5);
rt1.setAttribute('stroke','black');

var rt2 = document.createElementNS("http://www.w3.org/2000/svg","rect");
rt2.setAttribute('id','rt2');
rt2.setAttribute('width',50);
rt2.setAttribute('height',200);
rt2.setAttribute('x',175);
rt2.setAttribute('rx',5);
rt2.setAttribute('ry',5);
rt2.setAttribute('stroke','black');

var rt3 = document.createElementNS("http://www.w3.org/2000/svg","rect");
rt3.setAttribute('id','rt3');
rt3.setAttribute('width',50);
rt3.setAttribute('height',200);
rt3.setAttribute('x',375);
rt3.setAttribute('rx',5);
rt3.setAttribute('ry',5);
rt3.setAttribute('stroke','black');

var rt4 = document.createElementNS("http://www.w3.org/2000/svg","rect");
rt4.setAttribute('id','rt4');
rt4.setAttribute('width',50);
rt4.setAttribute('height',200);
rt4.setAttribute('x',475);
rt4.setAttribute('rx',5);
rt4.setAttribute('ry',5);
rt4.setAttribute('stroke','black');

var rt5 = document.createElementNS("http://www.w3.org/2000/svg","rect");
rt5.setAttribute('id','rt5');
rt5.setAttribute('width',50);
rt5.setAttribute('height',200);
rt5.setAttribute('x',575);
rt5.setAttribute('rx',5);
rt5.setAttribute('ry',5);
rt5.setAttribute('stroke','black');

var clicked = function(e) {
	console.log('test');
}

var s = document.getElementById("keyboard");
s.appendChild(r1);
s.appendChild(r2);
s.appendChild(r3);
s.appendChild(r4);
s.appendChild(r5);
s.appendChild(r6);
s.appendChild(r7);
s.appendChild(rt1);
s.appendChild(rt2);
s.appendChild(rt3);
s.appendChild(rt4);
s.appendChild(rt5);
r1.addEventListener("click",clicked);
r2.addEventListener("click",clicked);
r3.addEventListener("click",clicked);
r4.addEventListener("click",clicked);
r5.addEventListener("click",clicked);
r6.addEventListener("click",clicked);
r7.addEventListener("click",clicked);