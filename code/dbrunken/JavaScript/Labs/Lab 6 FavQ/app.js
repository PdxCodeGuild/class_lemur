Vue.createApp({
    data() {
        return {
            randomQuotes: [],
            searchTerm: '',
            searchResults: [],
            searchType: 'tag',
            quotes: [],
            pageCounter: 0,
            newHeader: '',
            last_page: false,
            page: 1
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
        randomQuote() {
            console.log(this.randomQuotes)
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes/',
                headers: {
                    Authorization: 'Token token="1adfb1b977107959bcd838bc16f8a6a7"',
                    Accept: 'application/json'
                }
            }).then(response => {
                console.log(response)
                this.randomQuotes = response.data.quotes
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
                    filter: this.searchTerm,
                    type: this.searchType,
                }
            }).then(response => {
                console.log(response.data)
                this.searchResults = response.data.quotes
                this.last_page=response.data.last_page
            })
        },
        nextPage() {
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
                    filter: this.searchTerm,
                    type: this.searchType,
                    page: this.page+1
                }
            }).then(response => {
                console.log(response.data)
                this.searchResults = response.data.quotes
                this.last_page=response.data.last_page
                this.page++
            })
        },
        previousPage() {
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
                    filter: this.searchTerm,
                    type: this.searchType,
                    page: this.page-1
                }
            }).then(response => {
                console.log(response.data)
                this.searchResults = response.data.quotes
                this.last_page=response.data.last_page
                this.page-1
            })
        }
    },
    created() {
        this.randomQuote()
    }
}).mount('#app')