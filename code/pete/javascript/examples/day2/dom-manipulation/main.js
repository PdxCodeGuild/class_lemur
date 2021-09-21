const header = document.getElementById('header')
console.log(header)
header.innerText += ' is fun!'

const button = document.querySelector('#button')
console.log(button)

const input1 = document.querySelector('#input1')
const input2 = document.querySelector('#input2')
const output = document.querySelector('#output')

button.onclick = function (event) {
	header.style = 'color: red;'
	// alert('you clicked it')
	console.log(event)
}

button.addEventListener('click', function () {
	console.log(input1)
	output.innerText = input1.valueAsNumber + input2.valueAsNumber
})