const App = {
    data() {
        return {
            message: 'To do List',
            list: [
            ],
            inputText: '',
        }
    },
    methods: {
        submitForm() {
            this.list.push(this.inputText)
            this.inputText=""
        },
        deleteItem(item){
            console.log(item, "item")
            // let index=this.list.index(item)
            // console.log(index, "index")
            this.list.splice(function(value){
                return value != item
            },1)
        }
    },
    
    // created() {
    //     alert('the vue app has been created')
    // }
}
Vue.createApp(App).mount('#app')