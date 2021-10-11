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
            halfelfAbilities: [],
            proficiencyChoices: null,
            amountOfProficiencies: [],
            numberOfProficiencies: 1,
            chosenProficiencies: [],
            proficiencies: {
                cha: [
                    { 'Deception': 0 },
                    { 'Intimidation': 0 },
                    { 'Performance': 0 },
                    { 'Persuasion': 0 }
                ],
                con: [],
                dex: [
                    { 'Acrobatics': 0 },
                    { 'Sleight of Hand': 0 },
                    { 'Stealth': 0 }
                ],
                int: [
                    { 'Arcana': 0 },
                    { 'History': 0 },
                    { 'Investigation': 0 },
                    { 'Nature': 0 },
                    { 'Religion': 0 }
                ],
                str: [
                    { 'Athletics': 0 }
                ],
                wis: [
                    { 'Animal Handling': 0 },
                    { 'Insight': 0 },
                    { 'Medicine': 0 },
                    { 'Perception': 0 },
                    { 'Survival': 0 }
                ],
            },
            charStats: {
                cha: 0,
                con: 0,
                dex: 0,
                int: 0,
                str: 0,
                wis: 0,
            },
            spellsKnown: [],
            spellsKnownAtlvl: [],
            spellsAtCharLvl: null,
            spellLevel: 1,
            character: null
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
                    this.spellDesc = response.data
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
            let classesCallRan = false
            let spellsCallRan = false
            console.log(this.classSelection, 'get spells known started')
            axios({
                method: 'get',
                url: url + 'classes/' + this.classSelection.toLowerCase() + '/spells'
            }).then((response) => {
                this.spellsKnown = response.data.results
                classesCallRan = true
                if (classesCallRan && spellsCallRan) this.compareSpells()
            })
            console.log(this.spellsKnown, 'axios ran classes url')

            let level = this.charLvl
            axios({
                method: 'get',
                url: url + 'spells',
                params: {
                    level: this.spellLevel
                }
            }).then((response) => {
                this.spellsKnownAtlvl = response.data.results,
                    console.log('axios just ran get spells')
                spellsCallRan = true
                if (classesCallRan && spellsCallRan) this.compareSpells()
            })
            this.spellsAtCharLvl = []
            console.log('before compare')
            // this.compareSpells()
            console.log('after compare')
            console.log(this.spellsKnownAtlvl)
        },

        compareSpells() {
            for (let i = 0; i < this.spellsKnown.length; i++) {
                for (let j = 0; j < this.spellsKnownAtlvl.length; j++) {
                    if (this.spellsKnown[i].name === this.spellsKnownAtlvl[j].name) {
                        console.log(this.spellsKnown[i])
                        this.spellsAtCharLvl.push(this.spellsKnown[i])
                    }
                }
            }
        },

        savingThrows(stat) {
            let save = 0
            switch (stat) {
                case 1:
                    save = -5
                    break
                case 2:
                case 3:
                    save = -4
                    break
                case 4:
                case 5:
                    save = -3
                    break
                case 6:
                case 7:
                    save = -2
                    break
                case 8:
                case 9:
                    save = -1
                    break
                case 10:
                case 11:
                    save = 0
                    break
                case 12:
                case 13:
                    save = 1
                    break
                case 14:
                case 15:
                    save = 2
                    break
                case 16:
                case 17:
                    save = 3
                    break
                case 18:
                case 19:
                    save = 4
                    break
                case 20:
                case 21:
                    save = 5
                    break
                case 22:
                case 23:
                    save = 6
                    break
                case 24:
                case 25:
                    save = 7
                    break
                case 26:
                case 27:
                    save = 8
                    break
                case 28:
                case 29:
                    save = 9
                    break
                case 30:
                    save = 10
            }
            return save
        },

        raceBonus() {
            let first = this.halfelfAbilities[0]
            let second = this.halfelfAbilities[1]
            switch (this.raceSelection) {
                case this.races[0].name:

                    //dragonborn
                    this.charStats.str += 2
                    this.charStats.cha += 1
                    break
                case this.races[1].name:
                    //dwarf

                    this.charStats.con += 2
                    break
                case this.races[2].name:
                    //elf

                    this.charStats.dex += 2
                    break
                case this.races[3].name:
                    //gnome

                    this.charStats.int += 2
                    break
                case this.races[4].name:
                    //half-elf

                    this.charStats.cha += 2
                    if (first === 'con' || second === 'con') {
                        this.charStats.con += 1
                    }
                    if (first === 'dex' || second === 'dex') {
                        this.charStats.dex += 1
                    }
                    break
                case this.races[5].name:
                    //halfling

                    this.charStats.dex += 2
                    break
                case this.races[6].name:
                    //half-orc

                    this.charStats.str += 2
                    this.charStats.con += 1
                    break
                case this.races[7].name:
                    //human

                    this.charStats.cha += 1
                    this.charStats.con += 1
                    this.charStats.dex += 1
                    this.charStats.int += 1
                    this.charStats.str += 1
                    this.charStats.wis += 1
                    break
                case this.races[8].name:
                    //tiefling

                    this.charStats.cha += 2
                    this.charStats.int += 2
            }
        },

        proficiencyBonus() {
            for (let i = 0; i < this.chosenProficiencies.length; i++) {
                switch (this.chosenProficiencies[i]) {
                    case Object.keys(this.proficiencies.cha[0])[0]:
                        this.proficiencies.cha[0].Deception += 3
                        break
                    case Object.keys(this.proficiencies.cha[1])[0]:
                        this.proficiencies.cha[1].Intimidation += 3
                        break
                    case Object.keys(this.proficiencies.cha[2])[0]:
                        this.proficiencies.cha[2].Performance += 3
                        break
                    case Object.keys(this.proficiencies.cha[3])[0]:
                        this.proficiencies.cha[3].Persuasion += 3
                        break
                    // End of cha
                    case Object.keys(this.proficiencies.dex[0])[0]:
                        this.proficiencies.dex[0].Acrobatics += 3
                        break
                    case Object.keys(this.proficiencies.dex[1])[0]:
                        this.proficiencies.dex[1]["Sleight of Hand"] += 3
                        break
                    case Object.keys(this.proficiencies.dex[2])[0]:
                        this.proficiencies.dex[2].Stealth += 3
                        break
                    // End of dex
                    case Object.keys(this.proficiencies.int[0])[0]:
                        this.proficiencies.int[0].Arcana += 3
                        break
                    case Object.keys(this.proficiencies.int[1])[0]:
                        this.proficiencies.int[1].History += 3
                        break
                    case Object.keys(this.proficiencies.int[2])[0]:
                        this.proficiencies.int[2].Investigation += 3
                        break
                    case Object.keys(this.proficiencies.int[3])[0]:
                        this.proficiencies.int[3].Nature += 3
                        break
                    case Object.keys(this.proficiencies.int[4])[0]:
                        this.proficiencies.int[4].Religion += 3
                        break
                    //end of int
                    case Object.keys(this.proficiencies.str[0])[0]:
                        this.proficiencies.str[0].Athletics += 3
                        console.log('strength chack')
                        break
                    //end of str
                    case Object.keys(this.proficiencies.wis[0])[0]:
                        this.proficiencies.wis[0]['Animal Handling'] += 3
                        break
                    case Object.keys(this.proficiencies.wis[1])[0]:
                        this.proficiencies.wis[1].Insight += 3
                        break
                    case Object.keys(this.proficiencies.wis[2])[0]:
                        this.proficiencies.wis[2].Medicine += 3
                        break
                    case Object.keys(this.proficiencies.wis[3])[0]:
                        this.proficiencies.wis[3].Perception += 3
                        break
                    case Object.keys(this.proficiencies.wis[4])[0]:
                        this.proficiencies.wis[4].Survival += 3
                        break

                }
            }
        },

        createCharacter() {
            this.character = 'things'
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