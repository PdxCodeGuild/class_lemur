const app = Vue.createApp({
    data() {
        return {
                character: '',
                keyword: '',
                searchResults: []
                }
            },

                methods: {
                    searchCharacter() {
                        console.log(this.keyword)
                        axios({
                            method: 'get',
                            url: 'https://superheroapi.com/api/5012545612091958/search/name',
                            // headers: {
                            //     'Authorization' : Bearer {{ 5012545612091958 }}
                            // },
                            // params: {
                            //     filter: this.keyword,
                            //     type: 'name'
                            // }
                        }).then(response => {
                            this.searchResults = response.data.results
                            console.log(response)

                        })
                    },
                },

    created() {
        this.searchCharacter()
    }
    
})

app.mount('#app')