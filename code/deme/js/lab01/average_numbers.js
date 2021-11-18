//                  Version 1
let numArray = [5, 0, 8, 3, 4, 1, 6]
let total = 0
let version1 = document.getElementById('version1')

for (let i = 0;  i < numArray.length; i++) {
    total = total + +numArray[i]
    console.log(numArray[i])
}
averageNum = document.createElement('p')
averageNum.innerHTML =(`For [5, 0, 8, 3, 4, 1, 6], the median is number is ${total / numArray.length}`)
version1.appendChild(averageNum)

//                  Version2
let numForm = document.getElementById('numForm')
let numList = document.getElementById('numList')
let resultDiv = document.getElementById('resultDiv')
let numListForm = document.getElementById('numListForm')
let numbers = document.getElementById('numbers')
let nums = []
let doneForm = document.getElementById('doneForm')
let sum = 0


numForm.addEventListener('submit', function(event) {
    event.preventDefault()
    let userNum = numListForm.value
    let numLi = document.createElement('li')
    numLi.innerHTML=userNum
    numList.appendChild(numLi)
    nums.push(numListForm.value)

})
doneForm.addEventListener('submit', function(event) {
    event.preventDefault()
    for(let i = 0; i < nums.length; i++){
        sum = sum + +nums[i]
    }
    sum = sum/nums.length
    resultDiv.innerText = `The average number is ${sum}.`;
    
})


