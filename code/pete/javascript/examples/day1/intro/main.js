let myName = 'Pete' // vars declared with let can be redefined
var otherName = 'Matt' // don't use var, nobody uses it anymore
const otherOtherName = 'Mark' // use const if you are not redeclaring

myName += ' Jones'
// otherOtherName += ' Dziuban' // causes error because const variables cannot be redeclared

// alert('hello ' + myName + ' ' + otherName + ' ' + otherOtherName)

const nums = [1, 2, 3, 4, 5]

nums.push(6)

console.log(nums, nums.length)
console.log(nums.banana)

// for loops
// for num in nums:
	// print(num)
	
// i = 0
// while i < len(nums):
	// print(nums[i])
	// i += 1

for (let i = 0; i < nums.length; i++) {
	// alert(nums[i])
}

// functions
function add(x, y) {
	return x + y
}

// let x = parseInt(prompt('enter number 1')) // use parseInt to convert a string or float to an integer
// let y = +prompt('enter number 2') // shorthand: use a + sign before a string to type convert

// alert(add(x, y))

console.log(4 + '4') // '44'
console.log('4' + 4) // '44'

console.log(add(1, 2, 3, 4, 5, 6, 7, 8)) // 3 ignores argument overload
console.log(add(1)) // NaN
console.log(typeof NaN)

// random numbers
let randomFloat = Math.random()
console.log(randomFloat)
console.log(randomFloat * nums.length)
console.log(Math.floor(randomFloat * nums.length))
console.log(nums[Math.floor(randomFloat * nums.length)])

const letters = ['a', 'b', 'c', 'd', 'e']
console.log(letters[Math.floor(Math.random() * letters.length)])

function randomItem (arr) {
	return arr[Math.floor(Math.random() * arr.length)]
}

console.log(randomItem([1, 'hello', 5, '5']))

// booleans and conditionals
// true and false are not capitalized

console.log(1 == '1')
console.log(1 === '1')

console.log(
	2 < 7 && 4 < 7
)

console.log(
	2 > 7 || 8 > 7
)

let num = 3
num = 7

let message = num < 6 ? `${num} is less than 6` : `${num} is greater than 6`

// alert(message)

// objects

const test = {
	a: 1,
	b: 2,
	c: 3,
	'CSRF-Token': 'fkjdskla;fn584iw;ao' // certain properties need quotes if they have hyphens, spaces, etc.
}

let prop = 'b'

console.log(test.b) // 2
console.log(test['CSRF-Token']) // 'fkjdskla;fn584iw;ao'
console.log(test.prop) // undefined
console.log(test[prop]) // 2


// extras
// arrow functions
const subtract = (x, y) => x - y
console.log(subtract(6, 2))

// array methods
const otherNums = [1, 4, 7, 2, 9, 3, 6, 8]
// otherNums.forEach(num => console.log(num))
otherNums.forEach(function (num) {
	console.log(num)
})

const doubledNums = otherNums.map(num => num * 2)
console.log(doubledNums)

const evens = otherNums.filter(num => num % 2 === 0)
console.log(evens)

const evensDoubled = otherNums.filter(num => num % 2 === 0).map(num => num * 2)
console.log(evensDoubled)