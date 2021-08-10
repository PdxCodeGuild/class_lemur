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
