// single line comments
/*
multi
line
comments
*/

// declaration
// py
// message = 'hello world'
// print(message)

// let message1 = 'hello world' // variables declared with let can be reassigned
// // var message2 = 'hello world?' // nobody uses var; just don't worry about this one
// const message3 = 'hello world!' // variables declared with const cannot be reassigned

// message1 += ' everybody'

// message3 += ' everybody'

// alert(message1)
// // alert(message2)
// alert(message3)

// alert, prompt & console.log
// py
// user_message = input('tell me something ')
// print(f'You told me: {user_message}')

// let userMessage = prompt('tell me something')
// alert(`You told me: ${userMessage}`)
// console.log('You told me: ' + userMessage)

// arrays and loops
// py 
// nums = [1, 2, 3, 4, 5]
// for num in nums:
//   print(num)
// i = 0
// while i < len(nums):
//   print(nums[i])
//   i += 1

// const nums = [1, 2, 3, 4, 5]
// for (let i = 0; i < nums.length; i++) {
// 	console.log(nums[i])
// }

// // py
// // nums.append(6)
// nums.push(6)
// console.log(nums, typeof nums)

// // py
// // nums.pop(-1) # pops off the last item of the list
// let poppedNum = nums.pop()
// console.log(poppedNum, nums)

// Array.join()
// py
// words = ['JavaScript', 'is', 'fun']
// sentence = ' '.join(words)
// print(sentence) # 'JavaScript is fun'

// const words = ['JavaScript', 'is', 'fun']
// const sentence = words.join(' ')
// console.log(sentence)

// Objects
// py
// instructor = {
	// 'name': 'Pete',
	// 'age': 34,
	// 'jobs': ['teacher', 'frontend dev']
	// 'favorite-food': 'curry'
// }

// const instructor = {
// 	name: 'Pete',
// 	age: 34,
// 	jobs: ['teacher', 'frontend dev'],
// 	'favorite-food': 'curry',
// 	placesTraveled: [
// 		{name: 'Greece', food: 'Moussaka'},
// 		{name: 'Korea', food: 'Bibimbap'},
// 	]
// }

// console.log(instructor)
// console.log(instructor.name)
// console.log(instructor['age'])

// console.log(instructor.placesTraveled[0].food)

// let prop = prompt('which property do you want?')
// alert(instructor.prop) // undefined
// alert(instructor['prop']) // undefined
// alert(instructor[prop])


// Functions
// py
// def add(x, y):
//   return x + y
// add(1, 2) # 3
// add(1, 2, 3) # TypeError: add() takes 2 positional arguments but 3 were given
// add(1) # TypeError: add() missing 1 required positional argument: 'y'

// function add(x, y) {
// 	return x + y
// }

// console.log(add(1, 2)) // 3
// console.log(add(1, 2, 3)) // 3
// console.log(add(1))
// let notANumber = add(1)
// console.log(typeof notANumber)

// // py
// // subtract = lambda x, y: x - y

// // arrow function
// const subtract = (x, y) => x - y
// console.log(subtract(3, 2))

// let multiply = function (x, y) {
// 	return x * y
// }

// const names = ['scott', 'swarty', 'david']

// function upperCaseName (name) {
// 	console.log(name.toUpperCase())
// }

// names.forEach(name => console.log(name.toUpperCase()))
// names.forEach(upperCaseName)

// Random numbers, etc.
// py
// import random
// names = ['scott', 'swarty', 'david']
// random.choice(names)

// names[random.random() * len(names) // 1]

// const names = ['scott', 'swarty', 'david']
// // let randomNum = Math.random()
// // console.log(randomNum)
// // console.log(randomNum * names.length)
// // console.log(Math.floor(randomNum * names.length))
// // console.log(names[Math.floor(randomNum * names.length)])

// function randomChoice(arr) {
// 	return arr[Math.floor(Math.random() * arr.length)]
// }

// console.log(randomChoice(names))

// conditionals 
// py
// x = 5
// if x > 0 and x < 10:
//   print('x is between 10 and 5')

// let x = 5
// if (x > 0 && x < 10) {
//     console.log('x is between 5 and 10')
// }
// // if x == 5 or x == 6: ...
// if (x == 5 || x == 6) {
//     console.log('x is 5 or 6')
// }

// let y = false
// // if not y: ...
// if (!y) {
//     console.log('y is false')
// }

// console.log(1 == '1') // false
// console.log(1 === '1') // true

// console.log(1 + '1') // '11'

// // x = 56
// let x = 56
// // if x < 60: ...
// if (x < 60) {
//     alert('cold')
// // elif x < 80: ...
// } else if (x < 80) {
//     alert('warm')
// // else:
// } else {
//     alert('hot')
// }

// ternary operator

let temp = 60
let weatherReport = temp > 55 ? 'warm' : 'cool'
console.log(weatherReport)