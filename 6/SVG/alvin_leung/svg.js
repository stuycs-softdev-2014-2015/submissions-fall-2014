var draw = function(){
    var s = document.getElementById('svg');
    var namespace = "http://www.w3.org/2000/svg"
    var pen = document.createElementNS(namespace,"circle");
    pen.setAttribute('id','pen');
    pen.setAttribute('cx',0);
    pen.setAttribute('cy',0);
    pen.setAttribute('r',20);
    pen.setAttribute('stroke','#000000');
    pen.setAttribute('fill','#FFFFFF');
    s.appendChild(pen);
    var penDown = false;
    var oldMidPtX,oldMidPtY,oldPtX,oldPtY,midptX,midptY;

    var movePen = function(e){
	pen.setAttribute('cx',e.offsetX);
	pen.setAttribute('cy',e.offsetY);
	if(penDown){
	    midptX = oldMidPtX + e.offsetX>>1;
	    midptY = oldMidPtY + e.offsetY>>1;
	    var p = document.createElementNS(namespace,'path');
	    var path = 'M ' + oldPtX + ' ' + oldPtY + ' S ' + oldMidPtX + ' ' + oldMidPtY+ ' ' + midptX + ' ' + midptY;
	    console.log(path);
	    p.setAttribute('d',path);
	    p.setAttribute('stroke','#000000');
	    p.setAttribute('fill','none');
	    p.setAttribute('stroke-width',40);
	    s.appendChild(p);
	    oldMidPtX = midptX;
	    oldMidPtY = midptY;
	    oldPtX = e.offsetX;
	    oldPtY = e.offsetY;
	}
    }
    s.addEventListener('mousemove',movePen);
    s.addEventListener('mousedown',function(e){
	penDown = true;
	oldMidPtX = e.offsetX;
	oldMidPtY = e.offsetY;
	oldPtX = e.offsetX;
	oldPtY = e.offsetY;
    });
    s.addEventListener('mouseup',function(){penDown = false;});
}();
