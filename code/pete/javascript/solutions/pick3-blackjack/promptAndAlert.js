const cardObj = {
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
	K: 10,
}


const card1 = prompt('Enter a card: ')
const card2 = prompt('Enter another card: ')
const card3 = prompt('Enter yet another card: ')

const cards = [card1, card2, card3]

let total = 0

for (let i = 0; i < cards.length; i++) {
	const card = cards[i]
	total += cardObj[card]
}

// Array.forEach alternatives:
// cards.forEach(function (card) {
// 	total += cardObj[card]
// })

// cards.forEach(card => total += cardObj[card])

alert(`Your total is: ${total}`)

if (total < 17) {
	alert('hit')
} else if (total < 21) {
	alert('stay')
} else if (total === 21) {
	alert('blackjack')
} else {
	alert('bust')
}