
const api=gLogin.api_key
console.log(api)




const App = {
    
    data() {
        return {
            ISBN:"", //test ISBN remove later
            inAuthor:"",
            inAll:"",//test search remove later
            inTitle:"",
            subject:"",
            inputText:"",
            searchType:"",
            searchResults:[],
            message:"Ebook search",
            counter:0
        }        
    },
    methods: {
        readbooks(){
            google.books.load();
            function initialize() {
                var viewer = new google.books.DefaultViewer(document.getElementById('viewerCanvas'));
                viewer.load(`ISBN:${this.ISBN}`);
            }
            google.books.setOnLoadCallback(initialize)
        },
        volumes(){         
            axios({
                
                method:'get',
                url: 'https://www.googleapis.com/books/v1/volumes',
                headers: {
                    accept: 'applicatio/json',
                    
                },
                params: {
                    q: this.inputText,
                    projection:'lite',
                    key:gLogin.api_key,
                    startIndex:this.counter                              
                }
            }).then(response => {
            console.log(response)            
            this.searchResults= response.data.items
            if (response.data.last_page) {
                this.pages="End of quotes"
            }
            })
        },
        first() {
            counter=0
            this.volumes()

        },
        next() {
            this.counter+=10
            this.volumes()
        },
        previous() {
            this.counter-=10
            this.volumes()
        }        
    },
    beforeCreated() {
        this.readbooks()
    }        
}
Vue.createApp(App).mount('#app')