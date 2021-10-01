with open('lab12.csv', 'r') as file:
    lines = file.read().split('\n')

contacts = []  # create list for dictionary
for line in lines:
    # print(line, "line")
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
# print(con_list)

def record():
    con_list1 = con_list
    loop_control = True
    while loop_control == True:
        repl = input("Do you want to create(C), retrieve(R), update(U), or delete(D) a record or exit(E)?")

        if repl == "C":
            new_name = input("Enter name: ")
            new_fruit = input("Enter fruit: ")
            new_color = input("Enter color: ")
            new_info = [new_name, new_fruit, new_color]
            new_info_dic = {}
            for i in range(len(new_info)):
                new_info_dic[headers[i]] = new_info[i]
            con_list1.append(new_info_dic)
            print(con_list1)

        if repl == "R":
            retrieve_name = input("Enter name: ")
            for dictionary in con_list1:
                if retrieve_name == dictionary['name']:
                    print(dictionary)

        if repl == "U":
            update_name = input("Enter name: ")
            for dictionary in con_list1:  # for each dictionary in the list
                # if input(update_name) is a value for 'name' key in the dictionaries
                if update_name == dictionary['name']:
                    print(dictionary, "b")  # print dictionary with name value
                    new_attribute = input("Which attribute would you like to update? ")
                    for dictionary in con_list1:
                        if update_name == dictionary['name']:
                            print(dictionary[new_attribute])
                            updated_attribute = input("Enter new attribute")
                            dictionary[new_attribute] = updated_attribute
        # print(con_list1)

        if repl == "D":
            delete_name = input("Enter the name you would like to delete: ")
            # print(con_list1)
            for dictionary in con_list1:
                if delete_name == dictionary['name']:
                    con_list1.remove(dictionary)
            # print(con_list1)

        if repl == "E":
            with open("lab12.csv", "r") as f:
                contents = f.read()
                print(contents)
            output = ",".join(headers) 
            for dict in con_list1:
                row = []
                #output += "\n" + ",".join(dict.values())***********other way instead of below for loop
                for el in dict:
                    row.append(str(dict[el]))
                    
                output += "\n" + ",".join(row)
        

            with open("lab12.csv", "w") as f:
                f.write(output)
            loop_control = False
record()



