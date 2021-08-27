'''
Programming 101
unit 5 lab
'''

import random
import string

#create a 10 character string

length = int(input("Password length: "))

letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

pw = letters + numbers + symbols
pw2 = ''

while length > 0:
    pw2 += pw
    length = length - 1
#if length == 0:
    #length 
print(pw2)