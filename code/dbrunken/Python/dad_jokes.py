'''
use API to get some dad jokes
'''

import requests

while True:
    url = 'https://icanhazdadjoke.com/'

    headers = {'Accept' : 'application/json'}