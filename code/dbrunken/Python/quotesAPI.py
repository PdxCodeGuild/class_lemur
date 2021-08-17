'''
get and pull quotes from favqs.com
'''

import requests
import pprint

# response = requests.get('https://favqs.com/api/qotd')

# data = response.json()
# # pprint.pprint(data)

# quote = data['quote']
# print(quote['body'])


#------------------------------VERSION 2----------------------------------------------#

headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
filter = input('what quote are you looking for? ')
page = 1

while True:

    params = {
        'filter': filter,
        'page': page
    }

    response = requests.get(f'https://favqs.com/api/quotes',params=params, headers=headers)

    print(response)
    data = response.json()
    pprint.pprint(data)

    quotes = data['quotes']

    for quote in quotes:
        print('-' * 40)
        print(quote['author'])
        print(quote['body'])
    
    next_page = input("type 'n' for next page, type 'new' for new search, or type 'done' to quit. \n")

    if next_page == 'n':
        page +=1
    elif next_page =='new':
        filter = input('What new keyword do you want to search by? ')
    else:
        break
