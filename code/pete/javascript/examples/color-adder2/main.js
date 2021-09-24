const form = document.querySelector('form')
const colorInput = document.querySelector('#color-input')
const colorContainer = document.getElementById('color-container')
// console.log(form, colorInput, colorContainer)

form.addEventListener('submit', function (event) {
	event.preventDefault()

	// console.log(colorInput.value) // the value of the input element
	const colorSection = document.createElement('section')
	colorSection.classList.add('color-section')
	colorSection.style.backgroundColor = colorInput.value
	colorContainer.appendChild(colorSection)

	colorSection.addEventListener('click', function() {
		alert(colorInput.value)
	})
})