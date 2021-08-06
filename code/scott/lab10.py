# Class Lemur Day Course
# Lab 10, ROT13
# Scott Cormack
# Python 3.9.6

def rot(encode, key):
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
     'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    result = []
    final_str = ''
    for i in encode:
        index = alpha.index(i)
        new_index = (index + 13) % 26
        new_char = alpha[new_index]
        result.append(new_char)
    for i in result:
        final_str += i
    return final_str


usr_ipt = input('Enter a word to encode: ')
usr_key = int(input('Enter a key to encode your message: '))
print('Your encoded message is')
print(rot(usr_ipt, usr_key))

