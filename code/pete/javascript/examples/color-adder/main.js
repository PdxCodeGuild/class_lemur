const main = document.querySelector('main')

const colorInput = document.querySelector('#color-input')

const form = document.querySelector('form')

const colorDivs = document.querySelectorAll('.color')
console.log(colorDivs)

const colorDivs2 = document.getElementsByClassName('color')
console.log(colorDivs2)

form.addEventListener('submit', function(event) {
	event.preventDefault()
	// console.log(event)
	// console.log('form was submitted')
	let color = colorInput.value
	const colorDiv = document.createElement('div')
	console.log(colorDiv)
	colorDiv.classList.add('color')
	colorDiv.style.backgroundColor = color
	main.appendChild(colorDiv)

	colorDiv.addEventListener('click', function() {
		alert(color)
	})
})