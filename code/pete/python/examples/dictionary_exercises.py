miles_morales = {
    'superhero': 'Spider-Man',
    'age': 17,
    'home': 'New York City',
    'family': ['Jefferson Davis', 'Rio Morales'],
    'occupation': 'student'
}

"""
Access: dict[key] or dict.get(key)
Access the 'superhero' key to print Miles' superhero name
"""
# print(miles_morales['superhero'])
# print(miles_morales.get('superhero'))

"""
Update: dict[key] = value
Happy Birthday Miles 🎂
Increase Miles' age by 1
"""
miles_morales['age'] += 1
# print(miles_morales)

"""
Add Miles' uncle, Aaron Davis, to the family value
"""
miles_morales['family'].append('Aaron Davis')
# print(miles_morales)


"""
Add key/value pair: dict[key] = value
Add more info to the miles_morales dictionary
"""
miles_morales['school_name'] = 'Brooklyn Visions Academy'
miles_morales['abilities'] = []
miles_morales['abilities'].append('web slinging')
miles_morales['abilities'].append('wall crawling')
miles_morales['abilities'].append('invisibility')

print('🕷️  Miles Morales  🕷️')
print()
for key in miles_morales.keys():
    print('🕸  ' + key, end='\n\t')
    print(miles_morales[key])
