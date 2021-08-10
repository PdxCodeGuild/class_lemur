'''
Part 2 (optional)
Add the ability to "search" for jokes using another endpoint. 
Create a REPL that allows one to enter a search term and go through jokes 
one at a time. You can also add support for multiple pages.
'''

import requests
import cowsay
import json
from time import sleep


url='https://icanhazdadjoke.com/'
headers={'Accept': 'application/json'}

choice= str(input('Hit enter key for random joke or enter a search term: '))

if choice == '':
    response=requests.get(url, headers=headers).json()
    joke=response['joke']
    if '?' in joke:
        question=joke.split('?')[0]
        response=joke.split('?')[1]
        cowsay.stegosaurus(f'{question}?')
        sleep(3)
        cowsay.trex(response)


    else:
        cowsay.trex(response['joke'])

else:
    i=0
    searchurl=url+f'search?term={choice}'
    results=requests.get(searchurl, headers=headers).json()['results']
    for result in results:
        i+=1
        stopper=input('hit enter for joke')
        print(result['joke'])
    if i >0:
        print("that's all the jokes!")
    else:
        print(f"we didn't find any jokes that mentioned '{choice}'.")
    
