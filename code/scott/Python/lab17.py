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
search = input('Enter a word to search the quote database with or enter "exit" to quit: ').lower()
if search == 'exit':
    print('Thank you for using the quote search program.')
    quit()

params = {
    'filter' : search,
    'page' : 1,
    'type' : 'tag'
}

while True:
    url = f'https://favqs.com/api/quotes/'
    headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
    response = requests.get(url, headers = headers, params = params).json()
    response = response['quotes']
    print('*' * 80 + '\nHere are your quotes from page ' + str(params['page']))
    for i in response:
        data = i['body']
        author = i['author']
        print(f'{data} \nBy {author}.')
    x = input('If you would you like to see the next page, enter "n"? If you would like to search for new quotes, enter your search term.  Type "exit" to quit: ').lower()
    if x == 'exit':
        print('Thank you for using the quote search program.')
        quit()
    elif x == 'n':
        params['page'] += 1
    else:
        params['filter'] = x