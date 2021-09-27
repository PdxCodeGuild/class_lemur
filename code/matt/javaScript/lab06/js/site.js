const url = 'https://favqs.com/api/quotes'
const urlByKeyword = "https://favqs.com/api/quotes/?filter="
token = "855df50978dc9afd6bf86579913c9f8b"

const App = {
    data() {
        return {
            searchTerm: null,
            searchSelection: '',
            info: {},
            infoByKeyword: null,
            infoByAuthor: null,
            infoByTag: null,
        }
    },
    methods: {
        search() {
            if (this.searchSelection == 'keyword') {
                axios
                    .get(`${urlByKeyword}${this.searchTerm}`, {
                        headers: {
                            'Authorization': `Bearer ${token}`
                        }

                    })
                    .then(response => (this.infoByKeyword = response.data.quotes))
            } else if (this.searchSelection == 'author') {
                axios
                    .get(`${urlByKeyword}${this.searchTerm}&type=author`, {
                        headers: {
                            'Authorization': `Bearer ${token}`
                        }

                    })
                    .then(response => (this.infoByKeyword = response.data.quotes))
            } else if (this.searchSelection == 'tag') {
                axios
                    .get(`${urlByKeyword}${this.searchTerm}&type=tag`, {
                        headers: {
                            'Authorization': `Bearer ${token}`
                        }

                    })
                    .then(response => (this.infoByKeyword = response.data.quotes))
            }
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