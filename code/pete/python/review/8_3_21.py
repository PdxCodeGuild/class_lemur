"""STRINGS"""
# 1. Print out all the letters (each on their own line) in message, capitalized

message = 'Coding is fun.'
for letter in message:
    print(letter.upper())

# 4. Redefine message so it ends in an exclamation point instead of a period
# (Note: Redefine, not change.  Strings are immutable and cannot be changed)
message = message[:-1] + '!'
print(message)

# message = list(message)
# print(message)
# message[-1] = '!'
# print(message)
# message = ''.join(message)
# print(message)


"""DICTIONARIES"""
# 2. Change the evening value to the appropriate boolean
class_lemur = {
    'instructor': 'Pete',
    'ta': 'Lisa',
    'evening': True,
    'subjects': ['Python', 'Flask', 'Django'],
}
class_lemur['evening'] = False
class_lemur['day'] = True
print(class_lemur)

# 5. Add the missing subjects to to the dictionary's 'subjects' value, in order
class_lemur['subjects'].insert(2, 'JavaScript')
class_lemur['subjects'].append('Vue')
class_lemur['subjects'].append('Django REST Framework')
print(class_lemur)


"""LISTS"""
# 3. Insert the missing subjects into the list in the order they'll appear in
# the course (Note: Python is before HTML/CSS. Django is after Flask)
subjects = ['HTML/CSS', 'Flask', 'JavaScript', 'Vue', 'Django REST Framework']
subjects.insert(0, 'Python')
subjects.insert(3, 'Django')
print(subjects)

# 6. Use the list.sort() method to sort the list of subject dictionaries by
# their start week key
subjects = [
    {
        'subject': 'HTML/CSS',
        'start_week': 5,
        'concepts': ['design', 'color theory', 'accessibility']
    },
    {
        'subject': 'Python',
        'start_week': 1,
        'concepts': ['nested data structures', 'booleans', 'floats']
    },
    {
        'subject': 'Django',
        'start_week': 7,
        'concepts': ['databases', 'model view controller', 'url patterns']
    },
    {
        'subject': 'Flask',
        'start_week': 6,
        'concepts': ['template rendering', 'servers']
    },
    {
        'subject': 'Django REST Framework',
        'start_week': 12,
        'concepts': ['apis', 'serializers']
    },
    {
        'subject': 'Vue',
        'start_week': 11,
        'concepts': ['state management', 'lifecycle hooks']
    },
    {
        'subject': 'JavaScript',
        'start_week': 9,
        'concepts': ['closures', 'scope', 'asynchronous code']
    },
]

def sorting_function(subject):
    return subject['start_week']

# sorting_function2 = lambda subject: subject['start_week']

# subjects.sort(key=lambda subject: subject['start_week'])
subjects.sort(key=sorting_function)
print(subjects)

# for subject in subjects:
#     print(sorting_function(subject))

# 7. With the sorted subjects list, print out a course overview
# For example, the Python section should look like this:
"""
----------------------------------------
Week 1: Python
Concepts:
  - nested data structures
  - booleans
  - floats
----------------------------------------
"""

for subject in subjects: # subject is each dictionary
    # print(subject)
    print(f"""
----------------------------------------
Week {subject['start_week']}: {subject['subject']}
Concepts:""") # you can access that dictionary's key/value pairs
    for concept in subject['concepts']: # concept is each string inside of the sub-list of concepts
        print(f'  - {concept}')
    print('----------------------------------------')