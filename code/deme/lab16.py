import requests
import json
response = requests.get('https://icanhazdadjoke.com', headers = {'accept': 'application/json'})
data = response.json()
print(data['joke'])

# print(response.url)
# print(response.text)
# print(response.status_code) 
# print(response.encoding) 
# print(response.headers) 

