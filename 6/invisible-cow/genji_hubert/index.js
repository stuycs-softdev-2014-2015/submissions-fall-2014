var handleMousePos = function(e) {
	console.log("x: "+ e.clientX + "\ty: " + e.clientY);
}

window.addEventListener("mousemove", handleMousePos);
