const TodoItem = {
	props: ['todo'], // the todo object from the v-for loop is the property
	template: `<li>{{ todo.text }}</li>`
}