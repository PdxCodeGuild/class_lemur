const App = {
	data() {
		return {
			colors: [
				'red',
				'green',
				'blue'
			],
			newColor: ''
		}
	},
	methods: {
		submitForm(event) {
			// event.preventDefault()
			console.log('hey')
			console.log(this.newColor)
			this.colors.push(this.newColor)
		},
		clickH1() {
			alert('hey')
		},
		alertColor(event, message) {
			alert(message)
			alert('work?')
		}
	}
}

Vue.createApp(App).mount('#app')