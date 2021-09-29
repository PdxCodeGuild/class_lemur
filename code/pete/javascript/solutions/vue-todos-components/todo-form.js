const TodoForm = {
	template: `
	<form @submit.prevent="submitAddTodo">
		<input type="text" v-model="newTodo">
		<button type="submit">add todo</button>
	</form>`,

	data() {
		return {
			newTodo: ''
		}
	},

	methods: {
		submitAddTodo() {
			console.log('this much worked')
			this.$emit('handleAddTodo', this.newTodo)
			this.newTodo = ''
		}
	}
}