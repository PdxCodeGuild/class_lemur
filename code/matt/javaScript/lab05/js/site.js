let app = new Vue({
    el: '#app',
    data: {
        message: 'finally!!!!!!',
        items: [],
        newItem: ''
    },
    methods: {
        addItem: function () {
            this.items.push({
                itemName: this.newItem,
                complete: false
            })
            this.newItem = ''
        },
        complete: function (item) {
            let index = this.items.indexOf(item)

            if (this.items[index].complete === false) {
                this.items[index].complete = true
            } else if (this.items[index].complete === true) {
                this.items[index].complete = false
            }
        },
        deleteItem: function (item) {
            let index = this.items.indexOf(item)
            this.items.splice(index, 1)
            // delete this.items[index]
        }
    }
})
