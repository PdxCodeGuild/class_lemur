const App = {
    data() {
        return {
            items: ''
        }
    },
    methods: {
        submitForm(event) {
            console.log(this.items)
            this.items.push(this.items)
        }
    }
}

Vue.createApp(App).mount('#app')