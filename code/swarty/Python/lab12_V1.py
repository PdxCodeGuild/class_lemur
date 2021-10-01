"""
Lab12 - Contact List - David Swartwood 

Let's build a program to manage a list of contacts. To start, we'll build a CSV ('comma separated values') together, 
and go over how to load that file. Headers might consist of name, favorite fruit, favorite color. Open the CSV, 
convert the lines of text into a list of dictionaries, one dictionary for each user. The text in the header represents 
the keys, the text in the other lines represent the values.





"""
#import modules
#from datetime import datetime


file='../../code/swarty/DavidsData.csv'
#Read current file

with open(file, 'r') as file:
    lines=file.read().split('\n')
    #categories=lines.pop(0)
data=[]
database=[]
for line in lines:
    line=line.split(',')
    data.append(line)
for i in range(1,len(data)):
    item={}    #new object with new ID
    for j in range(len(data[i])):
        category_name=data[0][j]
        category_data=data[i][j]
        category_name=category_name.strip()
        category_data=category_data.strip()
        item.update({category_name:category_data})  
    database.append(item)

for datapoint in database:
    print(datapoint)
#Write to file
# with open(updated, 'w') as file:
#     file.write('\nHyundai, mid market, small cars and SUVs, South Korea, Hyundai Motor Company'.join(line))