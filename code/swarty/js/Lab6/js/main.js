// Build a Vue application that allows a user to search for quotes on FavQs.

// Requirements:

// Your app must use Vue to fetch data and interact with the results.
// Let the user enter a search term and select whether to search by keyword, author, or tag.
// Implement pagination buttons when the search returns more than 25 quotes.
// When the page first loads, show the user a set of completely random quotes.
// You must have at least one Vue component in your app.
// Resources:

// Read the API documentation!
// Remember to use your Vue app data as your single source of truth.
// You'll need to set the Authorization header for the FavQs API to work.
const mytoken='6ac53ed6f4ae6184e6b11a7c9998a5b9'
const App = {
    data() {
        return {
            message: "It is known:",
            qotdQuote: [],
            qotdAuthor:'',
            inputText: '',
            searchType:'',
            searchResults: [],
            pages:"More quotes",
            counter:0,
        }        
    },
    methods: {
        qotd(){
            counter=0    
            axios({
                
                method:'get',
                url: 'https://favqs.com/api/quotes',
                headers: {
                    'Content-Type': 'application/json',
                    Authorization: `Token token=${mytoken}`,
                },
                params: {
                    // filter: this.inputText,
                    // type:this.searchType                    
                }
            }).then(response => {
            console.log(response)            
            this.searchResults= response.data.quotes
            console.log(this.searchResults)
            if (response.data.last_page) {
                this.pages="End of quotes"
            }
            })
        },
        quotes(){      
            counter=0    
            axios({
                
                method:'get',
                url: 'https://favqs.com/api/quotes',
                headers: {
                    'Content-Type': 'application/json',
                    Authorization: `Token token=${mytoken}`,
                },
                params: {
                    filter: this.inputText,
                    type:this.searchType                    
                }
            }).then(response => {
            console.log(response)            
            this.searchResults= response.data.quotes
            console.log(this.searchResults)
            if (response.data.last_page) {
                this.pages="End of quotes"
            }
            }),
            this.counter++
        },
        next() {
            this.counter++
            axios({
                method:'get',
                url: 'https://favqs.com/api/quotes',
                headers: {
                    'Content-Type': 'application/json',
                    Authorization: `Token token=${mytoken}`
                },
                params: {
                    filter: this.inputText,
                    type:this.searchType,
                    page: this.counter
                }
            }).then(response => {
            console.log(response.data)            
            this.searchResults= response.data.quotes
            console.log(this.searchResults)
            if (response.data.last_page) {
                this.pages="End of quotes"
            }
            })
        }
    },
    created() {
        this.qotd()
    }
        
}
Vue.createApp(App).mount('#app')