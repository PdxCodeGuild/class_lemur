import re

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


with open('gatsby.txt', 'r') as f:
    book = f.read()
    # print(book)

words = re.findall('\w+', open('gatsby.txt').read())
print(len(words))

characters = len(book)
print(characters)

sentences = len(book.split())
print(sentences)

def ari(a, b, c):
    # return 4.71 (a / b) + 0.5 (b / c) - 21.43
    return a + b + c

print(ari(characters, words, sentences))

# for number in ari_scale:

#     print(f"""
#     --------------------------------------------------------
#     The ARI for gatsby.txt is {ari}. This corresponds to a {ari}: {ari_scale['grade_level']} of difficulty that is suitable for an average person of {ari}:{ari_scale['ages']}
#     """)
#     print('--------------------------------------------------------')

'''
The ARI for gettysburg-address.txt is 12
This corresponds to a 11th Grade level of difficulty
that is suitable for an average person 16-17 years old.
'''