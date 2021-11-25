const app = Vue.createApp({
    data() {
        return {
                quote: '',
                keyword: '',
                quoteResults: [],
                tag: '',
                author: '',
                pageNum: 1,
                nextPage:'',
                prevPage: '',
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

                    prevPage: function() {

                        this.pageNum -= 1
            
                        if (this.keyword != '') {
                            this.prevPage = 'https://favqs.com/api/quotes/?'
                            this.type = this.keyword
                        } 
                        else if (this.tag != '') {
                            this.prevPage = 'https://favqs.com/api/quotes/?filter=filter&type=tag'
                            this.type = this.tag
                        }
                        else if (this.author != '') {
                            this.prevPage = 'https://favqs.com/api/quotes/?filter=filter&type=author'
                            this.type = this.author
                        }
            
            
            
                        axios({
                            method: 'get',
                            url: this.nextPage,
                            headers: {
                                Accept: 'application/json',
                                Authorization: 'Token token="855df50978dc9afd6bf86579913c9f8b"'
                            },
                            params: {
                                filter: this.type,
                                page: this.pageNum
                            },
                        }).then(response => {
                            console.log(response.data)
                            this.quoteResults = response.data.quotes
                            this.pageNum = response.data.page
            
                        })
            
                    },
                    nextPage: function() {
    
                        this.pageNum += 1
                        if (this.keyword != '') {
                            this.nextPage = 'https://favqs.com/api/quotes/?'
                            this.type = this.keyword
                        } 
                        else if (this.tag != '') {
                            this.nextPage = 'https://favqs.com/api/quotes/?filter=filter&type=tag'
                            this.type = this.tag
                        }
                        else if (this.author != '') {
                            this.nextPage = 'https://favqs.com/api/quotes/?filter=filter&type=author'
                            this.filter = this.author
                        }
            
                        axios({
                            method: 'get',
                            url: this.nextPage,
                            headers: {
                                Accept: 'application/json',
                                Authorization: 'Token token="855df50978dc9afd6bf86579913c9f8b"'
                            },
                            params: {
                                filter: this.type,
                                page: this.pageNum
                            },
                        }).then(response => {
                            console.log(response.data)
                            this.quoteResults = response.data.quotes
                            this.pageNum = response.data.page
            
                        })
                    }
                },

    created() {
        this.getQuote()
    },
    
    
})

app.mount('#app')