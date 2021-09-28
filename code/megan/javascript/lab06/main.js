const App = {
    data() {
        return {
            favQuote: '',
            userInput: '',
            search: []
        }
    },

    methods: {

        randomQuote() {     
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes',
                headers: {
                    'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"',
                }
            }).then(response => {
                console.log(response.data)
                this.favQuote = response.data.quotes
            })
        },

        findQuote() {   
            console.log(this.userInput)  
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes/search',
                headers: {
                    'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"',
                },
                params: {
                    term: this.userInput
                },
            }).then(response => {
                console.log(response)
                this.search = response.data.results
            })
        }
    }, // closes methods 

    created() {
        this.randomQuote()
    }
}

Vue.createApp(App).mount('#app')