import random 
import string

alphabet = string.ascii_letters 
digits = string.digits
punctuation = string.punctuation

all = alphabet + digits + punctuation

control = 0 
user_password = []


while control < 10:
    char = random.choice(all)
    total = user_password.append(char)
    final = ''.join(map(str, user_password))

    control += 1

print(f'Your password: {final}')