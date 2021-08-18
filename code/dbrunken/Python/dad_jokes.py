'''
use API to get some dad jokes
'''

import pprint
import requests


url = 'https://icanhazdadjoke.com/'
headers = {'Accept' : 'application/json'}

response = requests.get(url, headers=headers)

# pprint.pprint(response.text)
data = response.json()
print(data['joke'])

#----------------------------VERSION 2-------------------------------#

