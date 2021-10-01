faceCards = {
    J : 10,
    K : 10,
    Q : 10,
    A : 1
}

console.log(prompt('Please select three cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K):'))

first = prompt("What's your first card?")

second = prompt("What's your second card?")

third = prompt("What's your third card?")

if (first in faceCards) {
    first = faceCards[first]
} 

if (second in faceCards) {
    second = faceCards[second]
} 

if (third in faceCards) {
    third = faceCards[third]
} 


total = parseInt(first) + parseInt(second) + parseInt(third)
console.log(total)

if (total < 17) {
    console.log(`Your total was ${total}. I think you should hit.`)
} else if (total >= 17 && total < 21) {
    console.log(`Your total was ${total}. I think you should stay.`)
} else if (total == 21) {
    console.log(`Your total was ${total}. Blackjack!`)
} else {
    console.log(`Your total was ${total}. Already busted!`)
}