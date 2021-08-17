# """
# EXERCISE 1
# Translate for loop to list comprehension
# """
# hats = ['baseball cap', 'fedora', 'derby', 'panama']
# for hat in hats:
# 	print(hat)

# # list comprehension version...
# [print(hat)for hat in hats]
# # hats = [print(hat)for hat in hats]
# # print(hats) # [None, None, None, None]

# """
# EXERCISE 2
# Translate for loop to list comprehension
# """
# dogs = ['pluto', 'fido', 'clifford', 'lassie']
# dog_facts = []
# for dog in dogs:
# 	# dog = dog.capitalize()
# 	dog_facts.append(f"{dog.capitalize()} is a good boy.")
# print(dog_facts)

# # list comprehension version...
# dog_facts = [f"{dog.capitalize()} is a good boy." for dog in dogs]
# print(dog_facts)

# """
# EXERCISE 3
# Translate for loop to list comprehension
# """
# numbers = [1, 238, 74, 364, 65, 23, 765]
# evens = []
# odds = []
# for number in numbers:
# 	if number % 2 == 0:
# 		evens.append(number)
# 	else:
# 		odds.append(number)
# print(odds)
# print(evens)
# # list comprehension version
# # evens = []
# # odds = [number if number % 2 == 1 else evens.append(number) for number in numbers] # [1, None, None, None, 65, 23, 765]

# odds = [number for number in numbers if number % 2 == 1]
# evens = [number for number in numbers if number % 2 == 0]

# print(odds)
# print(evens)

# if 1 == 2:
#     print("that's crazy")
# else:
#     print('ok, good')

"""
EXERCISE 4
Translate for loop to list comprehension
"""
spring = ['march', 'april', 'may']
summer = ['june', 'july', 'august']
fall = ['september', 'october', 'november']
winter = ['december', 'january', 'febuary']
seasons2d = [spring, summer, fall, winter]

for season in seasons2d:
    print(season)
    for month in season:
        print(month)

# list comprehension version...
[[print(month) for month in season] for season in seasons2d]

seasons_capitalized = [[month.capitalize() for month in season] for season in seasons2d]
print(seasons_capitalized)