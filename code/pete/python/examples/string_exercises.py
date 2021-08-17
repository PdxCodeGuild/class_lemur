"""
ESCAPE SEQUENCES
"""
# \n newline
# \t tab
# using the backslash \ "escapes" the following characters
print('\nhello\t\tmore stuff\n')

# \" to include quotes w/o ending the string
print("\"I like Python,\" said the programming student.")

# double backslash \\ to print just one backslash
print("This is a backslash: \\")

print('\u3956')
print('\u6212')
print('\u0765')
print('\ub39d')
print('\u05ff')

print(0xdeadbeef)
# hexadcimal
"0123456789abcdef"
# binary

# 4 2 1

# 0 0 0 = 0
# 0 0 1 = 1
# 0 1 0 = 2
# 1 0 1 = 5

"""
RAW STRINGS
"""
print(r"\n \u0987 \t")
print('\u0987', r'\u0987')


"""
ASCII CODES
"""

print(ord('a')) # 97
print(chr(97)) # a

print(chr(98)) # b
print(chr(97 + 26))

# for i in range(200):
#     print(chr(i))

# for i in range(0x10fff):
#     print(chr(i))


"""
CONCATENATION + *
"""

print('hello' + ' ' + 'goodbye')

message = 'hello'
message += ' '
message += 'goodbye'
print(message)

print('-' * 80)
print('This is important and I want to see it')
print('-' * 80)

# print(message - 'goodbye') # TypeError: unsupported operand type(s) for -: 'str' and 'str'
# print('hello' / 'goodbye') # TypeError: unsupported operand type(s) for /: 'str' and 'str'

"""STRIP"""
from string import punctuation
extra_padding = '       hey        '
print(extra_padding.strip())
ninety = 'ninety-'
print(ninety.strip('-'))
print('@($)@%(this is the actual text here!)&@^')
print(punctuation)
print('@($)@%(this is the actual text here!)&@^'.strip(punctuation))
print('@($)@%(this! is! the! actual! text! here!)&@^'.strip(punctuation))

"""SPLIT"""
test = 'it\'s nice outside today, isn\'t it?'
print(test)
print(test.split('s'))
sentence = 'Python is fun to learn'
words = sentence.split()
print(words)

"""JOIN"""
print(' '.join(words))

letters = 'a b c d e'
print(letters)
letters_list = letters.split(' ')
print(letters_list)
print(' '.join(letters_list))