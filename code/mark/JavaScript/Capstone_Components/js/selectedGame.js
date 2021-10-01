const SelectedGame = {
    props: ['promo'],
    template: `<img :src="promo.image" alt="..." class="img-fluid w-100">
    <div class="row my-3">
        <h1 class="col bold">{{promo.title}}</h1>
            <h2 class="fw-bold text-success col border text-center bg-light">{{promo.status}}</h2>

    </div>
    <div class="row fs-2 border-primary border-top border-bottom border-4 text-center">
        <p class="col">Value: {{promo.worth}}</p>
        <p class="col">Deal Activated <b>{{promo.users}}</b> times!</p>
    </div>
    <div class="row fs-2">
        <label for="description" class="fw-bold my-2">Description:</label>
        <p id='description' class="border p-3">{{promo.description}}</p>
        <label for='instructions' class="fw-bold my-2">Instructions</label>
        <p id='instructions' class="border p-3">{{promo.instructions}}</p>
        <div class="row my-4 border-warning border-top border-bottom border-4 text-center">
            <p class="col"><b>Start Date:</b> {{promo.published_date}}</p>
            <p class="col"><b>End Date:</b> {{promo.end_date}}</p>
        </div>
        <div class="row">
            <p class="col text-center"><b>Type:</b> {{promo.type}}</p>
            <p class="col text-center"><b>Platform(s):</b> {{promo.platforms}}</p>
        </div>
    </div>
    <div class="row justify-content-center my-5">
        <a :href="promo.open_giveaway_url" class="btn btn-primary btn-lg col-6">Get this Deal</a>
    </div>`,
}