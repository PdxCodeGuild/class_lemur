const timeoutButton = document.getElementById('timeout-button')
const intervalButton = document.getElementById('interval-button')

const colors = ['red', 'green', 'blue']

let colorsChanging = false

function randomColor () {
	return colors[Math.floor(Math.random() * colors.length)]
}

timeoutButton.addEventListener('click', function () {
	setTimeout(function () {
		alert('hello')
	}, 1000)
})

let intervalId
intervalButton.addEventListener('click', function() {
	console.log('before if/else')
	console.log({ colorsChanging, intervalId })
	if (colorsChanging) {
		clearInterval(intervalId)
		colorsChanging = false
	} else {
		colorsChanging = true
		intervalId = setInterval(function() {
			document.body.style.backgroundColor = randomColor()
		}, 2000)
	}
	console.log('after if/else')
	console.log({ colorsChanging, intervalId })
	console.log('*******************************')
})