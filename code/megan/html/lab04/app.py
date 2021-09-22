from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		form_data = dict(request.form)
		print(form_data)
		

		# Version 2 (optional):
		# render a confirmation page
		# return render_template('confirmation', confirmation_data=???)

		# Version 3 (optional):
		# redirect to another view, sending the form_data info along
		# https://sodocumentation.net/flask/topic/6856/redirect
		# return redirect(url_for('confirmation', confirmation_data=???))

	return render_template('index.html') # index.html is the template with the form

# @app.route('/confirmation/<confirmation_data>/')
# def confirmation(confirmation_data):