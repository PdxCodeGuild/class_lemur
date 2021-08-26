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

encoded_list = [chr(ord(char) + move) if ord(char) < 110 else chr(ord(char) - move) for char in userText]
# if a letter is over 110 on chr(ord(letters)) then move -26, or move
encoded_text = ''.join(encoded_list, )
print(encoded_text)