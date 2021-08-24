from os import read
import math 
import re

text_file_list = ["the_grinch.txt", "the_golden_bird_Grimms.txt", "emporers_new_clothes.txt"]

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
def open_and_read(text_file_to_read):
    with open(text_file_to_read, encoding='UTF8') as file:
        text_file = file.read()
    file_name = file.name
    file.close()
    return text_file, file_name

def count_sent_word_char(text_file):
    sentence_count = len(re.split('[.!?]', text_file))
    word_count = len(re.split("\s+", text_file))
    character_count = len(re.findall('\w', text_file))
    return character_count, word_count, sentence_count

def calculate_ari(character_count, word_count, sentence_count):
    ari = (4.71 * (character_count/word_count)) + (.5 * (word_count/sentence_count)) - 21.43
    ari = math.ceil(ari)
    if ari > 14:
        ari = 14
    return ari

def main(text_file_list):
    for text_file_in_list in text_file_list:
        text_file, file_name = open_and_read(text_file_in_list)
        character_count, word_count, sentence_count = count_sent_word_char(text_file)
        ari = calculate_ari(character_count, word_count, sentence_count)
        print(f"The ARI for {file_name} is {ari}")
        print(f"This corresponds to a {ari_scale[ari]['grade_level']} level of difficulty")
        print(f"that is suitable for an average person {ari_scale[ari]['ages']} years old.")

main(text_file_list)
