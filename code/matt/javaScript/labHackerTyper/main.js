const hackery = document.querySelector("#hackery")
const everything = document.querySelector("#everything")
const hack = document.querySelector("#hack")

function hackeythings() {
    let randomWords = ["sdav", "adsfgadrg", "fdbafba"]
    let random = document.createElement("p")
    random.className = "text-danger"
    random.appendChild(document.createTextNode(randomWords[Math.floor(Math.random() * randomWords.length)]))
    hackery.appendChild(random)
}

hack.addEventListener('keypress', hackeythings)