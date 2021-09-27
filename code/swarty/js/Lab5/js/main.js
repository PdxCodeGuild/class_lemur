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
            count=length(list) 
        },
        
    },
    
    // created() {
    //     alert('the vue app has been created')
    // }
}
Vue.createApp(App).mount('#app')