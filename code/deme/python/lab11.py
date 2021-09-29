with open ('book.txt', encoding ='utf-8') as f:
    book = f.read()

#calculate words
words = book.split()
words = len(words)

#calculate characters
characters = len(book)

#Calculate sentences by adding up punctuation counts.
sentences = 0
sentences += book.count('.') + book.count('!') + book.count('?')

#ARI calculation 
ari =(4.71 * (characters / words )) + (0.5 * (words / sentences )) - 21.43

#Round ARI Score
ari = round(ari)

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

#define dictionary index with ari variable
ari_object = ari_scale[ari]

print(f"The ARI for book.txt is {ari}\nThis corresponds to a {ari_object['grade_level']} level of difficulty\nthat is suitable for an average person of {ari_object['ages']} years old. ")
 