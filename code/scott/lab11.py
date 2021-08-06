# Class Lemur Day Course
# Lab 11, ARI
# Scott Cormack
# Python 3.9.6

'''
After thinking about this one, it is actually far more difficult to count the actual number
of sentences in a text.  There seems to be a lot more to it than just counting punctuation as there
can be punctuation in abbreviations etc. (See what I did there!) After googling it for 2 minutes
getting an ACTUAL sentence count would require a TON of effort and the importing of modules.
'''
import math

# Use provided ARI scale dictionary
ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}

# Open and read A Tale of Two Cities
file = 'book.txt'
with open (file, encoding = 'utf-8') as f:
    raw = f.read()

# Calculate number chars minus spaces
num_chars = raw.strip(' ')
num_chars = len(num_chars)
print(num_chars)

# Calculate number of words
num_words = len(raw.split())
print(num_words)

# Calculate number of sentences
num_sent = raw.count('.') + raw.count('?') + raw.count('!')

# Calculate score
score = ((((num_chars / num_words) * 4.71) + ((num_words / num_sent) * 0.5)) - 21.43)
score = math.ceil(score)

# Display results
print('*' * 80)
print(f'''
The ARI for A Tale of Two cities is {score}.
This corresponds to a {ari_scale[score]['grade_level']} level of difficulty.
that is suitable for an average person {ari_scale[score]['ages']} years old.
''')
print('*' * 80)




