import requests

'''Part one'''

response = requests.get('https://favqs.com/api/qotd')
# print(response)
# print(response.text)

response = response.json()
# print(type(response))
response = response['quote']
# print(response)

quote = response['body']
author = response['author']

print(f'"{quote}"')
print(f'- {author}')

'''Part two'''
