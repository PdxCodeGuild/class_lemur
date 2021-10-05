const App = {
    data() {
        return {
            favQuote: '',
            userKeyword: '',
            userTag: '',
            userAuthor: '',
            foundQuotes: [],
            pageNumber: '',
            nextPageUrl: '',
            myFilter: ''
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
                // console.log(response.data)
                this.favQuote = response.data.quotes
            })
        },

        findKeyword() {    
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes/?',
                headers: {
                    'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"',
                },
                params: {
                    filter: this.userKeyword,
                },
            }).then(response => {
                console.log(response.data)
                this.foundQuotes = response.data.quotes
                this.pageNumber = response.data.page
                console.log(this.pageNumber)
            })
        },

        findTag() {    
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes/?filter=filter&type=tag',
                headers: {
                    'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"',
                },
                params: {
                    filter: this.userTag,
                },
            }).then(response => {
                console.log(response.data)
                this.foundQuotes = response.data.quotes
                this.pageNumber = response.data.page
            })
        },

        findAuthor() {    
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes/?filter=filter&type=author',
                headers: {
                    'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"',
                },
                params: {
                    filter: this.userAuthor,
                },
            }).then(response => {
                console.log(response.data)
                this.foundQuotes = response.data.quotes
                this.pageNumber = response.data.page

            })
        },

        nextPage: function() {
    
            this.pageNumber += 1
            console.log(this.pageNumber)

            // userKeyword: '',
            // userTag: '',
            // userAuthor: '', 

            if (this.userKeyword != '') {
                // console.log('userKeyword is truthy')
                this.nextPageUrl = 'https://favqs.com/api/quotes/?'
                this.myFilter = this.userKeyword
            } 
            else if (this.userTag != '') {
                this.nextPageUrl = 'https://favqs.com/api/quotes/?filter=filter&type=tag'
                this.myFilter = this.userTag
            }
            else if (this.userAuthor != '') {
                this.nextPageUrl = 'https://favqs.com/api/quotes/?filter=filter&type=author'
                this.myFilter = this.userAuthor
            }



            axios({
                method: 'get',
                url: this.nextPageUrl,
                headers: {
                    'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"',
                },
                params: {
                    filter: this.myFilter,
                    page: this.pageNumber
                },
            }).then(response => {
                console.log(response.data)
                this.foundQuotes = response.data.quotes
                this.pageNumber = response.data.page

            })
        

        },

        previousPage: function() {

            this.pageNumber -= 1
            console.log(this.pageNumber)

            // userKeyword: '',
            // userTag: '',
            // userAuthor: '', 

            if (this.userKeyword != '') {
                // console.log('userKeyword is truthy')
                this.nextPageUrl = 'https://favqs.com/api/quotes/?'
                this.myFilter = this.userKeyword
            } 
            else if (this.userTag != '') {
                this.nextPageUrl = 'https://favqs.com/api/quotes/?filter=filter&type=tag'
                this.myFilter = this.userTag
            }
            else if (this.userAuthor != '') {
                this.nextPageUrl = 'https://favqs.com/api/quotes/?filter=filter&type=author'
                this.myFilter = this.userAuthor
            }



            axios({
                method: 'get',
                url: this.nextPageUrl,
                headers: {
                    'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"',
                },
                params: {
                    filter: this.myFilter,
                    page: this.pageNumber
                },
            }).then(response => {
                console.log(response.data)
                this.foundQuotes = response.data.quotes
                this.pageNumber = response.data.page

            })

        }

    },
    
    created() {
        this.randomQuote()
    }
}

Vue.createApp(App).mount('#app')