const header = document.getElementById('header') 
console.log(header)

const button = document.querySelector('#button')
console.log(button)

const subHeader = document.querySelector('.sub-header')
console.log(subHeader)

const input1 = document.querySelector('#input1')
const input2 = document.querySelector('#input2')
console.log(input1, input2)
let value1 = input1.value
let value2 = input2.value

const output = document.querySelector('#output')

console.log(input1.value, input2.value)

// header.innerText = 'hello'

button.onclick = function () {
	header.style = 'color: red;'
}

button.addEventListener('click', function () {
	subHeader.style = 'color: blue'
})

function addInputs () {
	// output.innerText = value1 + value2
	output.innerText = +input1.value + +input2.value
}

button.addEventListener('click', addInputs)