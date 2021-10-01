Vue.createApp({
    data() {
        return {
            randomQuote: '',
            searchTerm: '',
            searchResults: [],
            quotes: [],
            pageCounter: 0,
            newHeader: '',
        }
    },
    methods: {
        FavQs() {
            axios({
                method: 'get',
                url: 'https://favqs.com/api/',
                headers: {
                    Accept: 'application/json'
                }
            }).then(response => {
                console.log(response)
                this.favQuote = response.data.quote
            })
        },
        dailyQuote() {
            // let myToken: "1adfb1b977107959bcd838bc16f8a6a7";
            axios({
                method: 'get',
                url: 'https://favqs.com/api/qotd',
                headers: {
                    Authorization: 'Token token="1adfb1b977107959bcd838bc16f8a6a7"',
                    Accept: 'application/json'
                }
            }).then(response => {
                console.log(response)
                this.dailyQuote = response.data.quote
            })
        },
        searchFavQ() {
            console.log(this.searchTerm);
            this.newHeader = "Search Results";
            this.quotes = [];
            this.pageCounter = 0;
            this.pageCounter++;
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes/',
                headers: {
                    Authorization: 'Token token="1adfb1b977107959bcd838bc16f8a6a7"',
                    Accept: 'application/json'
                },
                params: {
                    term: this.searchTerm,
                    type: this.searchType
                }
            }).then(response => {
                this.searchResults = response.data.quote
            })
        }
    }
}).mount('#app')