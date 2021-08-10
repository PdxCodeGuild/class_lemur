import requests

response = requests.get('https://api.ipify.org')

print(response) # <Response [200]>
print(type(response)) # <class 'requests.models.Response'>

print(response.text) # 76.105.186.48

print(response.url) # https://api.ipify.org
print(response.status_code) # 200
print(response.encoding) # ISO-8859-1
print(response.headers)
# {
#     'Server': 'Cowboy',
#     'Connection': 'keep-alive',
#     'Content-Type': 'text/plain',
#     'Vary': 'Origin',
#     'Date': 'Tue, 10 Aug 2021 17:05:40 GMT',
#     'Content-Length': '13',
#     'Via': '1.1 vegur'
# }

response = requests.get('https://gutenberg.org/files/14568/14568-0.txt')

response.encoding = 'utf-8'
print(response.text)
print(response)