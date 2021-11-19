import requests
import json
# response = requests.get('https://icanhazdadjoke.com', headers = {'accept': 'application/json'})
# data = response.json()
# print(data['joke'])

# headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}

search = input("Search for a joke or enter 'done' to exit:\n ")
repeat = True
while repeat == True: 
    if search != "done":
        response = requests.get('https://icanhazdadjoke.com/search', headers = {'Accept': 'application/json'}, params={'limit' : 25, 'term' : search })
        data = response.json()
        # print(data)
        # data = data['results']

        for joke in data['results']:
            print(joke['joke'])
    else:
        break
    


################ end point





# print(response.url)
# print(response.text)
# print(response.status_code) 
# print(response.encoding) 
# print(response.headers) 

