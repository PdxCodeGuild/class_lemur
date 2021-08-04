"""
Lab12 - Contact LIst - David Swartwood 

Let's build a program to manage a list of contacts. To start, we'll build a CSV ('comma separated values') together, 
and go over how to load that file. Headers might consist of name, favorite fruit, favorite color. Open the CSV, 
convert the lines of text into a list of dictionaries, one dictionary for each user. The text in the header represents 
the keys, the text in the other lines represent the values.





"""

with open('DavidsData.csv', 'w') as file:
    lines = file.read().split('\n')
    print(lines)



