const time = document.querySelector("#time")

const stopWatchTime = document.querySelector("#stop-watch")
const startBtn = document.querySelector("#start")
const stopBtn = document.querySelector("#stop")
const lapBtn = document.querySelector("#lap")
const laps = document.querySelector("#laps")
const resetBtn = document.querySelector("#reset")

const timeInput = document.querySelector("#time-input")
const startCoundownBtn = document.querySelector("#start-countdown")
const countdownOutput = document.querySelector("#countdown")

function clock() {
    const date = new Date()
    time.innerText = date.toLocaleTimeString()
}

setInterval(clock, 1000)

const date = new Date()
date.setHours(0, 0, 0, 0)

function startWatch() {
    date.setMilliseconds(date.getMilliseconds() + 11)
    m = date.getMinutes()
    s = date.getSeconds()
    ms = date.getMilliseconds()
    stopWatchTime.innerText = `${m} : ${s} : ${ms}`
    timer = setTimeout(startWatch, 10)

}

function stopWatch() {
    clearTimeout(timer)
}

function setLap() {
    let newlap = document.createElement("li")
    newlap.className = "list-group-item border-0"
    newlap.appendChild(document.createTextNode(`${date.getMinutes()} : ${date.getSeconds()} : ${date.getMilliseconds()}`))
    laps.appendChild(newlap)
}

function resetStopWatch() {
    clearTimeout(timer)
    date.setHours(0, 0, 0, 0)
    stopWatchTime.innerHTML = '0 : 0 : 0'
    while (laps.firstChild) {
        laps.removeChild(laps.firstChild)
    }
}

function getTimeOption() {
    const timeId = document.querySelector("#time-input")
    const timeNum = document.querySelector("#time-num")
    return [timeId, timeNum]
}

function startCountdown() {
    let time = getTimeOption()
    let timeId = time[0].value
    let timeNum = parseInt(time[1].value)

    countdownTime = new Date()
    countdownTime.setHours(0, 0, 0, 0)

    h = countdownTime.getHours()
    m = countdownTime.getMinutes()
    s = countdownTime.getSeconds()

    if (timeId === 'seconds') {
        countdownTime.setHours(0, 0, timeNum, 0)
    } else if (timeId === 'minutes') {
        countdownTime.setHours(0, timeNum, 0, 0)
    } else if (timeId === 'hours') {
        countdownTime.setHours(timeNum, 0, 0, 0)
    }

    countdown = setInterval(countdownUpdate, 1000)
    countdownOutput.innerHTML = `${h} : ${m} : ${s}`
}

function countdownUpdate() {
    h = countdownTime.getHours()
    m = countdownTime.getMinutes()
    s = countdownTime.getSeconds()

    countdownTime.setMilliseconds(countdownTime.getMilliseconds() - 1000)
    countdownOutput.innerHTML = `${h} : ${m} : ${s}`

    if (countdownTime.getSeconds() === 0 && countdownTime.getMinutes() === 0 && countdownTime.getHours() === 0) {
        clearInterval(countdown)
        alert("Countdown ended")
    }
}


startBtn.addEventListener('click', startWatch)

stopBtn.addEventListener('click', stopWatch)

lapBtn.addEventListener('click', setLap)

resetBtn.addEventListener('click', resetStopWatch)

timeInput.addEventListener('change', getTimeOption)

startCoundownBtn.addEventListener('click', startCountdown)