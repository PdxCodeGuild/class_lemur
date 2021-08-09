import requests # pip install requests or pip3 install requests or py -m pip install requests

# query = input('Welcome to the CocktailDB API.  What drink would you like to search for (or \'done\')?  ')

while True:
    query = input('Welcome to the CocktailDB API.  What drink would you like to search for (or \'done\')?  ')
    if query == 'done':
        break
    response = requests.get(f'https://www.thecocktaildb.com/api/json/v1/1/search.php?s={query}')
    # response = requests.get('https://www.thecocktaildb.com/fdsjkalfjdsa/json/v1/1/search.php?s=margarita') # 404

    # print(response) # <Response [200]>
    # print(type(response.text)) # <class 'str'>
    data = response.json()
    # print(type(data)) # <class 'dict'>
    drinks = data.get('drinks')
    if drinks is None:
        print('sorry we don\'t have that one')
        continue
    # print(type(drinks)) # <class 'list'>
    # first = drinks[0]
    # print(first.keys())
    for drink in drinks:
        print()
        print('-'*40)
        print(drink['strDrink'])
        print('Ingredients:')
        for key in drink.keys():
            if 'strIngredient' in key:
                if drink.get(key) is not None:
                    print('  • ' + drink.get(key))
        print('Instructions:')
        print(drink['strInstructions'])
        print('-'*40)
    
    print()


