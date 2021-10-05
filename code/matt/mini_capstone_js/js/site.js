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
            alignments: null,
            alignmentSelection: null,
            stats: null,
            charName: null,
            charLvl: 1,
            proficiencyChoices: null,
            amountOfProficiencies: [],
            numberOfProficiencies: 1,
            chosenProficiencies: [],
            charStats: {
                cha: 0,
                con: 0,
                dex: 0,
                int: 0,
                str: 0,
                wis: 0,
            },
            spellsKnown: [],
            spellsKnownAtlvl: null,
            spellsAtCharLvl: null,
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
        getAlignment() {
            axios({
                method: 'get',
                url: url + 'alignments'
            }).then((response) => {
                this.alignments = response.data.results
            })
        },
        getProficiencyChoices() {
            this.amountOfProficiencies = []
            axios({
                method: 'get',
                url: url + 'classes/' + this.classSelection.toLowerCase()
            }).then((response) => {
                if (this.classSelection === 'Monk') {
                    this.proficiencyChoices = response.data.proficiency_choices[2].from
                    this.amountOfProficiencies = response.data.proficiency_choices[2].choose
                } else {
                    this.proficiencyChoices = response.data.proficiency_choices[0].from
                    this.amountOfProficiencies = response.data.proficiency_choices[0].choose
                }
            })
        },
        setStats(stat) {
            if (stat.name.toLowerCase() === 'cha') {
                this.charStats.cha = stat.value
            }
            if (stat.name.toLowerCase() === 'con') {
                this.charStats.con = stat.value
            }
            if (stat.name.toLowerCase() === 'dex') {
                this.charStats.dex = stat.value
            }
            if (stat.name.toLowerCase() === 'int') {
                this.charStats.int = stat.value
            }
            if (stat.name.toLowerCase() === 'str') {
                this.charStats.str = stat.value
            }
            if (stat.name.toLowerCase() === 'wis') {
                this.charStats.wis = stat.value
            }

        },
        getSpellsKnown() {
            console.log(this.classSelection.toLowerCase())
            axios({
                method: 'get',
                url: url + 'classes/' + this.classSelection.toLowerCase() + '/spells'
            }).then((response) => {
                this.spellsKnown = response.data.results
            })
            console.log(this.spellsKnown)
            axios({
                method: 'get',
                url: url + 'spells',
                params: {
                    level: this.charLvl
                }
            }).then((response) => {
                this.spellsKnownAtlvl = response.data.results
            })
            for (spellK in this.spellsKnown) {
                for (spellA in this.spellsKnownAtlvl) {
                    if (spellA.name === spellK.name) {
                        this.spellsAtCharLvl.push(spellA)
                    }
                }
            }
        },
        createCharacter() {
        },


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
        axios({
            method: 'get',
            url: url + 'alignments'
        }).then((response) => {
            this.alignments = response.data.results
        })
    }
}

Vue.createApp(App).mount('#app')