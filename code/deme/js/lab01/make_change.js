let total = prompt("Enter amount: ")

total = total * 100
quarters = Math.floor(total / 25) 
dimes = Math.floor((total -(quarters* 25)) / 10)
nickels = Math.floor(((total - (quarters * 25)) - (dimes * 10)) / 5)
pennies = Math.floor(((total - (quarters * 25)) - (dimes * 10)) - (nickels * 5) / 1)
console.log(`${quarters} quarters, ${dimes} dimes, ${nickels} nickels, ${pennies} pennies.`)