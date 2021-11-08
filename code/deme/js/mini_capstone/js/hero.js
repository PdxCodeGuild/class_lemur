let info = document.getElementsByClassName("info")
let photo = document.getElementsByClassName("photo")
const app = Vue.createApp({
    data() {
        return {
                selectedCharacter: null,
                keyword: '',
                searchResults: []
                }
            },

                methods: {
                    searchCharacter() {
                        console.log(this.keyword)
                        axios({
                            method: 'get',
                            url: `https://superheroapi.com/api/5012545612091958/search/${this.keyword}`,
                          
                        }).then(response => {
                            this.selectedCharacter = null
                            this.searchResults = response.data.results
                            console.log(response)

                        })
                    },
                    selectCharacter(character){
                        console.log(character)
                        this.selectedCharacter = character
                        // photo.replace(info)

                    }
                },

    created() {
        this.searchCharacter()
    }
    
})

app.mount('#app')