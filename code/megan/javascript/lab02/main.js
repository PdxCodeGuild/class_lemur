// Part one 

// function linear_search(nums, value) {

//     for (let i = 0; i < nums.length; i++) {
    
//         if (nums[i] === value) {
//             return i
//         }
//     }
// }

// let nums = [1, 2, 3, 4, 5, 6, 7, 8]
// let index = linear_search(nums, 7)

// console.log(index) 
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

let nums = [1, 2, 3, 4, 5, 6, 7, 8]

let index1 = binary_search(nums, 7)
console.log(index1)