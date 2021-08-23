

# Lab 2: Blog

Let's make the template of a blog with a title, top-nav, side-nav, and multiple posts. Use [flexbox](https://css-tricks.com/snippets/css/a-guide-to-flexbox/) and [semantic elements](https://www.w3schools.com/html/html5_semantic_elements.asp) (header, nav, section, and footer). You can use a [custom font](https://fonts.google.com/), [fancy colors](https://htmlcolorcodes.com/color-names/), and generate fake content using an [Ipsum](https://meettheipsums.com/).

Once you have your template, incorporate it into a flask app.  Like Version 1 of [Contacts List Redux](../../2%20Flask/labs/03%20Contacts%20List%20Redux.md), you will load your blog posts from a json file.  They might look something like this:

```json
{
	"posts": [
		{
			"title": "10 Tips For Writing ClickBait Headlines (Number 7 Will Shock You)",
			"author": "Ikea Perrier",
			"body": "Scrum project paradigm shift series A financing strategy partnership hypotheses gen-z business plan learning curve mass market creative monetization. Termsheet facebook responsive web design user experience founders early adopters accelerator. Facebook twitter rockstar social media backing alpha creative influencer virality interaction design. Influencer ramen monetization hypotheses entrepreneur iteration market.",
			"date": "Aug. 24, 2021",
			"image": "10-tips-for-writing.png",
			"author_image": "ikea-perrier.jpeg"
		},
		{
			"title": "Lessons From My Year As A Sandwich Tester",
			"author": "Dr. Reason Machete",
			"body": "Cheeseburger rubber cheese mozzarella. Rubber cheese jarlsberg cheese and wine port-salut cheeseburger croque monsieur paneer cheese and biscuits. Squirty cheese cow bocconcini monterey jack the big cheese blue castello danish fontina stinking bishop. Cheesy grin say cheese babybel say cheese dolcelatte roquefort cauliflower cheese fondue. Fromage frais mozzarella.",
			"date": "Aug. 21, 2021",
			"image": "sandwich-tester.png",
			"author_image": "dr-reason-machete.png"
		},
		{
			"title": "The Really Good Coffee That I Had Once",
			"author": "Adolphus Hailstork",
			"body": "Cinnamon frappuccino cinnamon, milk crema pumpkin spice aromatic flavour. Caffeine kopi-luwak, as grinder fair trade that french press. Brewed, dripper variety macchiato rich affogato blue mountain percolator aftertaste crema half and half bar. Rich, ristretto decaffeinated at siphon wings robust. Crema organic a at viennese mug foam decaffeinated breve arabica. Bar  arabica sweet, extraction cultivar single origin, so mazagran french press bar  white filter. Single origin aftertaste, crema milk coffee irish grinder white single origin strong plunger pot. Et, coffee percolator crema at as aged white chicory. Macchiato crema aroma sugar cup black aged that.",
			"date": "Aug. 19, 2021",
			"image": "really-good-coffee.jpg",
			"author_image": "adolphus-hailstork.png"
		},
	]
}
```

Your blog post may not need images (this comes down to the style of the blog).  But it should include at least a title, author, and body.

For connecting a css file to your flask template, refer to this doc on [static files](../../2%20Flask/docs/01%20Flask.md#static-files).