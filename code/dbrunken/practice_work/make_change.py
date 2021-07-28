'''
create monetary change
'''

quarter = 25
dime = 10
nickle = 5
penny = 100

'''
pass in total dollar amount from input
convert to pennies
record running sum
divide total by 25(quarters)
'''

def make_change(user_in, q, d, n, p):
    total_p = user_in * p #total pennies
    total_q = user_in / q
    floor_q = total_p // q #returned 0.0 because 1.27 cannot be divided by 25
    mod_q = total_p % q
    floor_d= total_p // d
    mod_d = total_p % d
    floor_n = total_p // n
    mod_n = total_p % n
    total_change = total_p, total_q, floor_q, mod_q, floor_d,mod_d, floor_n, mod_n
    return total_change


total = input('how much money would you like to make change out of? ')
total = float(total)

print(make_change(total, quarter, dime, nickle, penny))

# if total == 0:
#     print("i see no money")

# else:
#     print(total // quater)