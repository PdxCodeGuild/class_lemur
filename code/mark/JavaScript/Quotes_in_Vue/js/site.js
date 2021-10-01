
const App = {
    data() {
        return {
            searchTerm: '',
            searchType: '',
            searchResults: [],
            lastPage: true,
            firstLoad: true,
            qotd: '',
            page: 1
        }
    },
    methods: {
        loadRandom: function () {
            axios({
                method: 'get',
                url: 'https://favqs.com/api/qotd'
            }).then(response => {
                this.qotd = response.data.quote
            })
        },
        searchQuotes() {
            this.page=1 
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes/?',
                headers: {
                    Authorization: 'Token token="855df50978dc9afd6bf86579913c9f8b"'
                },
                params: {
                    type: this.searchType,
                    filter: this.searchTerm,
                    page: this.page
                }
            }).then(response => {
                this.searchResults = response.data.quotes
                this.lastPage = response.data.last_page
                this.firstLoad = false
            })
        },
        nextPage() {
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes/?',
                headers: {
                    Authorization: 'Token token="855df50978dc9afd6bf86579913c9f8b"'
                },
                params: {
                    type: this.searchType,
                    filter: this.searchTerm,
                    page: ++this.page
                }
            }).then(response => {
                this.searchResults = response.data.quotes
            })
        },
        previousPage() {
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes/?',
                headers: {
                    Authorization: 'Token token="855df50978dc9afd6bf86579913c9f8b"'
                },
                params: {
                    type: this.searchType,
                    filter: this.searchTerm,
                    page: --this.page
                }
            }).then(response => {
                this.searchResults = response.data.quotes
            })
        }

    },
    mounted: function () {
        this.loadRandom()
    }
}

Vue.createApp(App).mount("#app")