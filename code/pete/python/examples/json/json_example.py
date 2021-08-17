import json

with open('cocktail.json', 'r') as f:
    raw_string = f.read()

print(raw_string)
print(type(raw_string))

data = json.loads(raw_string)
print(data)
print(type(data))

formatted_json = json.dumps(data, indent=4)

with open('cocktail.json', 'w') as f:
    f.write(formatted_json)