const timingMessage = document.querySelector('#timing-message')
timingMessage.style.display = 'none'

setTimeout(function() {
	timingMessage.style.display = 'block'
}, 3000)

alert('hey')

const colorChanger = document.getElementById('color-changer')
const colorChangerStopper = document.getElementById('color-changer-stopper')

let intervalId
let colorsChanging = false

colorChanger.addEventListener('click', function() {
	if (colorsChanging === false) {
		intervalId = setInterval(function() {
			document.body.style.backgroundColor = randomColor()
		}, 3000)
		colorsChanging = true
	}
})

colorChangerStopper.addEventListener('click', function() {
	if (colorsChanging === true) {
		clearInterval(intervalId)
		colorsChanging = false
	}
})

function randomColor() {
	const hexCodes = '0123456789abcdef'
	let color = '#'
	for (let i = 0; i < 6; i++) {
		color += hexCodes[Math.floor(Math.random() * hexCodes.length)]
	}
	return color
}

