"""Compute the ARI for a given body of text loaded in from a file. You can find a .txt file to use at Project Gutenberg.
The automated readability index (ARI) is a formula for computing the U.S. grade level for a given block of text. 
The general formula to compute the ARI is as follows:

The score is computed by multiplying the number of characters divided by the number of words by 4.71, adding the number of words divided by the number of sentences multiplied by 
0.5, and subtracting 21.43. If the result is a decimal, always round up. 
Scores greater than 14 should be presented as having the same age and grade level as scores of 14.

Scores correspond to the following ages and grad levels:

    Score  Ages     Grade Level
     1       5-6    Kindergarten
     2       6-7    First Grade
     3       7-8    Second Grade
     4       8-9    Third Grade
     5      9-10    Fourth Grade
     6     10-11    Fifth Grade
     7     11-12    Sixth Grade
     8     12-13    Seventh Grade
     9     13-14    Eighth Grade
    10     14-15    Ninth Grade
    11     15-16    Tenth Grade
    12     16-17    Eleventh grade
    13     17-18    Twelfth grade
    14     18-22    College
Once you’ve computed the ARI score, you can use the following dictionary to look up the age range and grade level.

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
The output should look something like the following:

--------------------------------------------------------

The ARI for gettysburg-address.txt is 12
This corresponds to a 11th Grade level of difficulty
that is suitable for an average person 16-17 years old.

--------------------------------------------------------
"""
#imported functions
from math import ceil
import re

#imported files
with open('Dorian_Grey.txt', 'r', encoding='utf-8') as f:
    wilde=f.read()
    #remove line breaks
    wilde=re.sub("\n"," ",wilde)




# Dictionaries and lists

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
#Functions

def ari_score(text):
    #get character count, word count, sentence count
    char_count=len(re.findall("[a-zA-Z]",text))
    word_count=len(re.findall(" [a-zA-Z]",text))
    sentence_count=len(re.findall("[.?!]", text))
    print(char_count, word_count, sentence_count)
    #apply equation
    score=ceil(4.71*(char_count/word_count)+0.5*(word_count/sentence_count)-21.43)
    return score

# with open('Dorian_Grey.txt', 'r', encoding='utf-8') as wilde_file:
#     wilde_lines = wilde_file.readlines()
#     for line in wilde_lines:
#         print(line)
print(ari_score(wilde))
ari = ari_score(wilde)
texts=(f' The ARI for Dorian_Grey.txt is {ari}\n',
f'This corresponds to a {ari_scale[ari]["grade_level"]} level of difficulty\n',
f'that is suitable for an average person {ari_scale[ari]["ages"]} years old.')
block_size = max(len(line) for line in texts)
print('-' * (block_size + 4))
print(*texts)
print('-' * (block_size + 4))

