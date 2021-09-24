const button = document.querySelector('#button')


const input1 = document.querySelector('#cash')


const Output = document.getElementById('output')
const cents = [
	{name:"tens", value: 1000},
    {name:"fives", value: 500},
    {name:"ones", value:100},
	{name:"half-dollars", value: 50},
	{name:"quarters", value:25},
	{name:"dimes", value: 10},
	{name:"nickels", value: 5},
	{name:"pennies", value: 1}
]
// console.log(cents.length)
function count(x, y){
    let div= Math.floor((x)/y)
    // console.log(div,"counting")
    return div
}
function rem(x, y){
    let rmdr=Math.round((x)%y)
    // console.log(rmdr,"rmdr")
    return rmdr
}

button.addEventListener('click', function () {
    Output.innerText ="Your total is: \n"
    let cash=100*input1.value
    for (let i = 0; i< cents.length; i++){
        const coin=cents[i]
        let counted = count(cash,coin.value) 
        cash= rem(cash,coin.value)
        if (counted){
            Output.innerText+= `${counted} ${coin.name}\n`       
        }
    }
})