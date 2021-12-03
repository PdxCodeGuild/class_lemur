new Vue({
    el: '#app',
    data: {
        message: 'Todo List',
        todo: [{
            index: 1,
            name: "",
            isComplete: false,
          }],
        completed: [{
            index: 1,
            name: '',
            isComplete: true,
          }],
        addNewItem: '',
    },
    methods: {

        addToListForm() {
            this.todo.push({name: this.addNewItem, isComplete: false, index: this.todo.length +1 });
            this.addNewItem='';
        },
        Remove: function (item) {
            this.todo = this.todo.filter((comItem) => comItem.name !== item.name)
            this.completed = this.completed.filter((comItem) => comItem.name !== item.name)

          },
        Complete: function (item) {
            item.isComplete = true
            this.completed.push({name: item.name, index: this.length + 1, isComplete: true});
            this.todo = this.todo.filter((comItem) => comItem.name !== item.name)
        },

    }
 
})