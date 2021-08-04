"""
Access element from list: mylist[i]
Given the list of seasons, print out 'summer'
"""
from random import shuffle
seasons = ['spring', 'summer', 'fall', 'winter']
print(seasons[1])
print(seasons[-3])


"""
Access element from nested lists: mylist[i][j]
Given the 2D list of seasons, print out 'july'
"""
spring = ['march', 'april', 'may']
summer = ['june', 'july', 'august']
fall = ['september', 'october', 'november']
winter = ['december', 'january', 'febuary']

seasons2d = [spring, summer, fall, winter]
print(seasons2d[1][1])


"""
Assignment mylist[i] = value
In the list seasons, change 'fall' to 'autumn'
"""
seasons[2] = 'autumn'
print(seasons)

"""
Assignment to nested lists
Fix the 'febuary' typo in winter THROUGH seasons2d
"""
seasons2d[3][2] = 'february'
print(seasons2d)

"""
Loops
Loop over seasons to print out each season
"""
seasons = ['spring', 'summer', 'fall', 'winter']
for season in seasons:
    print(season)


"""
Loop over seasons to print out each season using range() and len()
"""
for i in range(len(seasons)):
    print(seasons[i])


"""
Nested Loops
Loop over seasons2d AND the nested lists to print out each month
"""
seasons2d = [spring, summer, fall, winter]
for season in seasons2d:
    # print(season)
    for month in season:
        print(month)


"""
Using range() and len(), loop over seasons2d to print out each month
"""
for i in range(len(seasons2d)):
    season = seasons2d[i]
    for j in range(len(season)):
        print(season[j])

for i in range(len(seasons2d)):
    for j in range(len(seasons2d[i])):
        print(seasons2d[i][j])

"""
Inclusion: element in mylist
Append: mylist.append(element)
Use in and append to makes sure all the items_to_add are in grocery_list just once
"""
grocery_list = ['apples', 'bananas', 'oranges']
items_to_add = ['bananas', 'blueberries']
for item in items_to_add:
    if item not in grocery_list:
        grocery_list.append(item)
print(grocery_list)

"""
Insert: mylist.insert(index, element)
Add mangos to the top of the list
"""
grocery_list = ['apples', 'bananas', 'oranges']
grocery_list.insert(0, 'mangos')
print(grocery_list)

"""
Remove: mylist.remove(element)
Remove bananas from the list with .remove()
"""
grocery_list = ['apples', 'bananas', 'oranges']
grocery_list.remove('bananas')

"""
Pop: mylist.pop(index)
Using .pop(), remove brocolli from fruits and add it to vegetables
"""
fruits = ['apples', 'oranges', 'brocolli']
vegetables = ['potatoes', 'radishes', 'celery']
brocolli = fruits.pop(2)
vegetables.append(brocolli)
# vegetables.append(fruits.pop(2))
print(fruits, vegetables)


"""
Index: mylist.index(element)
Remove oranges from the randomized list with .pop()
"""
grocery_list = ['apples', 'bananas', 'oranges']
shuffle(grocery_list)  # grocery_list is now randomly shuffled
# index = grocery_list.index('oranges')
# grocery_list.pop(index)
grocery_list.pop(grocery_list.index('oranges'))
print(grocery_list)

"""
Remove all the mangos from too_many_mangos
"""
#					0			1		2			3		4				5			6			7		8
too_many_mangos = ['apples', 'mangos', 'bananas', 'mangos',
                   'blueberries', 'mangos', 'oranges', 'mangos', 'mangos']
# for fruit in too_many_mangos:
# 	if fruit == 'mangos':
# 		too_many_mangos.remove(fruit)
while 'mangos' in too_many_mangos:
    too_many_mangos.remove('mangos')
print(too_many_mangos)

# """
# Slicing mylist[start:end:step]
# Use slicing to print out a list of the programming langagues
# """

# languages = ['Python', 'JavaScript', 'Japanese', 'English', 'Arabic', 'Greek', 'Hindi']
# print(languages[0:2])
# # print(languages[:2])


# languages = ['Chinese', 'Spanish', 'Arabic', 'Python', 'JavaScript', 'C#', 'Java']
# print(languages[3:])


# languages = ['English', 'Thai', 'French', 'German', 'Rust', 'C', 'Go', 'Assembly', 'COBOL', 'Icelandic', 'Italian']
# print(languages[4:9])


# languages = ['JavaScript', 'English', 'French', 'Rust', 'Norwegian', 'Danish', 'Python']
# print(languages[::3])


# languages = ['Swahili', 'Go', 'Afrikaans', 'Java', 'Romansh', 'GDScript', 'Quechua']
# print(languages[1::2])


# """
# Use slicing to print out a list of the course sections in the order we will be covering them
# """
# languages_frameworks_engines_etc = ['Unity', 'Angular', 'French', 'Django Rest Framework', 'Russian', 'Lua', 'Vue', 'Pascal', 'Godot', 'JavaScript', 'Korean', 'PHP', 'Django', 'Perl', 'Dutch', 'CSS', 'Express', 'HLSL', 'HTML', 'Unreal Engine', 'Dothraki', 'Flask', 'Elvish', 'Doggo-Speak', 'Python', 'High Valyrian', 'Morse Code', 'C++']
# print(languages_frameworks_engines_etc[-4:2:-3])

# languages_frameworks_engines_etc.reverse()
# print(languages_frameworks_engines_etc)
# languages_frameworks_engines_etc.sort()
# print(languages_frameworks_engines_etc)
# print(languages_frameworks_engines_etc[::-1])
