import string

def get_user_input():
    user_string = input("Enter a string to encrypt: ")
    user_string = user_string.replace(" ", "").lower()
    while True:
        try:
            user_rotation = abs(int(input("Enter rotation value number: ")))
        except ValueError:
            print("You did not enter a valid number.")
            continue
        else:
            break
    if user_rotation > 26:
        user_rotation %= 26
        print(user_rotation)
    return user_string, user_rotation

def create_alphabet_dict():
    alphabet_dict = {}
    alphabet_list = list(string.ascii_lowercase)
    for i, letter  in enumerate(alphabet_list):
        alphabet_dict[letter] = i + 1
    return alphabet_dict

def number_key_alphabet_dict(alphabet_dict):
    new_dict = {}
    for k,v in alphabet_dict.items():
        new_dict[v] = k
    return new_dict


def ROT13(input_string, alphabet_dict, number_dict, rot_number=13):
    input_string_list = list(input_string)
    new_list = []
    for letter in input_string_list:
        num = alphabet_dict[letter]
        new_num = num + rot_number
        if new_num > 26:
            new_list.append(number_dict[new_num-26])
        else:
            new_list.append(number_dict[new_num])
    coded_string = "".join(new_list)
    return coded_string

def main():
    user_string, user_rotation = get_user_input()
    alphabet_dict = create_alphabet_dict()
    number_dict = number_key_alphabet_dict(alphabet_dict)
    print(ROT13(user_string, alphabet_dict, number_dict, user_rotation))

main()