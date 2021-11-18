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
            this.todo({newItem: this.addNewItem})
            this.completed({newItem: this.addNewItem})

          },
        Complete () {
            this.completed.push({newItem: this.addNewItem })
            this.todo.splice({newItem: this.addNewItem })
        },
    }
 //index for splice
})