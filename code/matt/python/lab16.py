import requests
import cowsay
import time

url = 'https://icanhazdadjoke.com/'
headers = {'Accept': 'application/json'}

response = requests.get(url, headers=headers)

data = response.json()

print(cowsay.stegosaurus(data['joke']))

search_url = 'https://icanhazdadjoke.com/search'

while True:
    print('*' * 40)
    query = input('Input the term you want to search for (or done to exit): ')
    print('*' * 40)
    params = {
        'term': query
    }

    if query == 'done':
        break

    response = requests.get(search_url, headers=headers, params=params)
    response.encoding = 'utf-8'
    data = response.json()

    jokes = data.get('results')
    print(jokes)
    for joke in jokes:
        print()
        print('-' * 40)
        print()
        if '?' in joke['joke']:
            joke_with_questionmark = joke['joke'].split('? ')
            for joke in joke_with_questionmark:
                print(joke)
                time.sleep(.5)
        else:
            print(joke['joke'])
