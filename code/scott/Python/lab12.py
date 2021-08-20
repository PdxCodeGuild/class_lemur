# Class Lemur Day Course
# Lab 12, CSV
# Scott Cormack
# Python 3.9.6
file_name = 'smite_characters.csv'

temp = []
complete = []

# Unpack the CSV and turn it into a working list of dictionaries
with open(file_name, 'r') as f:
    lines = f.read().split('\n')
for line in lines:
    temp.append(line.split(','))

for line in temp:
    

print(temp)
    
