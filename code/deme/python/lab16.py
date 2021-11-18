import requests
import json
# response = requests.get('https://icanhazdadjoke.com', headers = {'accept': 'application/json'})
# data = response.json()
# print(data['joke'])

# headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}

search = input("Search for a joke\n")
response = requests.get('https://icanhazdadjoke.com/search', headers = {'Accept': 'application/json'}, params={'term' : search})
data = response.json()
print(data)
# data = data['results']

# for joke in data:
#     print(joke['joke'])

################ end point





# print(response.url)
# print(response.text)
# print(response.status_code) 
# print(response.encoding) 
# print(response.headers) 

