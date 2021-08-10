'''
Use the Dad Joke API to get a dad joke and display it to the user. 
You may want to also use time.sleep to add suspense.

Part 1
Use the requests library to send an HTTP request to https://icanhazdadjoke.com/ 
with the accept header as application/json. 
This will return a dad joke in JSON format. 
You can then use the .json() method on the response to get a dictionary. 
Get the joke out of the dictionary and show it to the user.

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

