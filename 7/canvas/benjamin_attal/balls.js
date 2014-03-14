
var cvs = document.getElementById("cvs"),
    ctx = cvs.getContext("2d"),
    ball_list = [];


function intersection(b1, b2) {
    "use strict";
    var x0 = b1.x, y0 = b1.y, r0 = b1.r, x1 = b2.x, y1 = b2.y, r1 = b2.r;

    var a, dx, dy, d, h, rx, ry;
    var x2, y2;

    /* dx and dy are the vertical and horizontal distances between
     * the circle centers.
     */
    dx = x1 - x0;
    dy = y1 - y0;

    /* Determine the straight-line distance between the centers. */
    d = Math.sqrt((dy * dy) + (dx * dx));

    /* Check for solvability. */
    if (d > (r0 + r1)) {
        /* no solution. circles do not intersect. */
        return false;
    }
    if (d < Math.abs(r0 - r1)) {
        /* no solution. one circle is contained in the other */
        return false;
    }

    /* 'point 2' is the point where the line through the circle
     * intersection points crosses the line between the circle
     * centers.  
     */

    /* Determine the distance from point 0 to point 2. */
    a = ((r0 * r0) - (r1 * r1) + (d * d)) / (2.0 * d);

    /* Determine the coordinates of point 2. */
    x2 = x0 + (dx * a / d);
    y2 = y0 + (dy * a / d);

    /* Determine the distance from point 2 to either of the
     * intersection points.
     */
    h = Math.sqrt((r0 * r0) - (a * a));

    /* Now determine the offsets of the intersection points from
     * point 2.
     */
    rx = -dy * (h / d);
    ry = dx * (h / d);

    /* Determine the absolute intersection points. */
    var xi = x2 + rx;
    var xi_prime = x2 - rx;
    var yi = y2 + ry;
    var yi_prime = y2 - ry;

    return [xi, xi_prime, yi, yi_prime];
}

var draw_ball = function () {
    "use strict";
    console.log(this);

    ctx.beginPath();
    ctx.arc(this.x, this.y, this.r, 0, 2 * Math.PI);
    ctx.fillStyle = "#ff0000";

    ctx.fill();
    ctx.stroke();
};

var move_ball = function () {
    "use strict";
    var i;

    for (i = 0; i < ball_list.length; i += 1) {
        var points, b2, dx, dy, d, center, theta, n_x, n_y, dx2, dy2, dx3, dy3;
        points = intersection(this, ball_list[i]);
        b2 = ball_list[i];

        if (points[0]) {
            // Update speeds and direction
            dx = this.x - b2.x;
            dy = this.y - b2.y;

            d = Math.sqrt((dy * dy) + (dx * dx));

            center = Math.acos(dx / d) * (dy > 0 ? 1 : -1);
            theta = (this.a - center);

            n_x = Math.cos(theta) * b2.v + Math.cos(this.a) * this.v;
            n_y = Math.sin(theta) * b2.v + Math.sin(this.a) * this.v;
            dx2 = n_x - points[0];
            dy2 = n_y - points[2];

            this.a = Math.atan(dy2 / dx2) * (dx2 > 0 ? 1 : -1);
            this.v = Math.sqrt((dy2 * dy2) + (dx2 * dx2));

            b2.a = Math.PI - b2.a;
        }

        if (this.x + this.r >= 600 || this.x - this.r <= 0) {
            this.a = Math.PI - this.a;
        }

        if (this.y + this.r >= 600 || this.y - this.r <= 0) {
            this.a *= -1;
        }

        this.v = Math.min(this.v, 1);

        this.x += Math.cos(this.a) * this.v;
        this.y += Math.sin(this.a) * this.v;
    }
};

var spawn_ball = function (x, y, r, a, v) {
    "use strict";

    return {
        'x': x,
        'y': y,
        'r': r,
        'a': a,
        'v': v,
        'draw': draw_ball,
        'move': move_ball
    };
};

var animloop = function () {
    "use strict";

    cvs.width = cvs.width;
    var i;
    for (i = 0; i < ball_list.length; i += 1) {
        ball_list[i].draw();
        ball_list[i].move();
    }

    window.requestAnimationFrame(animloop);
};

var clicked = function (e) {
    "use strict";

    ball_list.push(spawn_ball(e.offsetX, e.offsetY, 10, Math.random() * 100, 0.5));
};


ball_list.push(spawn_ball(50, 50, 10, 5, 0.5));
ball_list.push(spawn_ball(20, 80, 10, 100, 0.5));
ball_list.push(spawn_ball(500, 20, 10, 30, 1));
ball_list.push(spawn_ball(500, 40, 10, 20, 1));
ball_list.push(spawn_ball(500, 60, 10, 40, 1));
ball_list.push(spawn_ball(500, 80, 10, 50, 1));

cvs.addEventListener("click", clicked);

window.requestAnimationFrame(animloop);
