Vue.createApp({
    data() {
        return {
            movie: '',
            movieQuote: [],
            book: '',
            // data that's populated from api calls
            characters: [],
            movies: [],

            searchTerm: '',
            searchResults: [],
            pageCounter: 0,
        }
    },
    methods: {
        lotr() {
            axios({
                method: 'get',
                url: 'https://the-one-api.dev/v2',
                headers: {
                    Accept: 'application/json'
                }
            }).then(response =>{
                console.log(response)
                this.movie = response.data.movie
            })
        },
        searchLotR() {
            console.log(this.searchTerm);
            this.movie= [];
            this.movie.quote= [];
            this.pageCounter=0;
            this.pageCounter++;
            axios({
                method: 'get',
                url: 'https://the-one-api.dev/v2/quote',
                headers: {
                    Authorization: 'Bearer DEpV0vMpfd2SYXHhQ6HF',
                    Accept: 'application/json'
                },
                params: {
                    dialog: '/' + this.searchTerm + '/i',

                }
            }).then(response =>{
                console.log(response)
                this.searchResults = response.data.docs
                
                for (let i=0; i<this.searchResults.length; i++) {
                    console.log(this.searchResults[i].character)
                    // look up the character name in the character array using the id, store the name on the result object?
                }
                console.log(this.searchResults)
            })
        },
        getLotrChar() {
            axios({
                method: 'get',
                url: 'https://the-one-api.dev/v2/character',
                headers: {
                    Accept: 'application/json'
                }
            }).then(response => {
                for (let i=0; i<this.characters.length; i++) {
                    console.log(this.characters[i].character)
                }
                this.character= [{
                    id:'',
                    name: ''
                }]
            })
        },    
        getLotrMovies() {
            axios({
                method: 'get',
                url: 'https://the-one-api.dev/v2/movie',
                headers: {
                    Accept: 'application/json'
                }
            }).then(response => {
                for (let i=0; i<this.movie.length; i++) {
                    console.log(this.movies[i].movie)
                }
                this.movie=[{
                    id: '',
                    movie: ''
                }]
            })
        }
    },
    created: function() {
        // a function that'll be called when the app is created

        // send a request to the lotr api to get all characters
        // assign the results to our app's data

        // send a request to the lotr api to get all movies
        // assign the results to our app's data
        this.getLotrChar()

        this.getLotrMovies()

        // example ===================
        // this.characters = [{
        //     id: '2342j2iu342i3',
        //     name: 'Gimli'
        // },{
        //     id: 'dfowfoij',
        //     name: 'Tom Bombadill'
        // }]

        // this.movies = [{
        //     id: '2342j2iu342i3',
        //     name: 'The Return of the King'
        // },{
        //     id: 'dfowfoij',
        //     name: 'The Fellowship of the Ring'
        // }]


        // this.quotes = [{
        //     id: 'laksdjflaskjdfasf',
        //     text: 'Bilbo is great',
        //     character: 'asadfasfasfdasdf'
        // }]

        // iterate over the list of quotes
        // for each quote, iterate over the list of characters
        // if the character's id matches the quote's character id
        // replace the quote's character id with the character name

        // this.quotes = [{
        //     id: 'laksdjflaskjdfasf',
        //     text: 'Bilbo is great',
        //     character: 'Gimli'
        // }]



    }
}).mount('#app')