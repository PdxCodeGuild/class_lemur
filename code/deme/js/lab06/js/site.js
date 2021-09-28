const app = Vue.createApp({
    data() {
        return {
                quote: '',
                keyword: '',
                quoteResults: []
                }
            },

                methods: {
                    getQuote() {
                        axios({
                            method: 'get',
                            url: 'https://favqs.com/api/qotd',
                            headers: {
                                Accept: 'application/json'
                            }
                        }).then(response => {
                            this.quote = response.data.quote    
                        })
                    },

                    searchQuote() {
                        console.log(this.keyword)
                        axios({
                            method: 'get',
                            url: 'https://favqs.com/api/quotes',
                            headers: {
                                Accept: 'application/json',
                                Authorization: 'Token token="855df50978dc9afd6bf86579913c9f8b"'
                            },
                            params: {
                                filter: this.keyword,
                                type: 'tag'
                            }
                        }).then(response => {
                            this.quoteResults = response.data.quotes
                            console.log(response)

                        })
                    }
                },

    created() {
        this.getQuote()
    }
})

app.mount('#app')