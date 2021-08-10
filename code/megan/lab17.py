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

    headers = {'Authorization': 'Token token="YOUR_APP_TOKEN"'}
    
    params = {
        'filter': user_response
    }

    # https://favqs.com/api/quotes?page=<page>&filter=<keyword>
    response = requests.get('https://favqs.com/api/quotes?page=<page>&', headers=headers, params=params)



    # print(response)
    print(response.text)

    response = response.json()
    # print(type(response))
    # response = response['quote']
    # # print(response)

    # quote = response['body']
    # author = response['author']


    # print(f'"{quote}"')
    # print(f'- {author}')

