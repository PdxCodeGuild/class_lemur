# Class Lemur Day Course
# Lab 17, Quotes API
# Scott Cormack
# Python 3.9.6

import requests

# # Version 1
# url = 'https://favqs.com/api/qotd'

# response  = requests.get(url)

# data = response.json()
# data = data['quote']['body']
# author = response.json()
# author = author['quote']['author']

# print(f'''
# Your random quote is: "{data}"
# Written by {author}.
# ''')

# Version 2
search = input('Enter a word to search the quote database with or press enter to quit: ')
if search == '':
    print('Thank you for using the quote search program.')
    quit()

params = {
    'filter' : search,
    'page' : 1,
    'type' : 'tag'
}

while True:
    url = f'https://favqs.com/api/quotes/?filter='
    headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
    response = requests.get(url, headers = headers, params = params).json()
    response = response['quotes']
    print('*' * 80 + '\nHere are your quotes from page ' + str(params['page']))
    for i in response:
        data = i['body']
        author = i['author']
        print(f'{data} \nBy {author}.')
    x = input('Would you like to see the next page? Enter to quit, anything else to continue: ')
    if x == '':
        break
    else:
        params['page'] += 1  