'''
Write a program that prompts the user for a string, and encodes it with ROT13.
 For each character, find the corresponding character, add it to an output string.
  Notice that there are 26 letters in the English language, so encryption is the
   same as decryption.
'''


user_string = input("Please enter a string to be encoded: ")

shift = int(input("Enter the amount of rotaions for encoding: "))

encoded_string = ""

i = 0

# Use a while loop to go through user_string and then for each letter
# change it to the unicode number and add the shift.
while i < len(user_string):
    for letter in user_string:
        if ord(letter) + shift > 122:
            encoded_string += chr((ord(letter) + shift) - 26)
        else:
            encoded_string += chr(ord(letter) + shift)
        i += 1

print(encoded_string)
