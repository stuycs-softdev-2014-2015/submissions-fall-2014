$(document).ready(function() {
    var svg = document.getElementById("game");
    var score_counter = document.getElementById("score");
    var lives_counter = document.getElementById("lives");
    var game_over = document.getElementById("game-over");
    var width = svg.getAttribute("width");
    var height = svg.getAttribute("height");

    var distance = function(a, b) {
        return Math.sqrt(Math.pow(a.x - b.x, 2) + Math.pow(a.y - b.y, 2));
    }

    var transform = function(tlist, x, y, angle) {
            var tl = svg.createSVGTransform(), rt = svg.createSVGTransform();
            tl.setTranslate(x, y);
            rt.setRotate(angle + 90, 0, 0);
            tlist.clear();
            tlist.appendItem(tl);
            tlist.appendItem(rt);
    }

    var move = function(obj, factor) {
        obj.x += factor * Math.cos(obj.angle * Math.PI / 180);
        obj.y += factor * Math.sin(obj.angle * Math.PI / 180);
        if (obj.x > width)     obj.x = 0;
        if (obj.x < 0)         obj.x = width - 1;
        if (obj.y > height)    obj.y = 0;
        if (obj.y < 0)         obj.y = height - 1;
    }

    var ship = {
        moving: false,
        firing: false,
        turning: 0,
        score: 0,
        lives: 3,

        x: width / 2,
        y: height / 2,
        angle: -90,
        cooldown: 0,
        invincibility: 120,
        respawning: 0,

        elem: document.getElementById("ship"),

        simulate: function() {
            if (this.moving)
                move(this, 4);
            if (this.turning)
                this.angle = (this.angle - (this.turning * 5)) % 360;
            if (this.firing) {
                if (!this.cooldown) {
                    bullets.spawn(this.x, this.y, this.angle);
                    this.cooldown = 15;
                }
            }
            if (this.cooldown)
                this.cooldown--;
            if (this.invincibility)
                this.invincibility--;
            if (this.respawning) {
                this.respawning--;
                if (!this.respawning) {
                    if (this.lives < 1)
                        this.respawning = -1;
                    else {
                        this.moving = false;
                        this.firing = false;
                        this.turning = 0;
                        this.lives--;
                        this.x = width / 2;
                        this.y = width / 2;
                        this.angle = -90;
                        this.invincibility = 120;
                    }
                }
            }

            if (!this.invincibility && !this.respawning) {
                for (var enemy in enemies.list) {
                    var eobj = enemies.list[enemy];
                    if (distance(this, eobj) < eobj.radius + 5) {
                        ship.respawning = 60;
                        svg.removeChild(eobj.elem);
                        enemies.list.splice(enemy, 1);
                    }
                }
            }
        },

        draw: function() {
            transform(this.elem.transform.baseVal, this.x, this.y, this.angle);

            if (this.respawning)
                this.elem.setAttribute("opacity", 0);
            else if (!((this.invincibility / 2) % 2 != 1))
                this.elem.setAttribute("opacity", 0.25);
            else
                this.elem.setAttribute("opacity", 1);
        }
    };

    var enemies = {
        list: [],

        simulate: function() {
            var dying = [];
            for (var enemy in this.list) {
                var obj = this.list[enemy];
                move(obj, obj.speed);
            }
            for (var i = 0; i < dying.length; i++) {
                var obj = this.list[dying[i] - i];
                svg.removeChild(obj.elem);
                this.list.splice(dying[i] - i, 1);
            }
            if (Math.random() < 0.02)
                this.spawn(Math.random() * width, Math.random() * height, Math.random() * 20 + 5, Math.random() * 360, Math.random() * 5 + 2);
        },

        draw: function() {
            for (var enemy in this.list) {
                var obj = this.list[enemy];
                transform(obj.elem.transform.baseVal, obj.x, obj.y, 0);
            }
        },

        spawn: function(x, y, r, angle, speed) {
            var elem = document.createElementNS("http://www.w3.org/2000/svg", "circle");
            elem.setAttribute("cx", 0);
            elem.setAttribute("cy", 0);
            elem.setAttribute("r", r);
            elem.setAttribute("fill", "#F0E68C");
            elem.setAttribute("stroke", "#BDB76B");
            svg.appendChild(elem);

            var obj = {
                x: x,
                y: y,
                radius: r,
                angle: angle,
                speed: speed,
                elem: elem
            };
            this.list.push(obj);
        }
    }

    var bullets = {
        list: [],

        simulate: function() {
            var dying = [];
            for (var bullet in this.list) {
                var obj = this.list[bullet];
                move(obj, 8);
                if (!ship.invincibility && !ship.respawning && distance(obj, ship) < 10) {
                    ship.respawning = 60;
                    dying.push(bullet);
                    continue;
                }
                for (var enemy in enemies.list) {
                    var eobj = enemies.list[enemy];
                    if (distance(obj, eobj) < eobj.radius + 5) {
                        ship.score += Math.floor(10 * eobj.radius);
                        dying.push(bullet);
                        svg.removeChild(eobj.elem);
                        enemies.list.splice(enemy, 1);
                        break;
                    }
                }
            }
            for (var i = 0; i < dying.length; i++) {
                var obj = this.list[dying[i] - i];
                svg.removeChild(obj.elem);
                this.list.splice(dying[i] - i, 1);
            }
        },

        draw: function() {
            for (var bullet in this.list) {
                var obj = this.list[bullet];
                transform(obj.elem.transform.baseVal, obj.x, obj.y, obj.angle);
            }
        },

        spawn: function(x, y, angle) {
            var elem = document.createElementNS("http://www.w3.org/2000/svg", "rect");
            elem.setAttribute("x", -1);
            elem.setAttribute("y", -5);
            elem.setAttribute("width", 2);
            elem.setAttribute("height", 10);
            elem.setAttribute("fill", "#080");
            elem.setAttribute("stroke", "#040");
            svg.appendChild(elem);

            var obj = {
                x: x,
                y: y,
                angle: angle,
                elem: elem
            };
            this.list.push(obj);
            move(obj, 10);
        }
    };

    step = function() {
        ship.simulate();
        enemies.simulate();
        bullets.simulate();

        ship.draw();
        enemies.draw();
        bullets.draw();

        score_counter.innerHTML = ship.score;
        lives_counter.innerHTML = ship.lives;
        if (ship.lives < 1 && ship.respawning < 0)
            game_over.setAttribute("opacity", 1);

        setTimeout(step, 1000 / 60);
    }

    $(document.body).on("keydown", function(e) {
        if (!ship.respawning) {
            switch (e.which) {
                case 65:  // A
                case 37:  // Left arrow
                    ship.turning = 1;
                    break;
                case 68:  // D
                case 39:  // Right arrow
                    ship.turning = -1;
                    break;
                case 87:  // W
                case 38:  // Up arrow
                    ship.moving = true;
                    break;
                case 32:  // Space
                    ship.firing = true;
                    break;
            }
        }
    });

    $(document.body).on("keyup", function(e) {
        if (!ship.respawning) {
            switch (e.which) {
                case 65:  // A
                case 37:  // Left arrow
                    ship.turning = 0;
                    break;
                case 68:  // D
                case 39:  // Right arrow
                    ship.turning = 0;
                    break;
                case 87:  // W
                case 38:  // Up arrow
                    ship.moving = false;
                    break;
                case 32:  // Space
                    ship.firing = false;
                    break;
            }
        }
    });

    step();
});
