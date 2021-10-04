new Vue({
    el: '#app',
    data: {
        message: 'Todo List',
        todo: [],
        completed: [],
        addNewItem: ''
    },
    methods: {

        addToListForm() {
            this.todo.push({newItem: this.addNewItem })
        },
        Remove () {
            this.todo.pop({newItem: this.addNewItem })
            this.completed.pop({newItem: this.addNewItem })

          },
        Complete () {
            this.completed.push({newItem: this.addNewItem })
            this.todo.pop({newItem: this.addNewItem })
        },
    }
 
})