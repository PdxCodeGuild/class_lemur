const app = Vue.createApp({
    data() {
        return {
                quote: '',
                keyword: '',
                quoteResults: [],
                tag: '',
                author: '',
                pageNum: 1,
                type: ''
                }
            },

                methods: {
                    getQuote() {
                        axios({
                            method: 'get',
                            url: 'https://favqs.com/api/quotes',
                            headers: {
                                Accept: 'application/json',
                                Authorization: 'Token token="855df50978dc9afd6bf86579913c9f8b"',
                            },
                        }).then(response => {
                            this.quote = response.data.quotes    
                        })
                    },

                    searchQuote() {
                        axios({
                            method: 'get',
                            url: 'https://favqs.com/api/quotes',
                            headers: {
                                Accept: 'application/json',
                                Authorization: 'Token token="855df50978dc9afd6bf86579913c9f8b"'
                            },
                            params: {
                                filter: this.keyword,
                                type: 'keyword'
                            }
                        }).then(response => {
                            this.quoteResults = response.data.quotes
                            console.log(response)

                        })
                    },

                    searchTag() {    
                        axios({
                            method: 'get',
                            url: 'https://favqs.com/api/quotes/?filter=filter&type=tag',
                            headers: {
                                Accept: 'application/json',
                                Authorization: 'Token token="855df50978dc9afd6bf86579913c9f8b"'
                            },
                            params: {
                                filter: this.tag,
                                type: 'tag'
                            },
                        }).then(response => {
                            this.quoteResults = response.data.quotes
                            this.pageNum = response.data.page
                        })
                    },

                    searchAuthor() {
                        axios({
                            method: 'get',
                            url: 'https://favqs.com/api/quotes/?filter=filter&type=author',
                            headers: {
                                Accept: 'application/json',
                                Authorization: 'Token token="855df50978dc9afd6bf86579913c9f8b"'
                            },
                            params: {
                                filter: this.author,
                                type: 'author'
                            }
                        }).then(response => {
                            this.quoteResults = response.data.quotes
                            this.pageNum = response.data.page


                        })
                        
                    },
            
                    prevPage() {
                        this.pageNum--
                        this.type = type
                        axios({
                          method: "get",
                          url: "https://favqs.com/api/quotes/",
                          headers: {
                            Accept: 'application/json',
                            Authorization: 'Token token="855df50978dc9afd6bf86579913c9f8b"'
                          },
                          params: {
                            filter: this.keyword,
                            type: this.type,
                            page: this.pageNum,
                          },
                        }).then((response) => {
                          this.quoteResults = response.data.quotes
                        });
                      },
                      nextPage() {
                        this.pageNum++
                        axios({
                          method: "get",
                          url: "https://favqs.com/api/quotes/",
                          headers: {
                            Accept: 'application/json',
                            Authorization: 'Token token="855df50978dc9afd6bf86579913c9f8b"'
                          },
                          params: {
                            filter: this.keyword,
                            type: this.type,
                            page: this.pageNum,
                          },
                        }).then((response) => {
                          this.quoteResults = response.data.quotes
                        });
                      },
                },

    created() {
        this.getQuote()
    },
    
    
})

app.mount('#app')