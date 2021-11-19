const form = document.querySelector('form')
const cardOpt = document.getElementsByTagName('select')
const adviceOutput = document.getElementById('advice-output')

form.addEventListener('submit', function(evt) {
    evt.preventDefault()
    console.log(evt)
    const total = (
        parseInt(cardOpt.card1.value)
        + +cardOpt.card2.value
        + parseInt(cardOpt.card3.value)
    )
    console.log(total)
    adviceOutput.innerText = `You have ${total} points in your hand.`
    adviceOutput.innerHTML += '&nbsp;'
    if (total < 17) {
        adviceOutput.innerText += 'hit'
    } else if (total < 21) {
        adviceOutput.innerText += 'stay'
    } else if (total === 21) {
        adviceOutput.innerText += 'blackjack winner'
    } else {
        adviceOutput.innerText += 'bust'
    }

})