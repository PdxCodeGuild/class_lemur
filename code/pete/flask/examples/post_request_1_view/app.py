from flask import Flask, render_template, request

from num_to_phrase import translate

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST']) # the route, or URL path of the view
def index(): # the view function
    if request.method == 'POST':
        # number = request.form.get('number')
        print(request.form, type(request.form))
        data = dict(request.form)
        print(data, type(data))
        number = int(data.get('number'))
        print(number)
        phrase = translate(number)
        print(phrase)
        return render_template('index.html', number=number, phrase=phrase)

    return render_template('index.html')

app.run(debug=True) # you need this or nothing will happen!
