Vue.createApp({
	data() {
		return {
			selectedPost: null,
			posts: [
				{
					title: '10 Tips For Writing ClickBait Headlines (Number 7 Will Shock You)',
					author: 'Ikea Perrier',
					body: 'Scrum project paradigm shift series A financing strategy partnership hypotheses gen-z business plan learning curve mass market creative monetization. Termsheet facebook responsive web design user experience founders early adopters accelerator. Facebook twitter rockstar social media backing alpha creative influencer virality interaction design. Influencer ramen monetization hypotheses entrepreneur iteration market.',
					date: 'Aug. 24, 2021',
					image: 'https://www.tckpublishing.com/wp-content/uploads/2014/02/Writing-Tips.jpg',
					authorImage: 'ikea-perrier.jpeg'
				},
				{
					title: 'Lessons From My Year As A Sandwich Tester',
					author: 'Dr. Reason Machete',
					body: 'Cheeseburger rubber cheese mozzarella. Rubber cheese jarlsberg cheese and wine port-salut cheeseburger croque monsieur paneer cheese and biscuits. Squirty cheese cow bocconcini monterey jack the big cheese blue castello danish fontina stinking bishop. Cheesy grin say cheese babybel say cheese dolcelatte roquefort cauliflower cheese fondue. Fromage frais mozzarella.',
					date: 'Aug. 21, 2021',
					image: 'https://static.toiimg.com/thumb/54714340.cms?width=1200&height=900',
					authorImage: 'dr-reason-machete.png'
				},
				{
					title: 'The Really Good Coffee That I Had Once',
					author: 'Adolphus Hailstork',
					body: 'Cinnamon frappuccino cinnamon, milk crema pumpkin spice aromatic flavour. Caffeine kopi-luwak, as grinder fair trade that french press. Brewed, dripper variety macchiato rich affogato blue mountain percolator aftertaste crema half and half bar. Rich, ristretto decaffeinated at siphon wings robust. Crema organic a at viennese mug foam decaffeinated breve arabica. Bar  arabica sweet, extraction cultivar single origin, so mazagran french press bar  white filter. Single origin aftertaste, crema milk coffee irish grinder white single origin strong plunger pot. Et, coffee percolator crema at as aged white chicory. Macchiato crema aroma sugar cup black aged that.',
					date: 'Aug. 19, 2021',
					image: 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/A_small_cup_of_coffee.JPG/1200px-A_small_cup_of_coffee.JPG',
					authorImage: 'adolphus-hailstork.png'
				}
			]
		}
	},
	methods: {
		selectPost(post) {
			this.selectedPost = post
		},
		clearSelectedPost() {
			console.log('test')
			this.selectedPost = null
		}
	}
}).mount('#app')