const App = {
    data() {
        return {
            message: 'To do List',
            list: [],
            inputText: '',
            checkedNames:[],
        }
    },
    methods: {
        submitForm() {
            this.list.push(this.inputText)
            this.inputText=""
            console.log(this.list)
        },
        deleteItem(item){
            i=0
            j=0
            if (this.list.indexOf(item)>=0){
                i=this.list.indexOf(item)
                this.list.splice(i,1)
            }
            if (this.checkedNames.indexOf(item)>=0){
                j=this.checkedNames.indexOf(item)
                this.checkedNames.splice(j,1)
            }

            console.log(this.checkedNames, this.list)
        },
        complete(item){
            i=0
            i=this.list.indexOf(item)
            this.list.splice(i,1)
        },
        incomplete(item){
            i=0
            i=this.checkedNames.indexOf(item)
            this.checkedNames.splice(i,1)
            this.list.push(item)
        }
    },
    
    // created() {
    //     alert('the vue app has been created')
    // }
}
Vue.createApp(App).mount('#app')