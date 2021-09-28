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
const token='6ac53ed6f4ae6184e6b11a7c9998a5b9'
const App = {
    data() {
        return {
            message: "It is known:",
            jotdQuote: '',
            jotdAuthor:'',
            inputText: '',
            results: [],
        }        
    },
    methods: {
        jotd(){
            axios({
                method:'get',
                url: 'https://favqs.com/api/qotd',
                headers:{
                    'Content-Type': 'application/json',
                    // Authorization: 'Token token'=data.token
                },
            }).then(response => {
                console.log(response)
                this.jotdQuote= response.data.quote.body
                this.jotdAuthor= response.data.quote.author
                console.log(this.jotdQuote, this.jotdAuthor)
            })
        }

    },
    created() {
        this.jotd()
    }
        
}
Vue.createApp(App).mount('#app')