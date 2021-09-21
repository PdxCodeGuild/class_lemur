/* 
variable declarations
*/

// // let  (if unsure, just use let)
// let name1 = 'Pete' // let-declared vars can re-declared
// // var
// var name2 = 'Demetric'
// // const
// const name3 = 'Megan' // const-declared vars can not

// name1 += ' Jones'
// // name3 += ' Bradner' causes an error because of the const declaration

// alert('Hello ' + name1 + ' ' + name2 + ' ' + name3 )

/*
prompt, alert & console.log
*/
// // name = input('Enter your name: ')
// let name4 = prompt('Enter your name:') // dialog box in browser
// // print(f'Welcome to JavaScript {name4}')
// alert(`Welcome to JavaScript ${name4}`) // text box in browser
// console.log('hello') // prints into the browser's console

/*
data types
*/
// // number
// let num1 = 3
// let num2 = 3.2
// console.log(num1, num2, typeof num1, typeof num2)
// // string
// let message = 'hello'
// console.log(message, typeof message)
// // boolean
// let bool = true
// console.log(bool, typeof bool)
// let var1 = undefined
// let var2 = null
// console.log(var1, var2, typeof var1, typeof var2)
// // arrays
// const nums = [1, 2, 3, 4, 5]
// console.log(nums, typeof nums)
// // objects
// const obj = {
// 	a: 'hello',
// 	b: 1
// }
// console.log(obj, typeof obj)


/*
Arrays and Loops
*/
// const nums = [2, 5, 7, 1, 8, 2, 0]
// for num in nums:
//  print(num)
// i = 0
// while i < len(nums):
//  print(nums[i])
//  i += 1

// JavaScript for loop
// for (let i = 0; i < nums.length; i++) {
// 	console.log(nums[i])
// }

// Array.forEach method
// nums.forEach(function (num) {
// 	console.log(num)
// })

// nums.push(54)
// console.log(nums)
// let poppedNum = nums.pop()
// console.log(nums, poppedNum)

// let myVar = 1
// var myVar = 2 // error when us
// const myVar = 3
// myVar = 4
// console.log(myVar)

// const words = ['JavaScript', 'is', 'fun']
// // sentence = ' '.join(words) .join is a string method in Python
// const sentence = words.join(' ')
// console.log(sentence)

/*
Functions
*/

// def add(x, y):
//  return x + y
// function add (x, y) {
// 	console.log(x, y)
// 	return x + y
// }
// console.log(add(2, 3)) // 5
// console.log(add(2, 3, 4)) // 5 (this would be an error in python)
// console.log(add(2)) // NaN not a number // x is 2, y is undefined
// console.log(typeof NaN) // number ?!?

// // arrow functions
// // subtract = lambda x, y: x - y
// const subtract = (x, y) => x - y
// console.log(subtract(5, 2)) // 3

/*
Random Numbers
*/

// const names = ['Pete', 'Demetric', 'Megan']

// import random
// print(random.random()) random number between 0 and 1
// print(random.choice(names))
// const randomNumber = Math.random()
// console.log(randomNumber)
// console.log(randomNumber * names.length)
// console.log(Math.floor(randomNumber * names.length))
// console.log(names[Math.floor(randomNumber * names.length)])

// function randomElement(arr) {
// 	return arr[Math.floor(Math.random() * arr.length)]
// }

// console.log(randomElement(names))

/*
Objects
*/

// const instructor = {
// 	name: 'Pete',
// 	jobs: ['teacher', 'frontend dev'],
// 	age: 34,
// 	'Favorite-Food': 'the burrito I just ate'
// }

// const property = 'jobs'

// console.log(instructor.name) // 'Pete'
// console.log(instructor['name']) // 'Pete'
// console.log(instructor['jobs'][0]) // 'teacher'
// console.log(instructor.jobs[1]) // 'frontend dev'
// console.log(instructor['Favorite-Food'])
// console.log(instructor.property) // undefined
// console.log(instructor[property]) // ['teacher', 'frontend dev']

/*
Conditionals
*/
// if 1 > 0:
//   print('yup')
if (1 > 0) {
	console.log('yup')
}

// if 1 > 0 and True:
//   print('yup')
if (1 > 0 && true) {
	console.log('yup')
}

// if True == True or 1 > 3:
//   print('yup')
if (true === true || 1 > 3) {
	console.log('yup')
}

console.log('1' == 1) // true
console.log('1' === 1) // false

// print('1' + 1) // TypeError
console.log('1' + 1) // '11'

// ternary operator
const temp = 60
const weather = temp > 55 ? 'hot' : 'cold'
console.log(weather)

while (temp > 55) {
	console.log('its hot')
}

function Component() { // JSX
	return temp > 55
		? <div>it's hot</div>
		: <div>it's cold</div>
}