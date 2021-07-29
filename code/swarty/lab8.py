"""
Lab 8 David Swartwood

Write a program that prompts the user for a string, and encodes it with ROT13. For each character, find the corresponding character, 
add it to an output string. Notice that there are 26 letters in the English language, so encryption is the same as decryption.

V2 Allow the user to input the amount of rotation used in the encryption / decryption
"""
letters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
initial=input("Enter the phrase to encode: ")
#initial="This is the way"                                               #test phrase
initial=initial.lower()
initial=list(initial)
#encoding
#rotation=13                                                            #V1
rotation=int(input("Enter a number between 1-25 to set rotation: "))    #V2
final=""
for char in initial:
    if char.isalpha:                                                    #watch for non alpha
        rotindex=letters.index(char)                                    #index inital ltter to cypher
    if rotindex >=(26-rotation):                                        #keep numbers in range
            rotindex-=26
        final+=(letters[rotindex+rotation])                             #apply rotation
    else:                                                               #pass through non alpha
        final+=(char)

print(final)