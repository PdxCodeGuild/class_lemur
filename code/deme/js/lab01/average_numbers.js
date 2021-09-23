//                  Version2
let numForm = document.getElementById('numForm')
let numList = document.getElementById('numList')
let numListForm = document.getElementById('numListForm')
let numbers = document.getElementById('numbers')
let num = []


numForm.addEventListener('submit', function(event) {
    event.preventDefault()
    let userNum = numListForm.value
    let numLi = document.createElement('li')
    numLi.innerHTML=userNum
    numList.appendChild(numLi)
    })

    let done = document.createElement('button')
    done.innerText = 'Done'
    numForm.appendChild(done)

    done.addEventListener('click', function(){
        for(let i =0; i<numList.length; i++)
        nums.push(numList[i])
        console.log(nums)
    })
})

// let userNums=[]
// let userInput = prompt("Please enter a number or 'done' to exit.")
// while(userInput != 'done'){
//   userNums.push(userInput)
//   userInput = prompt("Please enter a number or 'done' to exit.")
// }


// console.log(userNums)
// console.log(userInput)

// let nums = [5, 0, 8, 3, 4, 1, 6]
// let sum = 0

// for (let i = 0;  i < nums.length; i++) {
//     sum += nums[i]
//     console.log(nums[i])
// }
// console.log(sum)

// let averageNum = sum / nums.length
// console.log(averageNum)