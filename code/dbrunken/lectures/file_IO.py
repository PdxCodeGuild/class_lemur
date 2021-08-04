'''
file (input, output)
class_lemur
'''

# with open('filename.txt', 'r') as f:
    # contents = f.read()

'''
import this as that
import an object from a library as a variable name
'''
from time import sleep

with open('fire-and-ice.txt', 'r') as f:
    # print(f, type(f)) 
    poem = f.read()
print(type(poem)) #<class 'str'>
lines = f.readlines()
while '' in lines:
    lines.remove('')
print(lines)

for line in lines:
    sleep(1)
    print()
    print(line)
    print()
    sleep(1)

