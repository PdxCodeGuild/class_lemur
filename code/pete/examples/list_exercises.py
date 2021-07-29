# https://github.com/PdxCodeGuild/class_wallaby/blob/main/1%20Python/docs/09%20Lists%20%26%20Tuples.md#list-operations
"""
Access element from list: mylist[i]
Given the list of seasons, print out 'summer'
"""
seasons = ['spring', 'summer', 'fall', 'winter']


"""
Access element from nested lists: mylist[i][j]
Given the 2D list of seasons, print out 'july'
"""
spring = ['march', 'april', 'may']
summer = ['june', 'july', 'august']
fall = ['september', 'october', 'november']
winter = ['december', 'january', 'febuary']

seasons2d = [spring, summer, fall, winter]


"""
Assignment mylist[i] = value
In the list seasons, change 'fall' to 'autumn'
"""


"""
Assignment to nested lists
Fix the 'febuary' typo in winter THROUGH seasons2d
"""


"""
Loops
Loop over seasons to print out each season
"""


"""
Loop over seasons to print out each season using range() and len()
"""


"""
Nested Loops
Loop over seasons2d AND the nested lists to print out each month
"""


"""
Using range() and len(), loop over seasons2d to print out each month
"""


"""
Inclusion: element in mylist
Append: mylist.append(element)
Use in and append to makes sure all the items_to_add are in grocery_list just once
"""
grocery_list = ['apples', 'bananas', 'oranges']
items_to_add = ['bananas', 'blueberries']



"""
Insert: mylist.insert(index, element)
Add mangos to the top of the list
"""
grocery_list = ['apples', 'bananas', 'oranges']


"""
Remove: mylist.remove(element)
Remove bananas from the list with .remove()
"""
grocery_list = ['apples', 'bananas', 'oranges']


"""
Pop: mylist.pop(index)
Using .pop(), remove brocolli from fruits and add it to vegetables
"""
fruits = ['apples', 'oranges', 'brocolli']
vegetables = ['potatoes', 'radishes', 'celery']


"""
Index: mylist.index(element)
Remove oranges from the randomized list with .pop()
"""
from random import shuffle
grocery_list = ['apples', 'bananas', 'oranges']
shuffle(grocery_list) # grocery_list is now randomly shuffled


"""
SKIP ME!!
Remove all the mangos from too_many_mangos
too_many_mangos = ['apples', 'mangos', 'bananas', 'mangos', 'blueberries', 'mangos', 'oranges', 'mangos', 'mangos']
DON'T DO THIS ONE!
"""


"""
Slicing mylist[start:end:step]
Use slicing to print out a list of the programming langagues
"""

languages = ['Python', 'JavaScript', 'Japanese', 'English', 'Arabic', 'Greek', 'Hindi']


languages = ['Chinese', 'Spanish', 'Arabic', 'Python', 'JavaScript', 'C#', 'Java']


languages = ['English', 'Thai', 'French', 'German', 'Rust', 'C', 'Go', 'Assembly', 'COBOL', 'Icelandic', 'Italian']


languages = ['JavaScript', 'English', 'French', 'Rust', 'Norwegian', 'Danish', 'Python']


languages = ['Swahili', 'Go', 'Afrikaans', 'Java', 'Romansh', 'GDScript', 'Quechua']


"""
Use slicing to print out a list of the course sections in order
"""
languages_frameworks_engines_etc = ['Unity', 'Angular', 'French', 'Django Rest Framework', 'Russian', 'Lua', 'Vue', 'Pascal', 'Godot', 'JavaScript', 'Korean', 'PHP', 'Django', 'Perl', 'Dutch', 'CSS', 'Express', 'HLSL', 'HTML', 'Unreal Engine', 'Dothraki', 'Flask', 'Elvish', 'Doggo-Speak', 'Python', 'High Valyrian', 'Morse Code', 'C++']