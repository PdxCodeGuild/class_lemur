'''
programming 102
unit 5 lab
Create a Login
'''

# from random import shuffle


profiles = [
    {
        'username': 'blank',
        'password': '1234321'
    },
    {
        'username': 'dave',
        'password': '10465'
    },
    {
        'username': 'micah',
        'password': '0987890'
    }
]

# print(profiles['username'] == 'blank')
# print(profiles['password'] == '1234321')

# print(profiles['username'] == 'blank', profiles['password'] == '1234321')

def login_base(name, word, dict):    
    if name != dict['username']:
        return False
    if word != dict['password']:
        return False
    else:
        return True

# log_attempts = 0
# close_out = log_attempts + 3

if __name__ == '__main__':

    while True: #close_out == 0:

        username = input('\nenter your username: ')
        password = input('\nwhats the password? ')

        # id = profiles['blank':{'id'}], profiles['dave':{'id'}], profiles['micah':{'id'}]
        # username = username.append(id)

        for user in profiles:
            check_input =  login_base(username, password, user)
            if check_input == True:
                break
        

        if check_input != True:
            try_again = input('would you like to try again? ')
            no = 'no'
            if try_again == no:
                print('goodbye')
                break

        # if close_out == 3:
        #     print('thats too many attempts')
        #     break


        elif check_input == True:
            print(f'welcome {username}')
            break
      
