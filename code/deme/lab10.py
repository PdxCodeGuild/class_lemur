import string
ascii = list(string.ascii_lowercase)
rot = "nopqrstuvwxyzabcdefghijklm"
rot13 = list(rot)
def rot(user_input):
    user_input = list(user_input)
    #search for user_input in ascii
    output = []
    for char in user_input:
        rot_let = rot13[ascii.index(char)] #ascii.index(char) returns the index of the letters in user_input from ascii and finds the same letter in rot13 and returns the index of that letter in rot13
        output.append(rot_let) #adds each rot_let to output
    #convets list to string
    output = "".join(output)
    print(output)
word = input("Enter a word: ")
rot(word)