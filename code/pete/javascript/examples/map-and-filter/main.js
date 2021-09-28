// arrow functions

// using function declaration
function otherAdd (x, y) {
	return x + y
}

// using arrow function
const add = (x, y) => x + y

console.log(otherAdd(2, 3))
console.log(add(3, 4))

// forEach

const colors = ['red', 'green', 'blue']

for (let i = 0; i < colors.length; i++) {
	const color = colors[i]
	console.log(color)
}

colors.forEach(function(color) {
	console.log(color)
})

colors.forEach(function(color, index, arr) {
	// arr[index] = color.toUpperCase() you can use the index and arr as well :)
	console.log(color, index, arr)
})

colors.forEach(sayHi)

function sayHi() {
	// alert('hey!')
	console.log('hey')
}


// map

const sentences = colors.map(color => 'I spy with my little eye something... ' + color)
console.log(sentences)


// filter

const nums = [2, 5, 3.2, 98, 75, 81, 537, 15, 42, 93, 762, 0.1]
const evens = nums.filter(num => num % 2 === 0)
console.log(evens)
const odds = nums.filter(num => num % 2 === 1)
console.log(odds)

const numsObj = { nums, evens, odds }
console.log(numsObj)

// filter and map
const evenSentences = nums.filter(num => num % 2 === 0).map(num => `${num} is an even number`)
console.log(evenSentences)
const oddSentences = nums.filter(num => num % 2 === 1)
												 .map(num => `${num} is an odd number`)
console.log(oddSentences)