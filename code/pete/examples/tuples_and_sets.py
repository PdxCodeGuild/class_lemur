"""TUPLES"""

students = ('demetric', 'megan', 'dbrunken', 'swarty', 'matt', 'scott', 'mark')
students2 = list(students)
students3 = tuple(students2)
print(students, students2, students3)
# students.append('and') # AttributeError: 'tuple' object has no attribute 'append'
instructors = ('pete',)
print(instructors, type(instructors))
graduates = ()
print(graduates, type(graduates))

def translate(word):
    if word == 'hello':
        return 'hola', 'bonjour', 'konichiwa'

translations = translate('hello')
print(translations, type(translations))
spanish, french, japanese = translate('hello')
print(spanish, french, japanese)

colors = ['red', 'green', 'blue']
for i, color in enumerate(colors):
    print(f'color {color} is at index {i}')


"""SETS"""

print({1,2,2,3,1,4})

numbers = {1,2,3,4,5}
odds = {1, 3, 5}
print(numbers.difference(odds))

scotts_fruits = {'plums', 'cherries', 'pears'}
swartys_fruits = {'cherries', 'oranges', 'pears'}
print(scotts_fruits.intersection(swartys_fruits))


"""ZIP"""

letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
print(list(zip(letters, numbers)))

for letter, number in zip(letters, numbers):
    print()
    print(letter, number)