file_path = 'code/pete/review/data/abc.csv'

# 1. Open the file
file_path = 'abc.csv'
with open(file_path, 'r') as file:
    letters = file.read()
    
# 2. Print out its contents
    # print(letters)

# 3. Turn it into a list
# letters = list(letters)
letters.split(',')
# print(letters) #listed letters but also commas

# 4. Sort the list
letters.sort()
# print(letters)

# 5. Turn list into a string
letters = ','.join(letters)
# print(letters)

# 6. Write the sorted string back to the file
with open(file_path, 'w') as file:
    letters = file.write(letters) #write() needs one arguement

# 7. Do the same thing, but reversed: randomize the order of the file contents
with open(file_path2, 'r') as file:
    letters = file.read()
letters = letters.split(',')
# print(letters)

shuffle(letters)
print(letters)
