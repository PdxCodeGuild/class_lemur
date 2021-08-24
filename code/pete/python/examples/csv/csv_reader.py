with open('code/pete/examples/csv/cities.csv', 'r') as file:
    lines = file.read().split('\n')
for line in lines:
    print(line)
## turn raw csv string into list of dictionaries
cities = [
    {'name': 'Portland', 'cuisine': 'everything', 'country': 'USA', 'weather': 'temperate'},
    {'name': 'Detroit', 'cuisine': 'Greek', 'country': 'USA', 'weather': 'temperate'},
    {'name': 'D.C.', 'cuisine': 'ramen', 'country': 'USA', 'weather': 'temperate'},
    {'name': 'Florence', 'cuisine': 'pasta', 'country': 'Italy', 'weather': 'hot'},
]
## turn list of dictionaries back into a properly-formatted
## .csv file