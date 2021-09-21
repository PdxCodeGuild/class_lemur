
const button = document.querySelector('#button')

const card1 = document.querySelector('#card1')
const card2 = document.querySelector('#card2')
const card3 = document.querySelector('#card3')

const answer = document.querySelector('#answer')



button.addEventListener('click', function () {
    
    faceCards = {
        J : 10,
        K : 10,
        Q : 10,
        A : 1
    }

    if (card1 in faceCards) {
        card1 = faceCards[card1] 
    }
    
    else if (card2 in faceCards) {
        card2 = faceCards[card2]
    } 
    
    else if (card3 in faceCards) {
        card3 = faceCards[card3]
    } 

    console.log(card1.value)
    console.log(card2.value)
    console.log(card3.value)
    
    // answer.innerText = parseInt(card1.value) + parseInt(card2.value) + parseInt(card3.value)
    answer.innerText = card1.value + card2.value + card3.value

    // if (answer.innerHTML < 17) {
    //     console.log(`Your total was ${answer.innerHTML}. I think you should hit.`)
    // } else if (answer.innerHTML >= 17 && answer.innerHTML < 21) {
    //     console.log(`Your total was ${answer.innerHTML}. I think you should stay.`)
    // } else if (answer.innerHTML == 21) {
    //     console.log(`Your total was ${answer.innerHTML}. Blackjack!`)
    // } else {
    //     console.log(`Your total was ${answer.innerHTML}. Already busted!`)
    // }
})


