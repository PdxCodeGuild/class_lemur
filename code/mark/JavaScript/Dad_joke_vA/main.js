const url = "https://icanhazdadjoke.com"
const xhttp = new XMLHttpRequest()

function getDadJoke(terms){
    let params = `term=${terms}`
    console.log(params)
    xhttp.open("GET", url + "/search?"+params)
    // xhttp.open("GET", url)
    xhttp.setRequestHeader('Accept', 'application/json')
    xhttp.responseType = 'json'
    xhttp.onload = function () {
        console.log("Success", xhttp.response)
        for (let i = 0; i < xhttp.response.results.length; i++){
            alert(xhttp.response.results[i].joke)
        }
    }
    xhttp.onerror = function () {
        console.log("An Error Has Occurred")
    }
    xhttp.send()
}

function getSearchInput(){
    let searchTerm = prompt("Search for a joke category")
    return searchTerm
}

getDadJoke(getSearchInput())