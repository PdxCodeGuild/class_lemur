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
    11: 'eleven',
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
        console.log('work', num[0])
        if (num > 9 && num < 20  ) {
           alert(teens[num])
           document.getElementById('answer').innerHTML = teens[num]
        } else if (num > 19 && num < 100) {
            let x = num[0]
            let y = num[1]
            console.log(x,y)
           alert(nums10s[x] + nums01s[y])
           document.getElementById('answer').innerHTML =nums10s[x] + nums01s[y]
        }
    } else if (num.length == 3){
        let a = num[0]
        let b = num[1]
        let teen_num = 1 +b
        let c = num[2]
        console.log(num > 99)
        if (num > 99) {
            console.log(b)
            if (b > 1 && b != 0) {
                alert(nums01s[a] + ' hundred ' + nums10s[b] + nums01s[c])
                document.getElementById('answer').innerHTML = nums01s[a] + ' hundred ' + nums10s[b] + nums01s[c]
            }
            if (b == 0){
                alert(nums01s[a] + ' hundred and ' +  nums01s[c])
                alert('test2')
                document.getElementById('answer').innerHTML = nums01s[a] + ' hundred and ' +  nums01s[c]
            }
            if (b < 2  && b != 0) {
                alert(nums01s[a] + ' hundred ' +  teens[teen_num])
                alert('test3')
                document.getElementById('answer').innerHTML = nums01s[a] + ' hundred ' +  teens[teen_num]
            }
        }
    }
}

convert(x)