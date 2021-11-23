Vue.createApp({
    data() {
        return {
            message: 'Got things to do? Add em to the list: ',
            todos: [],
            doneDo: [],
            inputText: ''
        }
    },
    methods: {
        clickEvent() {
            console.log('item added')
        },
        submitForm() {
            // console.log(this.item)
            this.todos.push({
                item: this.inputText,
                isComplete: false
            })
        },
        incompleteItem (todo) {
            this.todos.push(todo)
            todo.isComplete = false
            let index = this.doneDo.indexOf(todo)
            console.log(index)
            this.doneDo.splice(index, 1)
        },
        doneItem (todo) {
            this.doneDo.push(todo)
            todo.isComplete = true
            let index = this.todos.indexOf(todo)
            console.log(index)
            this.todos.splice(index, 1)
        },
        deleteItem (done) {
            let item = this.doneDo.indexOf(done)
            console.log(item)
            this.doneDo.splice(item, 1)
        }
    }
}).mount('#app')