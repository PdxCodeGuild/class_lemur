/*
make change
*/

const coins = {
    quarter: 25,
    dime: 10,
    nickel: 5,
    penny: 1
}

const coinNames = ['quarter', 'dime', 'nickel', 'penny']
for (let i = 0; i< coinNames.length; i ++) {
    let coin = coinNames[i]
    let coinValue = coins[coin]
    console.log(coin, coinValue)
}

let usersChange = prompt("enter change amount")


function change(userChange) {
    let pennies = userChange * 100
    Math.floor(pennies)

    let quarters = Math.floor(pennies / 25)
    pennies = pennies - (quarters*25)
    
    let dimes = Math.floor(pennies/10)
    pennies = pennies - (dimes*10)

    let nickels = Math.floor(pennies/5)
    pennies = pennies - (nickels*5)

    return {quarters, dimes, nickels, pennies}
}
const changeData = change(usersChange)
alert(`${changeData.quarters}` + " quarters remain.")
alert(`${changeData.dimes}` + " dimes remain.")
alert(`${changeData.nickels}` + " nickles remain.")
alert(`${changeData.pennies}` + " pennies remain.")



/*
step 1: user enters dollar change amount
step 2: convert amount by 100 to get all pennies
step 3: floor divide to isolate remainder
step 4: with remainder, divide by highest coin
step 5: continue to ==0
return total and 'alert'
*/