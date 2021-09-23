let ballCanvas = document.getElementById("ballCanvas")
let ctx = ballCanvas.getContext('2d')

let ball = {
    radius: 4,
    px: Math.random()*ballCanvas.width,
    py: Math.random()*ballCanvas.height,
    vx: (2*Math.random()-1)*10,
    vy: (2*Math.random()-1)*10
}

function drawBall() {
    ctx.beginPath()
    ctx.arc(ball.px, ball.py, ball.radius, 0, 2 * Math.PI, false)
    ctx.fillStyle = "blue"
    ctx.fill()
}

function mainLoop() {
    ctx.clearRect(0,0,ballCanvas.width, ballCanvas.height)
    ball.px += ball.vx 
    ball.py += ball.vy
    if (ball.px < 0 + ball.radius || ball.px > ballCanvas.height - ball.radius){
        ball.vx *= -.99
    }
    if (ball.py < 0 + ball.radius || ball.py > ballCanvas.width - ball.radius) {
        ball.vy *= -.99
    }

    drawBall()
    window.requestAnimationFrame(mainLoop)
}

window.requestAnimationFrame(mainLoop)