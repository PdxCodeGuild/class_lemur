const todos = {
  data() {
    return {
      todos: [
        {
          title: 'eat', 
          isCompleted: false,
        },
        {
          title: 'sleep', 
          isCompleted: false,
        },
        {
          title: 'code', 
          isCompleted: false,
        },
        {
          title: 'repeat', 
          isCompleted: false,
        }
      ],
      toDones: [],
      newTodo: {
        title: '', 
        isCompleted: false,
      }
    }
  },
  methods: {
    deleteItem (lineItem) {
      this.todos.splice(lineItem, 1)
    },
    deleteComplete (lineItem) {
      this.toDones.splice(lineItem, 1)
    },
    completeItem (todo, index) {
      this.toDones.push(todo)
      todo.isCompleted= true
      this.todos.splice(index, 1)
    },
    uncompleteItem (todone, index) {
      this.todos.push(todone)
      todone.isCompleted= false
      this.toDones.splice(index, 1)
    },
    addTodo (event) {
      this.todos.push(
        this.newTodo
      )
    }
  }
}

Vue.createApp(todos).mount('#todos')
