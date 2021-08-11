import requests

'''Part one'''

# response = requests.get('https://favqs.com/api/qotd')
# # print(response)
# # print(response.text)

# response = response.json()
# # print(type(response))
# response = response['quote']
# # print(response)

# quote = response['body']
# author = response['author']

# print(f'"{quote}"')
# print(f'- {author}')

'''Part two'''


while True:

    user_response = input("Please enter a keyword you'd like to search with or 'done' to exit: ")

    if user_response == 'done':
        break
    
    # url = 'https://favqs.com/api/quotes?page=<page>&filter=<keyword>' # full url

    url = 'https://favqs.com/api/quotes?' 
    headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}

    params = {
        'filter': user_response,
        'page': 1
    }

    while True:

        response = requests.get(url + f'/search/{user_response}', headers=headers, params=params)

        # print(response)
        # print(response.text)

        response = response.json()
        # print(response)

        response = response['quotes']
        # quote = data.get('quotes')

        for quote in response:

            print(quote['body'])
            print(quote['author'])

        next = input("Enter 'next page' to see the next page or 'done' to exit: ")

        if next == "next page":

            params['page'] += 1
                
        elif next == 'done':
            break

      