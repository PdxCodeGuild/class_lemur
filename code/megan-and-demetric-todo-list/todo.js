let todo = document.getElementById('todo1')
let completed = document.getElementById('completed')
let addTodo = document.getElementById('addTodo')
let addComplete = document.getElementById('addComplete')
const form = document.getElementById("form")
const form1 = document.getElementById("form1")

//lists
let todoList = document.getElementById('todoList')
let completedList = document.getElementById('completedList')

form.addEventListener('submit', function(event) {
    event.preventDefault()
    let item = addTodo.value
    let itemLi = document.createElement('li')
    console.log(itemLi)
    itemLi.innerHTML=item
    todoList.appendChild(itemLi)
    let deleteButton = document.createElement('button')
    deleteButton.innerText = "Remove"
    itemLi.appendChild(deleteButton)
    let completeButton = document.createElement("button")
    completeButton.innerText = "Complete"
    itemLi.appendChild(completeButton)
    // itemLi.addEventListener('click', function() {
		// alert(item)
	// })
 
    completeButton.addEventListener('click', function(){
        completedList.appendChild(itemLi)
        itemLi.removeChild(completeButton)
    })
    deleteButton.addEventListener('click', function() {
        todoList.removeChild(itemLi)
    }) 
    deleteButton.addEventListener('click', function() {
        completedList.removeChild(itemLi)
    })
})

