# Class Lemur Day Course
# Lab 12, ROT13
# Scott Cormack
# Python 3.9.6

# Open CSV and convert to a list of dictionaries
def convert_csv(file):
    with open('smite_characters.csv', 'r') as f:
        keys = f.readline().strip('\n').split(',')
        data = f.read().splitlines(False)
        complete = []
        for i in range(len(data)):
            data[i] = data[i].split(',')
        # Test calls
        print(keys, type(keys))
        print(data, type(data))
        print(complete, type(complete))
        f.close()

def unpack(*args):
    num = len(args)

       
convert_csv('smite_characters.csv')
