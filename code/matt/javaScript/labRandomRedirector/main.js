countdown = document.querySelector("#countdown")

let time = 5

function whereToGo() {
    time--
    countdown.innerText = time

    let urls = ["https://puginarug.com/",
        "https://mondrianandme.com/",
        "https://www.codewars.com/",
        "https://longdogechallenge.com/",
        "https://thatsthefinger.com/"
    ]
    if (time === 0) {
        let chosenOne = Math.floor(Math.random() * urls.length)
        window.location = urls[chosenOne]
    }
}

setInterval(whereToGo, 1000)
