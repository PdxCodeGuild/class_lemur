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
            let i=0
            console.log(item, "item")
            i=this.list.indexOf(item)
            console.log(i, "index" , this.list)
            this.list.splice(i,1)
            console.log(this.list,"new")
        }
    },
    
    // created() {
    //     alert('the vue app has been created')
    // }
}
Vue.createApp(App).mount('#app')