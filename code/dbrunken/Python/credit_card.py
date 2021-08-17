'''
8/11
dbrunken
validate credit card numbers
'''

user_card = input('INPUT NUMBERS ON CARD: ')
# print(user_card)
credit_card = []

for num in user_card:
    credit_card.append(int(num))
# print(credit_card)

check_digit = []
check_digit = credit_card.pop(-1)
print(check_digit)


credit_card.reverse()
# print(credit_card)

#-------PsuedoCode-------#
'''
for the numbers in the credit card list:
    # find the even index in the list
    if index % 2 == even:
        # double number
        number * 2
    # otherwise do nothing
'''

for i, num in enumerate(credit_card):
    if i % 2 == 0:
        credit_card[i] = num * 2
        # if num > 9:
        #     num - 9
    
# print(credit_card)
    
for i, num in enumerate(credit_card):
    # print(num)
    if num > 9:
        credit_card[i] = num - 9
# print(credit_card)

# for i, num in enumerate(credit_card):
added_numbers = sum(credit_card)
print(added_numbers)

'''
floor divide to get single digit
check remainder digit with .pop()
print true or false
'''

check_num = added_numbers % 10
print(check_num)

if check_num == check_digit:
    print('Valid')
else:
    print('Invalid')