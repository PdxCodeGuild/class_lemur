'''
use API to get some dad jokes
'''

import pprint
import requests


url = 'https://icanhazdadjoke.com/'
headers = {'Accept' : 'application/json'}

# response = requests.get(url, headers=headers)

# # pprint.pprint(response.text)
# data = response.json()
# print(data['joke'])

#----------------------------VERSION 2-------------------------------#

while True:
    query = input('Enter keyword to search by: ').upper()
    if query == '':
        print('no jokes for you, which is better anyway')
        break

    url = f'https://icanhazdadjoke.com/search?term={query}'

    response = requests.get(url, headers=headers)
    data = response.json()
    data = data['results']

    for i in data:
        print(i['joke'])
        anuthaOne = input('press enter to get more jokes or "exit" to stop: ')
        if anuthaOne == 'exit':
            print('no more jokes for you')
            break