const form = document.querySelector('form')
const itemInput = document.querySelector('#todo-add')
const itemContainer = document.getElementById('items')
// console.log(form, colorInput, colorContainer)
let i=0
list=[]
form.addEventListener('submit', function (event) {
	event.preventDefault()
    
    list.push(itemInput.value)
    console.log(list)
	// console.log(colorInput.value) // the value of the input element
	const ItemLine = document.createElement('li')
    count=`item${i}`
    ItemLine.setAttribute('id', count)
	// ItemLine.innerText = list[i]
    ItemLine.innerText = itemInput.value
    const delbutton = document.createElement('button')
    ItemLine.appendChild(delbutton)
    delbutton.innerText = 'delete'
    delbutton.addEventListener('click', function (){
        itemContainer.removeChild(ItemLine)
        list.splice(i,1)
    })
    const doneButton = document.createElement('button')
    ItemLine.appendChild(doneButton)
    doneButton.innerText = 'complete'
    doneButton.addEventListener('click', function (){
        // ItemLine.style.setProperty("text-decoration", "line-through")
        ItemLine.style.textDecoration="line-through"
    })
	itemContainer.appendChild(ItemLine)
    itemInput.value=''
    i++
	
})