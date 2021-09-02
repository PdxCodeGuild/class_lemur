from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        saturation = request.form['saturation']
        lightness = request.form['lightness']
        return render_template('index.html', hues=range(0, 361), saturation=saturation, lightness=lightness)
    return render_template('index.html', hues=range(0, 361), saturation=50, lightness=50)

app.run(debug=True)