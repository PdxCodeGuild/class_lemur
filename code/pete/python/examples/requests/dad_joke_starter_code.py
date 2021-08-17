import requests

url = 'https://icanhazdadjoke.com/'
headers = {'Accept': 'application/json'}

response = requests.get(url, headers=headers)

print(response)
print(response.text)
data = response.json()
print(data)

