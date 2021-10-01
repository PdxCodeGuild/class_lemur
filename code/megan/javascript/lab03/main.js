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

let user = prompt("Please enter a string: ").toLowerCase()

let final = []


for (let i = 0; i < user.length; i++) {
    let char = user[i]
    final.push(translation[char])
  }

console.log(final)

