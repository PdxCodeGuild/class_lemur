
const App = {
    
    data() {
        return {
            userSearch: '',
            showId: '',
            userPerson: '',
            crewId: '',
            episodeId: '',
            // actorCast: '',
            // actorCrew: '',
            tvShow: null, 
            castMembers: [],
            crewMembers: [],
            episodeList: [],
            famousPerson: [],
            // allCast: [],
            // allCrew: [],
        }
    },

    methods: {

        findShow() {    
            axios({
                method: 'get',
                url: 'https://api.tvmaze.com/singlesearch/shows?',
                params: {
                    q: this.userSearch,
                },
            }).then(response => {
                console.log(response.data, 'findShow response object')
                this.tvShow = response.data
            })
        },

        findPerson() {
            axios({
                method: 'get',
                url: 'https://api.tvmaze.com/search/people?',
                params: {
                    q: this.userPerson
                }
            }).then(response => {
                console.log(response.data[0].person)
                this.famousPerson = response.data
            })
        },
        
        showCast() {  
            axios({
                method: 'get',
                url: `https://api.tvmaze.com/shows/${this.showId}/cast`,
            }).then(response => {
                console.log(response)
                this.castMembers = response.data
            })
        },
      

        showCrew() {    
            axios({
                method: 'get',
                url: `https://api.tvmaze.com/shows/${this.crewId}/crew`,
            }).then(response => {
                console.log(response)
                this.crewMembers = response.data
            })
        },

        showEpisodes() {    
            axios({
                method: 'get',
                url: `https://api.tvmaze.com/shows/${this.episodeId}/episodes`,
            }).then(response => {
                console.log(response)
                this.episodeList = response.data
            })
        },
    

        }
    }

Vue.createApp(App).mount('#app')
