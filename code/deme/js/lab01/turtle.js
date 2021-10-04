
var canvas = document.getElementById("turtle");

var ctx = canvas.getContext("2d"); //create drawing object

ctx.fillStyle = "#87CEEB"
ctx.fillRect(1, 1, 500, 400);
console.log(ctx)

//bottom rectangle
ctx.fillStyle = "green"
ctx.fillRect(1, 400, 1000, 20);
console.log(ctx)

//house
ctx.fillStyle = "blue"
ctx.fillRect(250, 200, 200, 200)

//door
ctx.fillStyle = "white"
ctx.fillRect(200, 200, 200, 200)
//sun
ctx.beginPath();
ctx.arc(100, 75, 50, 0, 2 * Math.PI);
ctx.fillStyle="yellow";
ctx.fill();
// ctx.stroke();



ctx.beginPath();
// ctx.moveTo(150, 50)
ctx.lineTo(250, 200)
ctx.lineTo(450, 200)
ctx.lineTo(350, 100)
ctx.lineTo(250, 200)

ctx.fillStyle="red"
ctx.fill();





ctx.stroke();
