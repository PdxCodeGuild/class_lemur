const everything = document.querySelector("#everything")
const hack = document.querySelector("#hack")
const access = document.querySelector("#access")
const danger = document.querySelector("#danger")
const error = document.querySelector("#error")
const stopNow = document.querySelector("#stop")

function accessMessage() {
    access.className = "bg-dark text-danger text-center border border-danger"
}
function closeAccessMessage() {
    access.className = "bg-dark visually-hidden text-danger text-center border border-danger"
}
function dangerMessage() {
    danger.className = "bg-dark text-danger text-center border border-danger"
}
function closeDangerMessage() {
    danger.className = "bg-dark visually-hidden text-danger text-center border border-danger"
}
function errorMessage() {
    error.className = "bg-dark text-danger text-center border border-danger"
}
function closeErrorMessage() {
    error.className = "bg-dark visually-hidden text-danger text-center border border-danger"
}
function stopnowMessage() {
    stopNow.className = "bg-dark text-danger text-center border border-danger"
}
function closeStopnowMessage() {
    stopNow.className = "bg-dark visually-hidden text-danger text-center border border-danger"
}

aS = setInterval(accessMessage, 7000)
aE = setInterval(closeAccessMessage, 10000)

dS = setInterval(dangerMessage, 5000)
dE = setInterval(closeDangerMessage, 7500)

eS = setInterval(errorMessage, 2000)
eE = setInterval(closeErrorMessage, 4000)

sS = setInterval(stopnowMessage, 9000)
sE = setInterval(closeStopnowMessage, 14000)



function hackeythings() {
    let randomWords = ["Code ", " print() ", " hack ", "\r\n", " access ", " denied ", " error ", " granted "]
    random = randomWords[Math.floor(Math.random() * randomWords.length)]
    hack.value += random
    // if (hack.value.length > 500) {
    //     access.className = "bg-dark text-danger text-center border border-danger"
    // }
    // if (hack.value.length > 750) {
    //     access.className = "bg-dark visually-hidden text-danger text-center border-0"
    // }
    // if (hack.value.length > 1000) {
    //     danger.className = "bg-dark text-danger text-center border border-danger"
    // }
    // if (hack.value.length > 1250) {
    //     access.className = "bg-dark text-danger text-center border-0"
    //     error.className = "bg-dark text-danger text-center border border-danger"
    // }
    // if (hack.value.length > 1500) {
    //     access.className = "bg-dark visually-hidden text-danger text-center border-0"
    //     error.className = "bg-dark visually-hidden text-danger text-center border border-danger"
    //     stopNow.className = "bg-dark text-danger text-center border border-danger"
    // }
    // if (hack.value.length > 1750) {
    //     access.className = "bg-dark visually-hidden text-danger text-center border-0"
    //     danger.className = "bg-dark visually-hidden text-danger text-center border border-danger"
    // }
    // if (hack.value.length > 2000) {
    //     access.className = "bg-dark visually-hidden text-danger text-center border-0"
    //     stopNow.className = "bg-dark visually-hidden text-danger text-center border-0"
    // }
    // if (hack.value.length > 2500) {
    //     access.className = "bg-dark text-danger text-center border border-danger"
    //     error.className = "bg-dark text-danger text-center border border-danger"
    //     stopNow.className = "bg-dark text-danger text-center border border-danger"
    //     danger.className = "bg-dark text-danger text-center border border-danger"
    // }
    if (hack.value.length > 3200) {
        clearInterval(aS)
        clearInterval(dS)
        clearInterval(eS)
        clearInterval(sS)

        error.className = "bg-dark visually-hidden text-danger text-center border-0"
        stopNow.className = "bg-dark visually-hidden text-danger text-center border-0"
        danger.className = "bg-dark visually-hidden text-danger text-center border-0"
        access.className = "bg-dark text-success text-center border border-success"
        access.innerHTML = "Access Granted"
        hack.className = "form-control bg-dark text-success"
    }

    hack.scrollTop = hack.scrollHeight
    console.log(hack.value.length)
}


hack.addEventListener('keypress', function (event) {
    event.preventDefault()
})

hack.addEventListener('keypress', hackeythings)