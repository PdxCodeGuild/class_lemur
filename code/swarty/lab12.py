"""
Lab12 - Contact List - David Swartwood 

Let's build a program to manage a list of contacts. To start, we'll build a CSV ('comma separated values') together, 
and go over how to load that file. Headers might consist of name, favorite fruit, favorite color. Open the CSV, 
convert the lines of text into a list of dictionaries, one dictionary for each user. The text in the header represents 
the keys, the text in the other lines represent the values.





"""
#import modules
from datetime import datetime


file='../../code/swarty/DavidsData.csv'
updated=f'../../code\swarty\DavidsData_{datetime.now().strftime("%b%d_%Y")}.csv'
#Read current file
lines={}
with open(file, 'r') as file:
    lines=file.read().split('\n')
    
print(lines)





#Write to file
# with open(updated, 'w') as file:
#     file.write('\nHyundai, mid market, small cars and SUVs, South Korea, Hyundai Motor Company'.join(line))
