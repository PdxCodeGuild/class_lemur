# Class Lemur Day Course
# Lab 16, Dad Joke API
# Scott Cormack
# Python 3.9.6

import requests
from time import sleep

# # Version 1
# url = 'https://icanhazdadjoke.com/'
# headers = {'Accept': 'application/json'}

# response  = requests.get(url, headers=headers)

# data = response.json()

# print('Your random, horribly cringe Dad joke is here...')
# sleep(1.5)
# print(data['joke'])
# sleep(1.5)
# print('Yayy....?')

headers = {'Accept' : 'application/json'}

while True:
    query = input('Enter your cheesy dad joke search word or just push enter to quit: ').lower()
    if query == '':
        print('Good call.  You dodged a time waster there.')
        break
    url = f'https://icanhazdadjoke.com/search?term={query}'

    response = requests.get(url, headers = headers)
    data = response.json()
    data = data['results']
    # print(data)
    for i in data:
        print(i['joke'])
        x = input('Press enter to see the next joke or "quit" to stop.').lower()
        if x == 'quit':
            print('''Thanks for going on this mega cheese journey of cheesiness.
    You will not get this time back... ever...
        ''')
            break