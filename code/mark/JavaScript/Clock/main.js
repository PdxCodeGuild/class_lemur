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
let increaseStopWatch = null
let decreaseCountdown = null
let seconds = 0
let totalTime = 0
let stopWatchTime = new Date(seconds * 1000).toISOString().substr(11, 8);
stopWatch.innerText = stopWatchTime
let countdownStart = new Date(totalTime * 1000).toISOString().substr(11, 8);
countdownTimer.innerText = countdownStart

function logTime (){
    let dateTime = new Date();
    clock.innerText= dateTime
}

function startStopWatchTime(){
    increaseStopWatch = setInterval(increaseTime, 1000)
}
function stopStopWatchTimer(){
    clearInterval(increaseStopWatch)
}

function increaseTime(){
    seconds += 1
    stopWatchTime = currentTime()
    stopWatch.innerText = stopWatchTime
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
    hours = parseInt(countdownHours.value)
    minutes = parseInt(countdownMinutes.value)
    seconds = parseInt(countdownSeconds.value)
    totalTime = (seconds + (minutes * 60) + (hours * 3600))
    let countdownStart = new Date(totalTime * 1000).toISOString().substr(11, 8);
    countdownTimer.innerText = countdownStart
    decreaseCountdown = setInterval(countdown, 1000)
}

function countdown() {
    if (totalTime === 0){
        console.log("BOOM")
        clearInterval(decreaseCountdown)
    }
    else {
        totalTime -= 1
        let countdownStart = new Date(totalTime * 1000).toISOString().substr(11, 8);
        countdownTimer.innerText = countdownStart
    }
}

setInterval(logTime, 1000)
startButton.addEventListener('click', startStopWatchTime)
stopButton.addEventListener('click', stopStopWatchTimer)
resetButton.addEventListener('click', clearStopWatch)
lapButton.addEventListener('click', addLapTime)
startCountdownButton.addEventListener('click', startCountdown)