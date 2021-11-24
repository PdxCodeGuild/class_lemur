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
            this.todo.splice({newItem: this.addNewItem}, 1)
            this.completed.splice({newItem: this.addNewItem}, 1)

          },
        Complete () {
            this.completed.push({newItem: this.addNewItem })
            this.todo.splice({newItem: this.addNewItem }, 1)
        },
    }
 //index for splice
})