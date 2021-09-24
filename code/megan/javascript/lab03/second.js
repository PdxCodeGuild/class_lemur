const button = document.querySelector('#button')

let input1 = document.querySelector('#input')

const solution = document.querySelector('#solution')


button.addEventListener('click', function () {
    
    translation = {
        a : 'n',
        b : 'o',
        c : 'p',
        d : 'q',
        e : 'r',
        f : 's',
        g : 't',
        h : 'u',
        i : 'v',
        j : 'w',
        k : 'x',
        l : 'y',
        m : 'z',
        n : 'a',
        o : 'b',
        p : 'c',
        q : 'd',
        r : 'e',
        s : 'f',
        t : 'g',
        u : 'h',
        v : 'i',
        w : 'j',
        x : 'k',
        y : 'l',
        z : 'm'
    }

    let input = input1.value

    let final = []
    
    for (let i = 0; i < input.length; i++) {
        let char = input[i]
        final.push(translation[char])
        solution.innerText = final.join('')
    }
    
})


