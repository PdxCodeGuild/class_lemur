// Version One 

time = document.getElementById('time')
date = document.getElementById('date')


function currentTime() {

    let d = new Date()
    time.innerHTML = d.toDateString()
    let t = new Date()
    date.innerHTML = t.toLocaleTimeString()
}

setTimeout(currentTime, 0)
setInterval(currentTime, 1000);

// Version Two

const start = document.getElementById('start')
const stop = document.getElementById('stop')
const lap = document.getElementById('lap')

let stopwatch = document.getElementById('stopwatch')

start.addEventListener('click', function () {

    let starting = new Date().setHours(0, 0, 0, 0)
    stopwatch.innerHTML = starting
})

// stop.addEventListener('click', function () {
//     stopwatch.innerHTML = 'bye'

// })

setInterval(start, 1000);
