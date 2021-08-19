from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/') # the route, or URL path of the view
def index(): # the view function
    return render_template('index.html')

@app.route('/advice/', methods=['POST'])
def advice():
    print(request.form)
    card1 = int(request.form.get('card1'))
    card2 = int(request.form.get('card2'))
    card3 = int(request.form.get('card3'))
    print(card1, card2, card3)
    total = card1 + card2 + card3

    if total < 17:
        advice = 'hit'
    elif total < 21:
        advice = 'stay'
    elif total == 21:
        advice = 'blackjack'
    else:
        advice = 'bust'
    return render_template('advice.html', total=total, advice=advice)




app.run(debug=True)