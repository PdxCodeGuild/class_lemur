const colors = {
	sky: '#0C064F',
	mountain: '#6E5647',
	snow: '#BFBCAE',
	moon: '#F7F579'
}

const w = 800
const h = 450

const moon = {
	x: 283,
	y: 271,
	r: 50,
	color: colors.moon
}

const cnv = document.querySelector('canvas')
const ctx = cnv.getContext('2d')

cnv.addEventListener('click', e => {
	// console.log(e)
	console.log(e.offsetX, e.offsetY)
	moon.x = e.offsetX
	moon.y = e.offsetY
	// drawMoon(moon)
})

const starsArray = []

for (let i = 0; i < 3000; i++) {
	const star = {
		x: Math.random() * w,
		y: Math.random() * h,
		r: Math.random() * 1.5,
	}
	starsArray.push(star)
}

function animationLoop() {
	ctx.fillStyle = colors.sky
	ctx.fillRect(0, 0, w, h)
	
	ctx.fillStyle = 'white'

	starsArray.forEach(star => {
		ctx.beginPath()
		ctx.arc(star.x, star.y, star.r, 0, 2 * Math.PI)
		ctx.fill()
	})

	drawMoon(moon)

	moon.x += 0.05
	moon.y -= 0.1
	
	drawTriangle(225, 125, h - 125, colors.mountain)
	drawTriangle(225, 125, 100, colors.snow)
	drawTriangle(w - 225, 125, h - 125, colors.mountain)
	drawTriangle(w - 225, 125, 100, colors.snow)
	

	requestAnimationFrame(animationLoop)
}

animationLoop()


function drawTriangle (startX, startY, height, color) {
  ctx.fillStyle = color
  ctx.beginPath()
  ctx.moveTo(startX, startY)
  ctx.lineTo(startX + height, startY + height)
  ctx.lineTo(startX - height, startY + height)
  ctx.closePath()
  ctx.fill()
  ctx.stroke()
}

function drawMoon(moon) {
	ctx.fillStyle = moon.color
	ctx.beginPath()
	ctx.arc(moon.x, moon.y, moon.r, 0, 2 * Math.PI)
	ctx.fill()
	const gradient = ctx.createRadialGradient(moon.x, moon.y, 0, moon.x, moon.y, 75)
	ctx.beginPath()
	gradient.addColorStop(0, 'rgba(255, 255, 255, .75)')
	gradient.addColorStop(1, 'rgba(255, 255, 255, 0)')
	ctx.fillStyle = gradient
	ctx.arc(moon.x, moon.y, 75, 0, 2 * Math.PI)
	ctx.fill()
}