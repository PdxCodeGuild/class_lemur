with open('lab12.csv', 'r') as file:
    lines = file.read().split('\n')
    # lines = file.read().split
    # print(lines)
# for line in lines:
# print(line)
# lines = lines.split(',')
# for line in lines:
#     print(line)
# for word in range(len(lines)):
#     print(word)

contacts = [] #create list for dictionary
for line in lines:
    for words in line:
        words = line.split(",")
        for word in words:
            word = line.split(",")
    contacts.append(word) 
headers = contacts[0]
# print(headers)

con_list = []

for values in contacts[1::]:
    con = {}
    for i in range(len(values)):
        con[headers[i]] = values[i] 
    con_list.append(con)
print(con_list)

repl = input("Do you want to create(C), retrieve(R), update(U), or delete(d) a record?")
def record(repl):
    con_list1 = con_list
    if repl == "C":
        new_name = input("Enter name: ")
        new_fruit = input("Enter fruit: ")
        new_color = input("Enter color: ")
        new_info = [new_name, new_fruit, new_color]
        new_info_dic = {}
        for i in range(len(new_info)):
            new_info_dic[headers[i]] = new_info[i] 
        # for values in new_info:
            # print(values)
            # print(new_info_dic)
            # for i in range(len(values)):
            #     new_info_dic[headers[i]] = values[i]
            # print(new_info_dic, values)
        con_list1.append(new_info_dic)
        print(con_list1)
    
    if repl == "R":
        retrieve_name = input("Enter name: ")
        for dictionary in con_list1:
            if retrieve_name == dictionary['name']:
                print(dictionary)

    if repl == "U":
        update_name = input("Enter name: ")
        for dictionary in con_list1:
            if update_name == dictionary['name']:
                print(dictionary)
                new_attribute = input("Which attribute would you like to update? ")
                # for dictionary in con_list1:
                #     if new_attribute == dictionary[new_attribute]:
                #         print(dictionary, "u")
        
    
    if repl == "D":
        delete_name = input("Enter a name: ")
        print(con_list1)
        for value in con_list1:
            print(value)
            if delete_name in value:
                con_list1.remove(value)
            print(con_list1)

record(repl)







# name, cuisine, country weather -----kets, loop over keys/lines to make new dictionaries
# split by calma

# have categories into dictionary by ket value pair
# cities = [
#     {'name: 'Portland' , 'cuisine': 'chicken}

# version 2
# while loop for input, append or create dictionary

# version 3
# turn list of dictionaries back into a properly formated .csv
# write to file
# //variable = book file
# variable = new file
# with open(1st variavle, 'r', encoding .. )

# with open(new variable,w, encoding...)
#     f.write(new variable)
#      """
# lab12 = "lab12.csv"
# lab12_new = "lab12_new.csv"
# with open(lab12, 'w') as lab12_new:
#     f.write(lab12_new)

