
const button = document.querySelector('#button')

let one = document.querySelector('#card1')

let two = document.querySelector('#card2')

let three = document.querySelector('#card3')


const answer = document.querySelector('#answer')


button.addEventListener('click', function () {
    
    let output1 = one.value
    let output2 = two.value
    let output3 = three.value

    
    const faceCards = {
        J : 10,
        K : 10,
        Q : 10,
        A : 1
    }
    
    // console.log(card1)
    // console.log(card2)
    // console.log(card3)
    // console.log(faceCards.J)

    if (output1 in faceCards) {
        output1 = faceCards[output1]
        console.log(output1, 'output1')
    }
    
    if (output2 in faceCards) {
        output2 = faceCards[output2]
        console.log(output2, 'output2')

    } 
    
    if (output3 in faceCards) {
        output3 = faceCards[output3]
        console.log(output3, 'output3')

    } 

    final = parseInt(output1) + parseInt(output2) + parseInt(output3)

    if (final < 17) {
        answer.innerText = `Your total was ${final}. I think you should hit.`
    } else if (final >= 17 && final < 21) {
        answer.innerText = `Your total was ${final}. I think you should stay.`
    } else if (final == 21) {
        answer.innerText = `Your total was ${final}. Blackjack!`
    } else {
        answer.innerText = `Your total was ${final}. Already busted!`
    }
})


