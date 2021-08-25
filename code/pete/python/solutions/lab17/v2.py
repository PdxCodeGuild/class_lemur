# Version 2: List Quotes by Keyword

# The Favqs Quote API also supports getting a list of quotes associated with a given keyword https://favqs.com/api/quotes?page=<page>&filter=<keyword>. Prompt the user for a keyword, list the quotes you get in response, and prompt the user to either show the next page or enter a new keyword. You can use string concatenation to build the URL.

import requests
# from pprint import pprint
from prettyprinter import cpprint

headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}

filter = input('Which quotes do you want to see? ')
page = 1

while True:
    params = {
        'filter': filter,
        'page': page
    }

    response = requests.get(f'https://favqs.com/api/quotes', params=params, headers=headers)

    # print(response)

    data = response.json()

    cpprint(data)

    quotes = data['quotes']

    try: 
        print(f"Page: {data['page']}")
        for quote in quotes:
            print()
            # print('-'*80)
            print(quote['author'])
            print(quote['body'])
            # print('-'*)

        next_page = input('type \'n\' for next page, type \'new\' for a new keyword search, or type \'done\' to quit  ')

        if next_page == 'n':
            page += 1
        elif next_page == 'new':
            filter = input('Which quotes do you want to see? ')
            page = 1
        else:
            break
    
    except KeyError:
        print('no quotes found')
        break