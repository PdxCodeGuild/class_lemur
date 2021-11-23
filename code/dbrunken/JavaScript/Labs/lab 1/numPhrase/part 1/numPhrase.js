//convert numbers to words

let nums01s = {
    0: '',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
}

let teens = {
    10: 'ten',
    12: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen'
}
let nums10s = {
    0: '',
    1: '',
    2:'twenty',
    3:'thirty',
    4:'forty',
    5:'fifty',
    6:'sixty',
    7:'seventy',
    8:'eighty',
    9:'ninety'
}

let x = prompt('give a number: ')
function convert (num) {
    
    let place100 = Math.floor(x)
    let place10 = Math.floor(x % 100)
    let place1 = x % 10

    const ones =  nums01s[place1]
    const tens = nums10s[place10]
    const hundreds = nums01s[place100]

    // console.log(x.length)
    if (num.length == 1) {
       alert(nums01s[num])
        // alert('hi')
    } else if (num.length == 2) {
        //console.log('work', num)
        if (num > 9 && num < 20  ) {
           alert(teens[num])
        } else if (num > 19 && num < 99) {
           alert(nums10s[num] + nums01s[num])
        }
    } else if (num.length == 3){
        if (num[1] > 9 && num[1] < 20) {
           alert(nums01s[num[0]] + teens[num])
        } else if (num[1] > 19 && num[1] < 99) {
           alert(nums01s[num[0]] + nums10s[num] + nums01s[num])
        }
    }
    
    // if (x === 0) {
    //     alert('zero')
    // } else if (x < 100) {
        // if (place10 === 1) {
        //     let teen = teens[place1]
        //     return teen
        // }
        // return tens + '-' + ones


    // } else if (place10 ===1) {
    //     let tens1 = teens[place1]
    //     return hundreds + 'hundred' + tens1
    // }
    // return hundreds + 'hundred' + tens1 + '-' + ones
}

convert(x)