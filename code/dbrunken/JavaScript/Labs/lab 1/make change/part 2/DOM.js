let userInput = document.getElementById('change')
let userBtn = document.getElementById('button')

let moneyDict = {
    'quarter' : .25,
    'dime' : .10,
    'nickel': .05,
    'penny':  .01
}

userBtn.onclick= function makeChange1()
    // function makeChange() {
    //     let valueIn = userInput.value
    //     console.log(valueIn)
    // }
    {
        let inputValue = userInput.value

        let selected_currency = document.getElementById('select').value
        if (selected_currency === 'pennies') {
            answer = inputValue * 100
            document.getElementById('makeChange').innerHTML = Math.floor(answer)
        } else if (selected_currency === 'nickles') {
            answer = inputValue * 5
            document.getElementById('makeChange').innerHTML = Math.floor(answer)
        } else if (selected_currency === 'dimes') {
            answer = inputValue * 10
            document.getElementById('makeChange').innerHTML = Math.floor(answer)
        } else if (selected_currency === 'quarters') {
            answer = inputValue * 25
            document.getElementById('makeChange').innerHTML = Math.floor(answer)
        } else if (selected_currency == 'all') {
            userInput = inputValue
        
            let pennies = userInput * 100                    
            Math.floor(pennies)
            
            let quarters = Math.floor(pennies / 25)
            pennies = pennies - (quarters*25)
            
            let dimes = Math.floor(pennies/10)
            pennies = pennies - (dimes*10)

            let nickels = Math.floor(pennies/5)
            pennies = pennies - (nickels*5)
            
            console.log(quarters, dimes, nickels, pennies)
            
            let answer = (`${quarters}` + " quarters remain." + `${dimes}` + " dimes remain." + `${nickels}` + " nickles remain." + `${pennies}` + " pennies remain.")
            
            document.getElementById('makeChange').innerHTML= answer
        }
    }

    // function makeChange(userChange) {
    //     let pennies = userChange * 100
    //     Math.floor(pennies)
    
    //     let quarters = Math.floor(pennies / 25)
    //     pennies = pennies - (quarters*25)
        
    //     let dimes = Math.floor(pennies/10)
    //     pennies = pennies - (dimes*10)
    
    //     let nickels = Math.floor(pennies/5)
    //     pennies = pennies - (nickels*5)
    
    //     return {quarters, dimes, nickels, pennies}
    // }
    // const changeData = makeChange(userInput)
    // makeChange.innerText = (`${changeData.quarters}` + " quarters remain.")
    // makeChange.innerText = (`${changeData.dimes}` + " dimes remain.")
    // makeChange.innerText = (`${changeData.nickels}` + " nickles remain.")
    // makeChange.innerText = (`${changeData.pennies}` + " pennies remain.")