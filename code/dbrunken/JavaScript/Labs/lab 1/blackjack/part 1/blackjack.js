// give advice on blackjack

let deck = {
    'A' : 1,
    2 : 2,
    3 : 3,
    4 : 4,
    5 : 5,
    6 : 6,
    7 : 7,
    8 : 8,
    9 : 9,
    10 : 10,
    'J' : 10,
    'Q' : 10,
    'K' : 10,
}

const card1 = prompt('enter first card ')
const card2 = prompt('enter second card ')
const card3 = prompt('enter third card ')

const hand = [card1, card2, card3]

let total = 0

for (let i=0; i<3; ++i) {
    total += deck[hand[i]]
}

alert('your total is: ' + total)

if (total < 17) {
    alert('hit')
} else if (total < 21) {
    alert('stay')
} else if (total === 21) {
    alert('blackjack')
} else {
    alert('bust')
}