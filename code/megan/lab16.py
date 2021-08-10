import requests

'''Part one'''

# url = 'https://icanhazdadjoke.com/'
# headers = {'Accept': 'application/json'}

# response = requests.get(url, headers=headers)

# # print(response)
# print(response.text)
# data = response.json()
# print(data)

# jokes = data.get('joke')
# print(jokes)

'''Part two'''

while True:

    word = input("Please enter the term you'd like to search with or 'done' to exit: ")

    if word == 'done':
        break

    headers = {'Accept': 'application/json'}

    params = {
        'term' : word
    }

    response = requests.get('https://icanhazdadjoke.com/search', headers=headers, params=params)
    # response = response.text
    # print(response.text)
    response = response.json()
    response = response['results']

    for object in response:
        print(object['joke'])
    