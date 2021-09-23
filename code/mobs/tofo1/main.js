const submitBtn = document.querySelector("#submit")
const item = document.querySelector("#item")
const listContainer = document.querySelector("#list-container")

let createItem = function () {
    let listItem = document.createElement("li")
    let listCompleted = document.createElement("button")
    let listDelete = document.createElement("button")
    let listGroup = document.createElement("span")

    listGroup.innerText = item.value
    listCompleted.innerText = "Complete"
    listDelete.innerText = "Delete"
    listItem.className = "ms-3 ps-1 list-group-item border-0"
    listCompleted.className = "completed mx-1 btn-primary"
    listDelete.className = "delete btn-primary"

    listCompleted.onclick = function () {
        let list = this.parentNode
        list.style.textDecoration = "line-through"
    }

    listDelete.onclick = function () {
        let list = this.parentNode
        listContainer.removeChild(list)
    }

    listItem.appendChild(listGroup)
    listItem.appendChild(listCompleted)
    listItem.appendChild(listDelete)

    return (listItem)
}

let addItem = function () {
    let list = createItem(item.value)
    listContainer.appendChild(list)
}

submitBtn.addEventListener('click', addItem)

