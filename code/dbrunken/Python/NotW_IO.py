'''
ARI
8/3/21
create an automated readability index
with the formula: 4.71(char/words) + 0.5(words/sentences) - 21.43
'''
import string
import re

with open('NotW.txt', 'r', encoding= 'utf-8') as f:
    book = f.read()
# print(book)

def counter(file):
    from string import whitespace
    char = len(book.translate(str.maketrans('', '', string.punctuation + whitespace)))
    words = len(book.split(' '))
    sentences = len(re.split(r'\w[.!?]', book))
    print(char, words, sentences)
    # def calc_ari(char, words, sentences):
    ari = (4.71*(char/words)) + (0.5*(words/sentences)) - 21.43
    # if 
    return round(ari)

ari_result = counter(book)
print(ari_result)

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

# for ari_result in ari_scale.keys():

# print(ari_scale[ari_result])
print(f"The ARI scale indicates that this book is good for ages {ari_scale[ari_result]['ages']}")
print(f"\nThat is roughly the equivalent of {ari_scale[ari_result]['grade_level']}")
