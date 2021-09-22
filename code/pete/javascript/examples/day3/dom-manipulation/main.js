const header = document.getElementById('header')
console.log(header)
header.innerText += ' is fun!'

const subHeader = document.getElementById('sub-header')

const button = document.querySelector('#button')
console.log(button)

const input1 = document.querySelector('#input1')
const input2 = document.querySelector('#input2')
console.log(input1)

const output = document.querySelector('#output')

button.onclick = function () {
	header.style.color = 'red'
}

button.addEventListener('click', function () {
	subHeader.style.color = 'blue'
})

button.addEventListener('click', function () {
	output.innerText = input1.valueAsNumber + input2.valueAsNumber
})