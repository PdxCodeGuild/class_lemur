const url = "https://icanhazdadjoke.com"
const xhttp = new XMLHttpRequest()

function getSearchInput(url, terms){
    let params = `term=${terms}`
    return url + "/search?" + params
}

function showDadJoke(dadJokes){
    let jokeContainer = document.querySelector("#dadJoke")
    for (let i = 0; i < dadJokes.results.length; i++){
        let joke = document.createElement("li")
        joke.innerText = dadJokes.results[i].joke
        jokeContainer.appendChild(joke)
    }

}

function http_get (url, success) {
    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState === 4 && this.status === 200) {
            let data = JSON.parse(xhttp.responseText);
            success(data);
        }
    };
    xhttp.open("GET", url);
    xhttp.setRequestHeader('Accept', 'application/json')
    xhttp.send();
    jokeNumber = 0
}

function getDadJoke(){
    http_get(getSearchInput(url, document.getElementById('searchTerm').value) , function(data) {
    console.log(data);
    showDadJoke(data)})
}

getJoke.addEventListener('click', getDadJoke)

