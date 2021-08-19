from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print('you did a POST request')
        print(request.form)
        percent = int(request.form.get('percent').strip('%'))
        # print(percent, type(percent))
        # if percent < 60:
        #     grade = 'F'
        # elif percent < 70:
        #     grade = 'D'
        # elif percent < 80:
        #     grade = 'C'
        # elif percent < 90:
        #     grade = 'B'
        # elif percent <= 100:
        #     grade = 'A'
        # else:
        #     grade = 'Not a valid percent'
        return render_template('index.html', percent=percent) #, grade=grade)
        
    print('you did a GET request')
    return render_template('index.html')

@app.route('/redirect-start/')
def redirect_start():
    print('you are redirecting!')
    return redirect('/redirect-end')

@app.route('/redirect-end/')
def redirect_end():
    print('you are being redirected')
    return 'you have been redirected'

app.run(debug=True)
