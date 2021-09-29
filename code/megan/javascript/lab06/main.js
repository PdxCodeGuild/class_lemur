const App = {
    data() {
        return {
            favQuote: '',
            userInput: '',
            foundQuotes: []
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
                url: 'https://favqs.com/api/search/',
                headers: {
                    'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"',
                },
                params: {
                    filter: this.userInput
                },
            }).then(response => {
                console.log(response)
                this.foundQuotes = response.data.quotes
            })
        }
    }, // closes methods 

    created() {
        this.randomQuote()
    }
}

Vue.createApp(App).mount('#app')