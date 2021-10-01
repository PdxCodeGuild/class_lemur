from time import sleep
from colorama import Fore, Back, Style

with open('books/fire-and-ice.txt', 'r') as f:
    # print(f) # <_io.TextIOWrapper name='fire-and-ice.txt' mode='r' encoding='UTF-8'>
    poem = f.read()
# print(type(poem)) # <class 'str'>
lines = poem.split('\n')
while '' in lines:
    lines.remove('')
# print(lines)

fire = Fore.YELLOW + Back.RED + Style.BRIGHT
ice = Fore.WHITE + Back.BLUE + Style.BRIGHT

for line in lines:
    style = fire if 'ire' in line else ice
    sleep(1)
    print(Style.RESET_ALL + '\n')
    print(style + line, end='')
    print(Style.RESET_ALL + '\n')
    sleep(1)

# with open('books/around-the-world-in-80-days.txt', 'r') as f:
#     contents = f.read()

# print(contents)