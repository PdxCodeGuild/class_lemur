const width = canvas.width
console.log(width)
const height =canvas.height
// const height= window.getComputedStyle(document.querySelector(#canvas)).height

const ctx = canvas.getContext("2d");
let ball = {
    radius: 4,
    px: Math.random()*width,
    py: Math.random()*height,
    vx: (2*Math.random()-1)*10,
    vy: (2*Math.random()-1)*10
}
function dot(){
    ctx.beginPath();
    ctx.arc(ball.px, ball.py, ball.radius, 0, 2 * Math.PI, false);
    ctx.fillStyle = 'green';
    ctx.fill()
}

function drawing() {
    // update the ball's position
    
    ball.px += ball.vx
    ball.py += ball.vy
    // check if it hit a boundary
    if(ball.px + ball.vx < 0 ||ball.px + ball.vx < width ) {
        ball.vx = -ball.vx;
    }
    if(ball.py + ball.vy < 0 ||ball.py + ball.vy < height ) {
        ball.vy = -ball.vy;
    }
    // draw the ball
    dot()
    // window.requestAnimationFrame(main_loop);
}
// window.requestAnimationFrame(main_loop);
setInterval(drawing, 10)