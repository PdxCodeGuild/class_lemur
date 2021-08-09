'''
ROT13
encode user input into rot13
'''
from string import ascii_lowercase as letters

userText = list(input('type anything: '))
# rot_letters = 'nopqrstuvwxyzabcdefghijklm'
move = int(13)
encoded_text = ''

i = 0 

while i < len(userText):

    for letter in userText:
        if ord(letter) + move:
            encoded_text += (chr(ord(letter)) + (if chr(ord(letter)) > 109)
