let ballCanvas = document.getElementById("ballCanvas")
let ctx = ballCanvas.getContext('2d')
let force = 0


let ball1 = {
    radius: 8,
    mass: 1000000,
    px: Math.random()*ballCanvas.width,
    py: Math.random()*ballCanvas.height,
    vx: (2*Math.random()-1)*2,
    vy: (2*Math.random()-1)*2,
    ballColor: 'blue'
}

let ball2 = {
    radius: 10,
    mass: 1000000,
    px: Math.random()*ballCanvas.width,
    py: Math.random()*ballCanvas.height,
    vx: (2*Math.random()-1)*2,
    vy: (2*Math.random()-1)*2,
    ballColor: 'red'
}

let ball3 = {
    radius: 6,
    mass: 1.5,
    px: Math.random()*ballCanvas.width,
    py: Math.random()*ballCanvas.height,
    vx: (2*Math.random()),
    vy: (2*Math.random()),
    ballColor: 'black'
}

let balls = [ball1, ball2]

function moveBall(ball) {
    ball.px += ball.vx
    ball.py += ball.vy
}

function drawBall(ball) {
    ctx.beginPath()
    ctx.arc(ball.px, ball.py, ball.radius, 0, 2 * Math.PI, false)
    ctx.fillStyle = ball.ballColor
    ctx.fill()
}

function checkWallCollision(ball) {
    if (ball.px - ball.radius <= 0  || ball.px + ball.radius >= ballCanvas.height ){
        ball.vx *= -.99
    }
    if (ball.py - ball.radius <= 0  || ball.py + ball.radius >= ballCanvas.width ) {
        ball.vy *= -.99
    }
}

function checkBallCollision(){
    distance = Math.sqrt(((ball1.px - ball2.px) * (ball1.px - ball2.px)) + ((ball1.py - ball2.py) * (ball1.py - ball2.py)))
    if (distance < ball1.radius + ball2.radius){
        newVelocityX1 = (ball1.vx * (ball1.mass - ball2.mass) + (2*ball2.mass * ball2.vx)) / (ball1.mass + ball2.mass)
        newVelocityY1 = (ball1.vy * (ball1.mass - ball2.mass) + (2*ball2.mass * ball2.vy)) / (ball1.mass + ball2.mass)
        newVelocityX2 = (ball2.vx * (ball2.mass - ball1.mass) + (2*ball1.mass * ball1.vx)) / (ball2.mass + ball1.mass)
        newVelocityY2 = (ball2.vy * (ball2.mass - ball1.mass) + (2*ball1.mass * ball1.vy)) / (ball2.mass + ball1.mass)
        ball1.vx = newVelocityX1
        ball1.vy = newVelocityY1
        ball2.vx = newVelocityX2
        ball2.vy = newVelocityY2
        ball1.px = newVelocityX1 + ball1.px
        ball1.py = newVelocityY1 + ball1.py
        ball2.px = newVelocityX2 + ball2.px
        ball2.py = newVelocityY2 + ball2.py
    }
}

function checkIfNear() {
    if (ball1.px + ball1.radius + ball2.radius > ball2.px 
        && ball1.px < ball2.px + ball1.radius + ball2.radius
        && ball1.py + ball1.radius + ball2.radius > ball2.py 
        && ball1.py < ball2.py + ball1.radius + ball2.radius)
        {
            checkBallCollision()
        }
    
}

function gravity() {
    // force = g(m1*m2)/r^2
    let distance1 = Math.sqrt(((ball2.px - ball1.px) * (ball2.px - ball1.px)) + ((ball2.py - ball1.py) * (ball2.py - ball1.py)))
    let distance2 = Math.sqrt(((ball1.px - ball2.px) * (ball1.px - ball2.px)) + ((ball1.py - ball2.py) * (ball1.py - ball2.py)))
    const g = .00000000006674
    let force1 = -g * ((ball2.mass * ball1.mass)/(Math.abs(distance1)**2))*(distance1/Math.abs(distance1))
    let force2 = -g * ((ball1.mass * ball2.mass)/(Math.abs(distance2)**2))*(distance2/Math.abs(distance2))
    ball1.vx += force1
    ball1.vy += force1
    ball2.vx += force2
    ball2.vy += force2
}

function mainLoop() {
    // ctx.clearRect(0,0,ballCanvas.width, ballCanvas.height)
    ctx.fillStyle = "rgba(255,255,255,.3)"
    ctx.fillRect(0,0,ballCanvas.width, ballCanvas.height)
    gravity()
    for (let i = 0; i < balls.length; i++){
        moveBall(balls[i], force)
        
    }
    for (let i=0; i < balls.length; i++){
        checkWallCollision(balls[i])
        checkIfNear()
        drawBall(balls[i])
    }
    // drawBall()
    window.requestAnimationFrame(mainLoop)
}



window.requestAnimationFrame(mainLoop)