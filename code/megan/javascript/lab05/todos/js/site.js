const App = {
    data() {
        return {
            items: [
                {
                    title: 'Buy milk',
                    isComplete: false
                },
                {
                    title: 'Get gas',
                    isComplete: true
                }
            ],
            newItem: '',
        }
    },
    computed: {
        itemFalse() {
            return this.items.filter(item => item.isComplete === false)
        },
        itemTrue() {
            return this.items.filter(item => item.isComplete === true)
        }
    },
    methods: {

        addItem: function() {

            this.items.push({
                title: this.newItem,
                isComplete: false
            })
            
            this.newItem = ''
        },

        markCompleted: function (item) {

            item.isComplete = true
        },

        removeItem: function (item) {
            
            this.items.splice(this.items.indexOf(item), 1)  
            // ^ removes the last item of the list 

        }

    }
}

Vue.createApp(App).mount('#app')