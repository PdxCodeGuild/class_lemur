const url = 'https://favqs.com/api/quotes/'
token = "855df50978dc9afd6bf86579913c9f8b"

const App = {
    data() {
        return {
            searchTerm: null,
            searchSelection: '',
            info: {},
            infoByKeyword: null,
            page: 1,
            lastPage: false
        }
    },
    methods: {
        search() {
            if (this.searchSelection == 'keyword') {
                if (this.searchTerm != this.searchTerm) {
                    console.log(searchTerm)
                    console.log(this.searchTerm)
                    this.page = 1
                }
                axios({
                    method: 'get',
                    url: url,
                    headers: {
                        'Authorization': `Bearer ${token}`
                    },
                    params: {
                        filter: this.searchTerm,
                        page: this.page
                    }
                }).then((response) => {
                    this.infoByKeyword = response.data.quotes
                    this.lastPage = response.data.last_page
                })
            } else if (this.searchSelection == 'author') {
                // title(this.searchTerm)
                axios({
                    method: 'get',
                    url: url,
                    headers: {
                        'Authorization': `Bearer ${token}`
                    },
                    params: {
                        filter: this.searchTerm,
                        type: 'author',
                        page: this.page
                    }
                }).then((response) => {
                    this.infoByKeyword = response.data.quotes
                    this.lastPage = response.data.last_page
                })
            } else if (this.searchSelection == 'tag') {
                axios({
                    method: 'get',
                    url: url,
                    headers: {
                        'Authorization': `Bearer ${token}`
                    },
                    params: {
                        filter: this.searchTerm,
                        type: 'tag',
                        page: this.page
                    }
                }).then((response) => {
                    this.infoByKeyword = response.data.quotes
                    this.lastPage = response.data.last_page
                })
            }
        },
        nextPage() {
            this.page++
            this.search()
        },
        previousPage() {
            this.page--
            this.search()
        },
        resetPage() {
            this.page = 1
        }
    },
    created() {
        axios
            .get(url, {
                headers: {
                    'Authorization': `Bearer ${token}`
                }
            })
            .then(response => (this.info = response.data.quotes))
    }
}
Vue.createApp(App).mount('#app')