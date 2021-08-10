import requests

url = "https://favqs.com/api/qotd"

headers = {
    'Content-type': 'application/json'
}

response = requests.get(url, headers=headers).json()
quote_json = response.get("quote")
author = quote_json.get("author")
quote = quote_json.get("body")
print(f"{quote} - {author}")