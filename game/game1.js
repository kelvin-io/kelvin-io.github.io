var canvas = document.getElementById("canvas");
var context = canvas.getContext("2d");

var character = {
    x: 50,
    y: canvas.height / 2,
    width: 50,
    height: 50,
    color: "blue",
    speed: 5,
    isJumping: false,
    jumpHeight: 100,
    jumpCount: 0
};

var obstacles = [];
var obstacleWidth = 50;
var obstacleHeight = 50;
var obstacleSpeed = 2;
var obstacleSpawnInterval = 1000;
var score = 0;

function drawCharacter() {
    context.fillStyle = character.color;
    context.fillRect(character.x, character.y, character.width, character.height);
}

function updateCharacter() {
    if (character.isJumping) {
        character.y -= character.speed;
        character.jumpCount += character.speed;
        if (character.jumpCount >= character.jumpHeight) {
            character.isJumping = false;
            character.jumpCount = 0;
        }
    } else {
        character.y += character.speed;
    }
}

function drawObstacles() {
    context.fillStyle = "red";
    for (var i = 0; i < obstacles.length; i++) {
        context.fillRect(obstacles[i].x, obstacles[i].y, obstacleWidth, obstacleHeight);
    }
}

function updateObstacles() {
    for (var i = 0; i < obstacles.length; i++) {
        obstacles[i].x -= obstacleSpeed;

        if (obstacles[i].x + obstacleWidth < 0) {
            obstacles.splice(i, 1);
            i--;
            score++;
        }

        if (isCollision(character, obstacles[i])) {
            // Game over
            alert("Game over! Your score: " + score);
            location.reload();
        }
    }
}

function isCollision(rect1, rect2) {
    return rect1.x < rect2.x + obstacleWidth &&
           rect1.x + character.width > rect2.x &&
           rect1.y < rect2.y + obstacleHeight &&
           rect1.y + character.height > rect2.y;
}

function jumpCharacter() {
    if (!character.isJumping) {
        character.isJumping = true;
    }
}

function spawnObstacle() {
    var y = Math.random() * (canvas.height - obstacleHeight);
    obstacles.push({ x: canvas.width, y: y });
}

function clearCanvas() {
    context.clearRect(0, 0, canvas.width, canvas.height);
}

function drawScore() {
    context.font = "16px Arial";
    context.fillStyle = "black";
    context.fillText("Score: " + score, 10, 20);
}

document.addEventListener("keydown", function (event) {
    if (event.keyCode === 32) {
        jumpCharacter();
    }
});

setInterval(function () {
    spawnObstacle();
}, obstacleSpawnInterval);

function gameLoop() {
    clearCanvas();

    updateCharacter();
    updateObstacles();

    drawCharacter();
    drawObstacles();
    drawScore();

    requestAnimationFrame(gameLoop);
}

gameLoop();