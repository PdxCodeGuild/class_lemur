/*
card=""
while card == "":
    card=input("What is your first card? ")
    playercards= [card]
    if card in ("2","3","4","5","6","7","8","9","10"):
        card=int(card)
    # Face or Ace"
    elif card in ("A", "J", "Q", "K"):
        if card == "A":
            card=1
        else:
            card=10
    #not in deck
    else:
        print("not a standard card")
        card=""
total=card
hit=1
while hit:
    card=""
    while card == "":
        card=input("What is your next card? ")
        playercards.append(card)
        if card in ("2","3","4","5","6","7","8","9","10"):
            card=int(card)
        #Face or Ace
        elif card in ("A", "J", "Q", "K"):
            if card == "A":
                card=1
            else:
                card=10
        #not in deck
        else:
            print("not a standard card")
            card=""
    total+=card
    hit=0
    if total > 21:
        print(f"{playercards, total} You busted!")
    elif total == 21:
        print(f"{playercards, total} Blackjack!")
    elif total <17:
        print(f"{playercards, total} Hit!")
        hit=1
    else:
        print(f"{playercards, total} stay")
*/
// const button = document.querySelector('#button')
// console.log(button)
let cards=[]
let value1=0
let i=0
const output1=""
const faces=["10","J","Q","K"]

const button = document.querySelector('#button')
console.log(button)

const input1 = document.querySelector('#card1')
const input2 = document.querySelector('#card2')
const input3 = document.querySelector('#card3')
const test1 = input1.value
console.log(typeof input1.value)
console.log(input1.value.toUpperCase(),"input1")

const output = document.querySelector('#output')

button.addEventListener('click', function () {
    console.log(input1.value.toUpperCase(),"input1func")
    cards.push(input1.value.toUpperCase(),input2.value.toUpperCase(),input3.value.toUpperCase())
    while (true){
        if (faces.includes(cards[i])){
            value1+=10
        } else if (cards[i]=="A"){
            value1+=1
        } else {
            value1+=parseInt(cards[i])
        }
        console.log(value1, "value1")
        i+=1
        // console.log(cards, card)
        if (value1<17){
            output.innerText =`Hit   Your Cards: ${cards}` 
        } else if(value1>=17 && value1<=20){
            output.innerText =`Stay Your Cards: ${cards}`
            break
        } else if (value1==21){
            output.innerText =`BLACKJACK!!! Your Cards: ${cards}`
            break
        } else{
            output.innerText =`BUSTED!!! Your Cards: ${cards}`
            break
        }
    }    
})


