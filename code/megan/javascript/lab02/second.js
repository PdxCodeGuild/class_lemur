// Part one 

function linear_search(nums, value) {

    for (let i = 0; i < nums.length; i++) {
    
        if (nums[i] === value) {
            return i
        }
    }
}

nums = [1, 2, 3, 4, 5, 6, 7, 8]

// let index = linear_search(nums, 7)

// const button = document.querySelector('#button1')

// const one = document.querySelector('#one')
// const two = document.querySelector('#two')
// const three = document.querySelector('#three')
// const four = document.querySelector('#four')
// const five = document.querySelector('#five')
// const six = document.querySelector('#six')

// const nums = document.querySelector('#nums')

// button.addEventListener('click', function () {
//     console.log(one.value, two.value, three.value, four.value, five.value, six.value)
    
//     // let index = linear_search(nums.innerText, 7)

//     Array.from(nums.innerText = one.value + two.value + three.value + four.value + five.value + six.value, 7)

// })


// const button = document.querySelector('#button2')

const input1 = document.querySelector('#input1')

// button.addEventListener('click', function () {

//     console.log(input1.value)
//     answer.innerText = linear_search(nums, parseInt(input1.value))

// })




// Part two

function binary_search(nums, value) {

    nums.sort()

    let low = 0
    let high = nums.length - 1

    console.log(low, high)

    let counter = 0

    while (low < high) {

        counter ++ 
        let mid = Math.floor(high + low)
        console.log({
            low, mid, high
        })

        if (counter === 10) {
            return
        }

        for (let i = 0; i < nums.length; i++) {

            if (value === nums[0]) {
                return 0
            } 
            else if (nums[mid] === value) {
                return mid 
            }

            else if (value < nums[mid]) {
                high = mid - 1
            }

            else if (value > nums[mid]) {
                low = mid + 1
            }
        }

    }
}

// let nums = [1, 2, 3, 4, 5, 6, 7, 8]

// let index1 = binary_search(nums, 7)
// console.log(index1)

const button = document.querySelector('#button2')

const input2 = document.querySelector('#input2')

button.addEventListener('click', function () {

    console.log(input1.value)
    answer.innerText = linear_search(nums, parseInt(input1.value))

    console.log(input2.value)
    answer2.innerText = linear_search(nums, parseInt(input2.value))

})
