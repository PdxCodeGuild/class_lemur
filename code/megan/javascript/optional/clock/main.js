// Version One 

time = document.getElementById('time')
date = document.getElementById('date')

setTimeout(currentTime, 0)
setInterval(currentTime, 1000);

function currentTime() {

    let d = new Date()
    time.innerHTML = d.toDateString()
    let t = new Date()
    date.innerHTML = t.toLocaleTimeString()

}

// Version Two

const start = document.getElementById('start')
const stop = document.getElementById('stop')
const lap = document.getElementById('lap')

// let hours = 0 
// let minutes = 0
// let seconds = 0

let stopwatch = document.getElementById('stopwatch')

start.addEventListener('click', function () {
    
    function stopWatch() {
        
        let begin = new Date().getTime()
        // begin.setHours(0, 0, 0, 0)
        let answer = stopwatch.innerHTML = '00:00:00'
        console.log(answer)
    }

    function startTimer() {
        seconds++
        if (seconds >= 60) {
            seconds = 0 
            minutes ++
            if (minutes >= 60) {
                minutes = 0
                hours++ 
                if (hours >= 12 ) {
                    hours = 0
                }
            }
        } 
    }
    
    going = setInterval(stopWatch, 1000)

})


stop.addEventListener('click', function () {
    clearInterval(going)
})

 
