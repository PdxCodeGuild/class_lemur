function creditCardValidation(cardNumString){
    let cardNumSum = 0
    let cardNumList = cardNumString.split('');
    let checkDigit = cardNumList.pop()
    cardNumList.reverse()
    for (let i = 0; i < cardNumList.length; i += 2){
        cardNumList[i] = parseInt(cardNumList[i]) * 2
        if (cardNumList[i] > 9){
            cardNumList[i] -= 9
        }
    }
    for (let i = 0; i < cardNumList.length; i++){
        cardNumSum += +cardNumList[i]
    }
    let secondDigit = cardNumSum.toString()[1]
    checkIfValid(secondDigit, checkDigit)
}

function checkIfValid(secondDigit, checkDigit){
    if (secondDigit == checkDigit){
        alert("This is a valid number")
    }
    else {
        alert("This is NOT a valid number")
    }
}

function getInputNumber(){
    let searchTerm = prompt("Enter Credit Card Number")
    return searchTerm
}

creditCardValidation(getInputNumber())
// creditCardValidation("4556737586899855")