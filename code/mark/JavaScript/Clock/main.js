let clock = document.querySelector('#clock')
let stopWatch = document.querySelector('#stopWatch')
let countdownTimer = document.querySelector('#countdown')
let startButton = document.querySelector("#startStopWatch")
let stopButton = document.querySelector("#stopStopWatch")
let resetButton = document.querySelector("#clearStopWatch")
let lapButton = document.getElementById("lapStopWatch")
let startCountdownButton = document.getElementById("startCountdown")
let countdownHours = document.getElementById("hours")
let countdownMinutes = document.getElementById("minutes")
let countdownSeconds = document.getElementById("seconds")
let clockSection = document.getElementById('clockSection')
let stopwatchSection = document.getElementById('stopwatchSection')
let countdownSection = document.getElementById('countdownSection')
let clockButton = document.getElementById('clockButton')
let stopwatchButton = document.getElementById('stopwatchButton')
let countdownButton = document.getElementById('countdownButton')
let increaseStopWatch = null
let alreadyStartedCountdown = false
let count = 0
let seconds = 0
let totalTime = 0
let stopWatchTime = new Date(seconds * 1000).toISOString().substr(11, 8);
let countdownStart = new Date(totalTime * 1000).toISOString().substr(11, 8);

stopWatch.innerText = stopWatchTime
countdownTimer.innerText = countdownStart

function logTime() {
    let dateTime = new Date();
    clock.innerText = dateTime
}

function startStopWatchTime() {
    increaseStopWatch = setInterval( function (){
        seconds += 1
        stopWatchTime = currentTime()
        stopWatch.innerText = stopWatchTime
    }, 1000)
}
function stopStopWatchTimer() {
    clearInterval(increaseStopWatch)
}

function currentTime() {
    let stopWatchTime = new Date(seconds * 1000).toISOString().substr(11, 8);
    return stopWatchTime
}

function clearStopWatch() {
    seconds = 0
    let stopWatchTime = new Date(seconds * 1000).toISOString().substr(11, 8);
    stopWatch.innerText = stopWatchTime
    let lapList = document.getElementById("lapList")
    while (lapList.firstChild) {
        lapList.firstChild.remove()
    }
}

function addLapTime() {
    let lapList = document.getElementById("lapList")
    let listItem = document.createElement("li")

    listItem.className = "list-group-item"
    listItem.innerText = stopWatchTime

    lapList.appendChild(listItem)
}

function startCountdown() {
    
    if (alreadyStartedCountdown == false){
        if (!countdownHours.value) {
            hours = 0
        }
        else {
            hours = parseInt(countdownHours.value)
        }
        if (!countdownMinutes.value) {
            minutes = 0
        }
        else {
            minutes = parseInt(countdownMinutes.value)
        }
        if (!countdownSeconds.value) {
            seconds = 0
        }
        else {
            seconds = parseInt(countdownSeconds.value)
        }
        totalTime = (seconds + (minutes * 60) + (hours * 3600))
        let countdownStart = new Date(totalTime * 1000).toISOString().substr(11, 8);
        countdownTimer.innerText = countdownStart
        let decreaseCountdown = setInterval(function () {
            if (totalTime === 0) {
                clearInterval(decreaseCountdown)
                alreadyStartedCountdown = !alreadyStartedCountdown
                let flashBackground = setInterval(function () {
                    if (count === 8) {
                        clearInterval(flashBackground)
                        document.body.style.background = 'white'
                        count = 0
                    }
                    else if (count % 2 === 1) {
                        document.body.style.background = 'white'
                        count += 1
                    }
                    else {
                        document.body.style.background = 'red'
                        count += 1
                    }
                }, 250)
            }
            else {
                totalTime -= 1
                let countdownStart = new Date(totalTime * 1000).toISOString().substr(11, 8);
                countdownTimer.innerText = countdownStart
            }
        }, 1000)
        alreadyStartedCountdown = !alreadyStartedCountdown
    }
}

function showClock() {
    fadeInEffect(clockSection)
    fadeOutEffect(countdownSection)
    fadeOutEffect(stopwatchSection)
    clockButton.className = "btn btn-danger m-2"
    stopwatchButton.className = "btn btn-primary m-2"
    countdownButton.className = "btn btn-primary m-2"
}

function showStopwatch() {
    fadeInEffect(stopwatchSection)
    fadeOutEffect(clockSection)
    fadeOutEffect(countdownSection)
    clockButton.className = "btn btn-primary m-2"
    stopwatchButton.className = "btn btn-danger m-2"
    countdownButton.className = "btn btn-primary m-2"
}

function showCountdown() {
    fadeInEffect(countdownSection)
    fadeOutEffect(clockSection)
    fadeOutEffect(stopwatchSection)
    clockButton.className = "btn btn-primary m-2"
    stopwatchButton.className = "btn btn-primary m-2"
    countdownButton.className = "btn btn-danger m-2"
}

function fadeOutEffect(fadeTarget) {
    let outEffect = setInterval(function () {
        if (fadeTarget.style.opacity > 0) {
            fadeTarget.style.opacity -= 0.01
        }
        else {
            clearInterval(outEffect)
        }
    }, 5)
}

function fadeInEffect(fadeTarget) {
    let inEffect = setInterval(function () {
        if (fadeTarget.style.opacity < 1) {
            fadeTarget.style.opacity = parseFloat(fadeTarget.style.opacity) + .01
        }
        else {
            clearInterval(inEffect)
        }
    }, 5)
}


setInterval(logTime, 1000)
startButton.addEventListener('click', startStopWatchTime)
stopButton.addEventListener('click', stopStopWatchTimer)
resetButton.addEventListener('click', clearStopWatch)
lapButton.addEventListener('click', addLapTime)
startCountdownButton.addEventListener('click', startCountdown)
clockButton.addEventListener('click', showClock)
stopwatchButton.addEventListener('click', showStopwatch)
countdownButton.addEventListener('click', showCountdown)
