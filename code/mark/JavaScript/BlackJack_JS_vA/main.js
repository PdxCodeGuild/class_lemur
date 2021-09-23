let cardArray = {
    A: 1,
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 8,
    9: 9,
    10: 10,
    J: 10,
    Q: 10,
    K: 10
}
function getResult() {
    let firstCard = prompt("First Card").toUpperCase()
    let secondCard = prompt("Second Card").toUpperCase()
    let thirdCard = prompt("Third Card").toUpperCase()
    return cardArray[firstCard] + cardArray[secondCard] + cardArray[thirdCard]
}

function giveAdvice(handValue){
    if (handValue < 17){
        alert(`${handValue}: Hit`)
    }
    else if (handValue < 21){
        alert(`${handValue}: Stay`)
    }
    else if (handValue == 21){
        alert(`${handValue}: Blackjack!`)
    }
    else{
        alert(`${handValue}: Already Busted`)
    }
}

giveAdvice(getResult())