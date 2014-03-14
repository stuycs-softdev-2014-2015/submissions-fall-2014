var width, height;
var score, lives;
var ship, balls, shots;

function distance(a, b) {
    return Math.sqrt(Math.pow(a.x - b.x, 2) + Math.pow(a.y - b.y, 2));
}

function simulate_ship() {
    ship.x += ship.speed * Math.cos(ship.angle * Math.PI / 180);
    ship.y += ship.speed * Math.sin(ship.angle * Math.PI / 180);

    if (ship.x > width)     ship.x = 0;
    if (ship.x < 0)         ship.x = width;
    if (ship.y > height)    ship.y = 0;
    if (ship.y < 0)         ship.y = height;

    if (lives && !ship.invincibility) {
        for (var i = 0; i < balls.length; i++) {
            if (!balls[i].spawning && !balls[i].dying && distance(ship, balls[i]) < balls[i].size + 5) {
                balls[i].growing = balls[i].size;
                lives--;
                ship = {
                    x: width / 2,
                    y: height / 2,
                    angle: 270,
                    speed: 0,
                    cooldown: 0,
                    invincibility: 120
                };
            }
        }
    }

    if (ship.cooldown)
        ship.cooldown--;
    if (ship.invincibility)
        ship.invincibility--;
}

function simulate_shot(shot) {
    shot.x += shot.speed * Math.cos(shot.angle * Math.PI / 180);
    shot.y += shot.speed * Math.sin(shot.angle * Math.PI / 180);

    for (var i = 0; i < balls.length; i++) {
        if (!balls[i].spawning && !balls[i].dying && distance(shot, balls[i]) < balls[i].size + 5) {
            balls[i].dying = true;
            return false;
        }
    }

    if (shot.x > width || shot.x < 0 || shot.y > height || shot.y < 0)
        return false;
    return true;
}

function simulate_ball(ball) {
    ball.x += ball.speed * Math.cos(ball.angle * Math.PI / 180);
    ball.y += ball.speed * Math.sin(ball.angle * Math.PI / 180);

    if (ball.x > width)     ball.x = 0;
    if (ball.x < 0)         ball.x = width;
    if (ball.y > height)    ball.y = 0;
    if (ball.y < 0)         ball.y = height;

    if (ball.dying) {
        ball.size--;
        score++;
        if (ball.size < 1)
            return false;
    }
    if (ball.growing > 1) {
        ball.size++;
        ball.growing--;
    }
    if (ball.spawning)
        ball.spawning--;
    return true;
}

function spawn_ball() {
    balls.push({
        x: Math.random() * width,
        y: Math.random() * height,
        size: Math.random() * 20 + 10,
        angle: Math.random() * 360,
        speed: Math.random() * 1 + 0.5,
        spawning: 30,
        dying: false
    });
}

function clear(ctx) {
    ctx.fillStyle = "white";
    ctx.fillRect(0, 0, width, height);
}

function draw_ball(ctx, ball) {
    ctx.save();

    ctx.beginPath();
    ctx.arc(ball.x, ball.y, ball.size, 0, 2 * Math.PI);

    if (ball.dying)
        ctx.fillStyle = "rgb(255, 225, 225)";
    else if (ball.growing > 1)
        ctx.fillStyle = "rgb(255, 150, 150)";
    else
        ctx.fillStyle = "rgb(255, " + (200 * (30 - ball.spawning) / 30) + ", " + (200 * (30 - ball.spawning) / 30) + ")";
    ctx.fill();
    ctx.strokeStyle = "#F00";
    ctx.stroke();
    ctx.restore();
}

function draw_shot(ctx, shot) {
    ctx.save();
    ctx.translate(shot.x, shot.y);
    ctx.rotate(shot.angle * Math.PI / 180);
    ctx.translate(-shot.x, -shot.y);

    ctx.beginPath();
    ctx.rect(shot.x - 8, shot.y - 1, 16, 2);

    ctx.fillStyle = "#080";
    ctx.fill();
    ctx.strokeStyle = "#040";
    ctx.stroke();
    ctx.restore();
}

function draw_ship(ctx) {
    ctx.save();
    ctx.translate(ship.x, ship.y);
    ctx.rotate(ship.angle * Math.PI / 180);
    ctx.translate(-ship.x, -ship.y);

    ctx.beginPath();
    ctx.moveTo(ship.x - 15, ship.y - 10);
    ctx.lineTo(ship.x - 15, ship.y + 10);
    ctx.lineTo(ship.x + 15, ship.y);
    ctx.closePath();

    ctx.fillStyle = "#6DD";
    ctx.fill();
    ctx.strokeStyle = "#0AA";
    ctx.stroke();
    ctx.restore();
}

function step(ctx) {
    // Do logic
    simulate_ship();
    for (var i = 0; i < shots.length; i++) {
        if (!simulate_shot(shots[i])) {
            shots.splice(i, 1);
            i--;
        }
    }
    for (var i = 0; i < balls.length; i++) {
        if (!simulate_ball(balls[i])) {
            balls.splice(i, 1);
            i--;
        }
    }
    if (Math.random() < 0.02)
        spawn_ball();

    // Render state to canvas
    clear(ctx);
    for (var i = 0; i < balls.length; i++)
        draw_ball(ctx, balls[i]);
    for (var i = 0; i < shots.length; i++)
        draw_shot(ctx, shots[i]);
    if (lives && !((ship.invincibility / 4) % 2))
        draw_ship(ctx);
    ctx.fillStyle = "black";
    ctx.font = "16px monospace";
    ctx.fillText("Score: " + score, 20, 24);
    ctx.fillText("Lives: " + lives, 20, height - 20);
    if (!lives) {
        ctx.fillStyle = "#500";
        ctx.font = "32px monospace";
        ctx.fillText("GAME OVER", width / 2 - 90, height / 2);
    }

    // Set callback for next frame
    setTimeout(function() { step(ctx) }, 1000 / 60);
}

$(document).ready(function() {
    var canvas = document.getElementById("canvas");
    width = canvas.width;
    height = canvas.height;

    // Set up game vars
    score = 0;
    lives = 3;
    ship = {
        x: width / 2,
        y: height / 2,
        angle: 270,
        speed: 0,
        cooldown: 0,
        invincibility: 120
    };
    balls = [];
    shots = [];

    // Set handlers
    $(document.body).on("keydown", function(e) {
        if (lives) {
            switch (e.which) {
                case 65:  // A
                case 37:  // Left arrow
                    ship.angle = (ship.angle - 15) % 360;
                    break;
                case 68:  // D
                case 39:  // Right arrow
                    ship.angle = (ship.angle + 15) % 360;
                    break;
                case 87:  // W
                case 38:  // Up arrow
                    ship.speed++;
                    if (ship.speed > 4)
                        ship.speed = 4;
                    break;
                case 83:  // S
                case 40:  // Down arrow
                    ship.speed--;
                    if (ship.speed < 0)
                        ship.speed = 0;
                    break;
                case 32:  // Space
                    if (!ship.cooldown) {
                        shots.push({
                            x: ship.x,
                            y: ship.y,
                            angle: ship.angle,
                            speed: 5
                        });
                        ship.cooldown = 15;
                    }
                    break;
            }
        }
    });

    // Start
    step(canvas.getContext("2d"));
});
