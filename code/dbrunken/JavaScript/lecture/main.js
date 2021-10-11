// single line comment
/*
multi
line
comment
*/

// declarations
// py
// message = "hello world"
// print(message)

// let message1 = 'hello world' //variables declared with let can be reassigned
// // let message2 = 'hello world?'
// const let message3 = 'hello world!' // variables with const cannot be reassigned

// message1 += ' everybody'
// // message3 += ' everybody'

// alert(message1)

// alert, prompt & console.log
// py
// user_message = input('tell me something ')
// print(f'you told me: {user_message}')

// let userMessage = prompt('tell me something ')
// alert(`you told me: ${userMessage}`)
// console.log('you told me: '+ userMessage)

// arrays and loops
// py
// nums = [1, 2, 3, 4, 5]
// for num in nums:
    // print(num)

// i = 0
// while i <length(nums):
//     print(nums[i])
//     i+=1

// const nums = [1, 2, 3, 4, 5]
// for (let i = 0; i < nums.length; i ++) {
//     console.log(nums[i])
// }

// py
// nums.append(6)
// nums.push(6)
// console.log

// py
// nums.pop(-1) // pops off the last of the list
// let poppedNum = nums.pop()
// console.log(poppedNum, nums)

// objects
// py
// instructor = {
//     'name': 'pete',
//     'age': 34,
//     'jobs': ['teacher', 'frontend dev']
// }

// const instructor = {
//     name: 'pete',
//     age: 34,
//     jobs: ['teacher', 'frontend dev'],
//     'favorite-food': 'curry'
// }

// console.log(instructor)
// console.log(instructor.name)
// console.log(instructor['age'])

// let prop = prompt('which property do you want')
// alert(instructor.prop) //undefined
// alert(instructor['prop']) //undefined
// alert(instructor[prop])

// function add(x, y) {
//     return x + y
// }

// console.log(add(1, 2))
// console.log(add(1, 2, 3))
// console.log(add(1))
// let notANumber = add(1)
// console.log(typeof notANumber)

// const subtract = (x, y) => x-y
// console.log(subtract(3, 2))

// let multiply = function (x, y) {
//     return x * y
// }

// const names = ['scott', 'swarty', 'david']

// function upperCaseName (name)

//==================================================================

const header = document.getElementById('header')
console.log(header)
header.innerText += 'is fun'

const subHeader = document.getElementById('sub-header')

const button = document.querySelector('#button')
console.log(button)

const input1 = document.querySelector
const input2 = document.querySelector

button.onClick = function () {
    header.style.color = 'red'
}

button.addEventListener('click', function () {
    subHeader.style.color = 'blue'
})