const form = document.querySelector('form')
// const card1 = document.getElementById('card1')
// const card2 = document.querySelector('#card2')
const cardSelects = document.getElementsByTagName('select')
const adviceOutput = document.getElementById('advice-output')

// console.log(form, cardSelects, adviceOutput)

form.addEventListener('submit', function(evt) {
	evt.preventDefault()
	// console.log(evt)
	// console.log('hello')
	const total = (
		parseInt(cardSelects.card1.value)
		+ +cardSelects.card2.value // using + before is a shorthand for turning string-numbers into numbers
		+ parseInt(cardSelects.card3.value)
	)
	console.log(total)
	adviceOutput.innerText = `Your total is ${total}.`
	adviceOutput.innerHTML += '&nbsp;'  // html entity: non breaking space
	if (total < 17) {
		adviceOutput.innerText += 'You should hit.'
	} else if (total < 21) {
		adviceOutput.innerText += 'You should stay.'
	} else if (total === 21) {
		adviceOutput.innerText += 'Blackjack!'
	} else {
		adviceOutput.innerText += 'Bust...'
	}

})