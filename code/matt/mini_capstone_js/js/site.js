const urlSearch = "https://www.dnd5eapi.co"
const url = "https://www.dnd5eapi.co/api/"

const App = {
    data() {
        return {
            spell: null,
            spellInfo: null,
            spellUrl: null,
            spellDesc: null,
            classes: [],
            races: [],
            subRaces: null,
            subClasses: [],
            raceSelection: null,
            classSelection: null,
            subraceSelection: '',
            dragonAncestory: null,
            subclassSelection: '',
            stats: null,
            charStats: {
                cha: 0,
                con: 0,
                dex: 0,
                int: 0,
                str: 0,
                wis: 0,
            },
            stated: 0


        }
    },
    methods: {
        findSpell() {
            axios({
                method: 'get',
                url: url + 'spells',
                params: {
                    name: this.spell
                }
            }).then((response) => {
                this.spellInfo = response.data.results
                this.spellUrl = this.spellInfo[0].url
                axios({
                    method: 'get',
                    url: urlSearch + this.spellUrl
                }).then((response) => {
                    this.spellDesc = response.data.desc[0]
                })
            })
        },
        getSubClass() {
            console.log(this.classSelection)
            console.log(this.raceSelection)
            axios({
                method: 'get',
                url: url + 'classes/' + this.classSelection.toLowerCase()
            }).then((response) => {
                this.subClasses = response.data.subclasses
            })
        },
        getSubRace() {
            this.subRaces = null
            if (this.raceSelection === 'Dragonborn') {
                axios({
                    method: 'get',
                    url: url + 'traits/draconic-ancestry'
                }).then((response) => {
                    this.dragonAncestory = response.data.trait_specific.subtrait_options.from
                    console.log(this.dragonAncestory)
                    if (this.dragonAncestory.length < 1) {
                        this.dragonAncestory = null
                    }
                })
            } else {
                this.dragonAncestory = null
                axios({
                    method: 'get',
                    url: url + 'races/' + this.raceSelection.toLowerCase() + '/subraces'
                }).then((response) => {
                    this.subRaces = response.data.results
                    if (this.subRaces.length < 1) {
                        this.subRaces = null
                    }
                })
            }
        },
        setStats(stat) {
            if (stat.name.toLowerCase() === 'cha') {
                this.charStats.cha = stat.value
                console.log(this.charStats.cha)
            }
            if (stat.name.toLowerCase() === 'con') {
                this.charStats.con = stat.value
                console.log(this.charStats.con)
            }
            if (stat.name.toLowerCase() === 'dex') {
                this.charStats.dex = stat.value
                console.log(this.charStats.dex)
            }
            if (stat.name.toLowerCase() === 'int') {
                this.charStats.int = stat.value
                console.log(this.charStats.int)
            }
            if (stat.name.toLowerCase() === 'str') {
                this.charStats.str = stat.value
                console.log(this.charStats.str)
            }
            if (stat.name.toLowerCase() === 'wis') {
                this.charStats.wis = stat.value
                console.log(this.charStats.wis)
            }

        },
        createCharacter() {


        }
    },
    created() {
        axios({
            method: 'get',
            url: url + 'classes'
        }).then((response) => {
            this.classes = response.data.results
        })
        axios({
            method: 'get',
            url: url + 'races'
        }).then((response) => {
            this.races = response.data.results
        })
        axios({
            method: 'get',
            url: url + 'ability-scores'
        }).then((response) => {
            this.stats = response.data.results
        })
    }
}

Vue.createApp(App).mount('#app')