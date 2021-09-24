const button = document.querySelector('#button')

const Output = document.getElementById('output')
const prizes = [0,4,7,100,50000,1000000,25000000]
let cost=0
let won=0

function pick6(){
    let picks=[]
    for(let i=0; i<6;i++){
        picks.push(Math.round(100*Math.random()))
    }
    return picks
}
function checking(ticket, pulled){
    let matches=0
    for(let i=0; i<6;i++){
        if (pulled[i]==ticket[i]){
            matches+=1
        }
    }
    let cash=prizes[matches]
    return cash
}

button.addEventListener('click', function () {
    
    for (let i=0;i<100000;i++){
        cost+=2
        let ticket_win=checking(pick6(),pick6())
        won+=ticket_win
    }
    let roi=Math.round(100*(won-cost)/cost)
    Output.innerText =`Your total winnings are: $${won} \n`
    Output.innerText +=`You spent:  $${cost} \n`
    Output.innerText +=`Your ROI is: ${roi}%`
})