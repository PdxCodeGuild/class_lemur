
const App = {
    data() {
        return {
            allGames: [],
            hideGamesList: [],
            selectedPromo: null,
            platform: '',
            type: '',
            sortBy: ''
        }
    },
    methods: {
        loadRandom: function () {
            fetch('https://gamerpower.p.rapidapi.com/api/giveaways',
                {
                    method: 'GET',
                    headers: {
                        'x-rapidapi-host': 'gamerpower.p.rapidapi.com',
                        'x-rapidapi-key': '3f1fb12e85msh1264d4f6fb7378cp198ad1jsn76eb42b0580f'
                    },
                    params: { 
                        platform: this.platform, 
                        type: this.type, 
                        'sort-by': this.sortBy }
                }).then(response => response.json())
                .then(response => {
                    this.allGames = response
                }).catch(error => console.log(error.message))
        },
        selectPromo (promo) {
            this.selectedPromo = promo
        },
        clearSelectedPromo () {
            this.selectedPromo = null
        },
        notInterested (game) {
            this.hideGamesList.push(game)
            let index = this.allGames.indexOf(game)
            this.allGames.splice(index, 1)
        }
    },
    mounted: function () {
        this.loadRandom()
    },
    computed: {
        ByPlatform() {
            let sortBy = this.sortBy
            let allGames = this.allGames.filter(game => game.platforms.includes(this.platform))
            allGames = allGames.filter(game => game.type.includes(this.type))
            return allGames.sort(function(a,b){
                if (a[sortBy] < b[sortBy]) {
                    return -1;
                  }
                  if (a[sortBy] > b[sortBy]) {
                    return 1;
                  }
                  return 0;
            })
        },
    }
}

Vue.createApp(App).mount("#app")
