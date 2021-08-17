'''
For this lab we'll be using the Favqs Quotes API to first get a random quote, 
and then allow the user to find quotes by keyword. 
To accomplish this we'll be using the requests library.

Version 1: Get a Random Quote
The URL to get a random quote is https://favqs.com/api/qotd, 
send a request here, parse the JSON in the response into a python dictionary, 
and show the quote and the author.

Version 2: List Quotes by Keyword
The Favqs Quote API also supports getting a list of quotes associated with 
a given keyword https://favqs.com/api/quotes?page=<page>&filter=<keyword>.
Prompt the user for a keyword, list the quotes you get in response, and prompt
the user to either show the next page or enter a new keyword. You can use
string concatenation to build the URL.
'''


import pprint
import requests
import json
from time import sleep
from textwrap import fill
token='"6ac53ed6f4ae6184e6b11a7c9998a5b9"'
headers={'Content-Type': 'application/json', 'Authorization': f'Token token={token}'}
choice= str(input('Hit enter key for th quote of the day or enter a search term: '))

if choice == '':
    url='https://favqs.com/api/qotd'
    response=requests.get(url, headers=headers).json()
    print(response['quote']['body'])
    #qotd=response['quote'['body']]
    

else:
    page=1
    headers={'Authorization': f'Token token={token}'}
    while True:
        # search_url=f'https://favqs.com/api/quotes?page={page}&filter={choice}'
        url='https://favqs.com/api/quotes?'
        pull=requests.get(url, headers=headers, params={'format': 'json','page': page, 'filter': choice}).json()
        for quote in pull['quotes']:
            print(fill(quote['body'], width =60))
            print(f"\n  -{quote['author']}-\n\n")
        if pull['last_page']:
            print('End of quotes.')
            break
        if input('Would you like to see another page(y/n)? ') =='y': 
            page+=1
        else: break
