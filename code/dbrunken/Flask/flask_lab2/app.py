'''
flask 2 lab
incorporate user input from 102 lab
*User Login*
'''

from flask import Flask, render_template, request
from unit_5_lab import profiles, login_base

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/login/', methods= ['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = dict(request.form)
        login_name = data['username']
        login_pass = data['password']    
        # print(login_name, login_pass)
        for user in profiles:
            check_input =  login_base(login_name, login_pass, user)
            try:
                if check_input == True:
                    return render_template('index.html', check_input=check_input, username=login_name)
                profiles.get('username', 'password', check_input)
            except AttributeError:
                    got_error = True
                    return render_template('index.html', check_input=check_input, username=login_name, got_error=got_error)


                 

    return render_template('index.html', login_name=login_name, login_pass=login_pass)

# @app.route(profiles)

# while True: #close_out == 0:

#     for user in profiles:
#         check_input =  login(username, password, user)
#         if check_input == True:
#             break
    

#     if check_input != True:
#         try_again = input('would you like to try again? ')
#         no = 'no'
#         if try_again == no:
#             print('goodbye')
#             break

#     elif check_input == True:
#         break

app.run(debug=True)