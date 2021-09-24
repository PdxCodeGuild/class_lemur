changeForm = document.getElementById("changeForm")
userChange = document.getElementById("userChange")
changeDiv = document.getElementById('changeDiv')

// let total = prompt("Enter amount: ")

// total = total * 100


 
changeForm.addEventListener('submit', function(event) {
    event.preventDefault()
    let total = userChange.value * 100
    quarters = Math.floor(total / 25) 
    dimes = Math.floor((total -(quarters* 25)) / 10)
    nickels = Math.floor(((total - (quarters * 25)) - (dimes * 10)) / 5)
    pennies = Math.floor(((total - (quarters * 25)) - (dimes * 10)) - (nickels * 5) / 1)
    change = `Your change is: ${quarters} quarters, ${dimes} dimes, ${nickels} nickels, ${pennies} pennies.`
    let changeAmount = document.createElement('p')
    changeAmount.innerHTML = change
    changeDiv.appendChild(changeAmount)
   
    // let changeAmount = document.createElement('p')
        // changeAmount.innerHTML=userNum
        // numList.appendChild(numLi)
        // nums.push(numListForm.value)

    })

// const coins = ['quarter', 'dime', 'nickel']
// for(let i =0; i<coins.length; i++){

// }

