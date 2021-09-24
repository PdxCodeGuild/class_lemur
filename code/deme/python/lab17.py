import requests

response = requests.get('https://favqs.com/api/qotd')
print(f"status code: {response.status_code}")
data = response.json()
quote = data['quote']
print(quote['author'])
print(quote['body'])
headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
page = 1
filter = input('Enter a keyword to search for quotes: ')

while True:
    params = {
        'filter': filter,
        'page': page
    }

    response = requests.get(f'https://favqs.com/api/quotes', headers=headers, params=params)
    # print(response.text)
    data = response.json()
    quotes = data['quotes']
    num = 0

    #count number of quotes displayed
    for quote in data['quotes']:
        num += 1
    print(f"{num} quotes associated with {filter} - page {data['page']}")

    #display author and quotes
    for quote in quotes:
            print()
            print(quote['author'])
            print(quote['body'])

    action = input("Enter 'next page', 'new keyword' or 'done': ")

    if action == 'next page':
        page += 1
    elif action == 'new keyword':
        filter = input('Enter a keyword to search for quotes: ')
    else:
        break
