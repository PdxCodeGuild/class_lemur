
var canvas = document.getElementById("turtle");

var ctx = canvas.getContext("2d"); //create drawing object

//bottom rectangle
ctx.fillStyle = "green"
ctx.fillRect(200, 400, 1000, 20);
console.log(ctx)

ctx.fillStyle = "blue"
ctx.fillRect(250, 200, 200, 200)


//circle
// ctx.fillStyle = "#FF9111"
// ctx.beginPath();
// ctx.arc(100, 100, 0, 2 * Math.PI);
// console.log(ctx)

ctx.beginPath();
ctx.arc(100, 75, 50, 0, 2 * Math.PI);
ctx.fillStyle="red";
ctx.fill();
// ctx.stroke();



ctx.stroke();
