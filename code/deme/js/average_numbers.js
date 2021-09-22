let nums = [5, 0, 8, 3, 4, 1, 6]
let sum = 0

for (let i = 0;  i < nums.length; i++) {
    sum += nums[i]
    console.log(nums[i])
}
console.log(sum)

let averageNum = sum / nums.length
console.log(averageNum)

let userNums=[]
let userInput = prompt("Please enter a number or 'done' to exit.")
while(userInput != 'done'){
  userNums.push(userInput)
  userInput = prompt("Please enter a number or 'done' to exit.")
}

console.log(userNums)
console.log(userInput)





