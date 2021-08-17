# For this lab we'll be using the Favqs Quotes API to first get a random quote, and then allow the user to find quotes by keyword. To accomplish this we'll be using the requests library.

# Version 1: Get a Random Quote

# The URL to get a random quote is https://favqs.com/api/qotd, send a request here, parse the JSON in the response into a python dictionary, and show the quote and the author.

import requests
import pprint

response = requests.get('https://favqs.com/api/qotd')
# print(response)

data = response.json()
# pprint.pprint(data)
quote = data['quote']
print(quote['author'])
print(quote['body'])