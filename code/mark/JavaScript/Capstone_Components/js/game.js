const GameComponent = {
    props: ['game'],
    template: `
        <div class="card d-flex img-zoom-container" style="width: 18rem;">
            <img :src="game.image" @click="selectPromo(game)" class="card-img-top" alt="...">
            <div class="card-body panel-body text-dark">
                <h5 class="card-title">{{ game.title }}</h5>
                <h6 class="card-subtitle my-1">End Date: {{ game.end_date }}</h6>
                <h6 class="card-subtitle my-1">Value: {{ game.worth }}</h6>
                <h6 class="card-subtitle my-1">Times Deal Activated: {{ game.users }}</h6>
                <p class="card-text ">{{ game.description }}</p>
                <div class="row align-baseline">
                    <a :href="game.open_giveaway_url" class="btn btn-primary col-6">Grab this Deal!</a>
                    <a class="btn btn-danger col-6" @click="notInterested(game)">Not Interested</a>
                </div>
            </div>
        </div>`,
    data(){
        return {
            selectedPromo: '',
            removeGame: ''
        }
    },
    methods: {
        selectPromo(game){
           this.selectedPromo = game
           this.$emit('promo-select', this.selectedPromo)
        },
        notInterested(game){
            this.removeGame = game
            this.$emit('not-interested', this.removeGame)
        }
    }
}