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
    let firstCard = document.querySelector("#card1").value.toUpperCase()
    let secondCard = document.querySelector("#card2").value.toUpperCase()
    let thirdCard = document.querySelector("#card3").value.toUpperCase()
    return cardArray[firstCard] + cardArray[secondCard] + cardArray[thirdCard]
}

function giveAdvice(){
    handValue = getResult()
    if (handValue < 17){
        output.innerText = `${handValue}: Hit`
    }
    else if (handValue < 21){
        output.innerText = `${handValue}: Stay`
    }
    else if (handValue == 21){
        output.innerText = `${handValue}: Blackjack!`
    }
    else{
        output.innerText = `${handValue}: Already Busted`
    }
}

button.addEventListener('click', giveAdvice)

