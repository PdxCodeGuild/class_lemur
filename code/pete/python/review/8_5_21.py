from random import shuffle

file_path = 'code/pete/review/data/abc.csv'
file_path2 = 'code/pete/review/data/abc2.csv'
file_path3 = 'code/pete/review/data/abc3.csv'

# 1. Open the file
with open(file_path, 'r') as file:
    letters = file.read()

# 2. Print out its contents
print(letters)

# 3. Turn it into a list
# letters = list(letters)
letters = letters.split(',')
print(letters)

# 4. Sort the list
letters.sort()
print(letters)

# 5. Turn list into a string
letters = ','.join(letters)
print(letters)

# 6. Write the sorted string back to the file
with open(file_path2, 'w') as file:
    file.write(letters)

print('\n\n')

# 7. Do the same thing, but reversed: randomize the order of the file contents

# open file
with open(file_path2, 'r') as file:
    letters = file.read()
print(letters)

# turn csv string into list
letters = letters.split(',')
print(letters)

# randomize order of list
shuffle(letters)
print(letters)

# join randomized list into csv-formated string
letters = ','.join(letters)
print(letters)

# write string to file
with open(file_path3, 'w') as file:
    file.write(letters)