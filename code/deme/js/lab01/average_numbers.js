let nums = [5, 0, 8, 3, 4, 1, 6]
let sum = 0

for (let i = 0;  i < nums.length; i++) {
    sum += nums[i]
    console.log(nums[i])
}
console.log(sum)

let averageNum = sum / nums.length
console.log(averageNum)

//                  Version2
let numForm = document.getElementById('numForm')
let numList = document.getElementById('numList')
let numListForm = document.getElementById('numListForm')
let numbers = document.getElementById('numbers')
let numDiv = document.getElementById('numDiv')

numForm.addEventListener('submit', function(event) {
    event.preventDefault()
    let userNum = numListForm.value
    let numLi = document.createElement('li')
    console.log(numLi)
    numLi.innerHTML=userNum
    numList.appendChild(numLi)
    let addNum = document.createElement('button')
    addButton.innerText = "Add Number"

    
    addButton.addEventListener('click', function(){
        numList.appendChild(numLi)
    })
}

    // numLi.appendChild(addButton)
    // let completeButton = document.createElement("button")
    // completeButton.innerText = "Complete"
    // itemLi.appendChild(completeButton)
// let userNums=[]
// let userInput = prompt("Please enter a number or 'done' to exit.")
// while(userInput != 'done'){
//   userNums.push(userInput)
//   userInput = prompt("Please enter a number or 'done' to exit.")
// }

// console.log(userNums)
// console.log(userInput)
