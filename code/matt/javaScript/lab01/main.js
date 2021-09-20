// make change elements
const changeBtn = document.querySelector('#make-change')
const dollars = document.querySelector('#dollars')
const changeOutput = document.querySelector('#change-output')

//pick 6 elements
const tickets = document.querySelector('#tickets')
const getLucky = document.querySelector('#get-lucky')
const roi = document.querySelector('#roi')


// ROT13 elements
const phrase = document.querySelector('#phrase')
const shift = document.querySelector('#shift')
const encode = document.querySelector('#encode')
const encodedPhraseOutput = document.querySelector('#encoded-phrase')

function makeChange() {
    cents = dollars.value * 100

    coins = {
        quarters: 25,
        dimes: 10,
        nickels: 5,
        pennies: 1
    }

    message = ''
    for (key in coins) {
        message += (`${Math.floor(cents / coins[key])} ${key} `)
        cents = cents % coins[key]
    }
    changeOutput.innerText = message
}

function randomTicket() {
    let i = 0
    ticket = []
    while (i < 6) {
        ticket.push(Math.floor(Math.random() * 10))
        i++
    }
    return ticket
}


function compareTicket(winningTicket, luckyTicket) {
    let i = 0
    let matches = 0
    while (i < 6) {
        if (luckyTicket[i] == winningTicket[i]) {
            matches++
        }
        i++
    }
    return matches
}

function pick6() {
    let winningTicket = randomTicket()
    console.log(winningTicket)
    let i = 0
    let expenses = 0
    let earnings = 0
    while (i < parseInt(tickets.value)) {
        expenses += 2
        let luckyTicket = randomTicket()
        switch (compareTicket(winningTicket, luckyTicket)) {
            case 1:
                earnings += 4
                break
            case 2:
                earnings += 7
                break
            case 3:
                earnings += 100
                break
            case 4:
                earnings += 50000
                break
            case 5:
                earnings += 1000000
                break
            case 6:
                earnings += 25000000
                break
        }
        i++
    }
    roi.innerText = `Earnings: ${earnings} 
    ROI: ${((earnings - expenses) / expenses)}`
}



function ROT13() {
    encodedPhrase = ''

    for (let i = 0; i < phrase.value.length; i++) {
        encodedPhrase += String.fromCharCode((parseInt(phrase.value[i].charCodeAt(0)) + parseInt(shift.value)))
    }
    encodedPhraseOutput.innerText = encodedPhrase
}

changeBtn.addEventListener('click', makeChange)

encode.addEventListener('click', ROT13)

getLucky.addEventListener('click', pick6)