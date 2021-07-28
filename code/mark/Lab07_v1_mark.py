def credit_card_validation(card_num_string):
    card_num_list = list(card_num_string)
    check_digit = card_num_list.pop()
    reversed_card_num = card_num_list[::-1]
    print(reversed_card_num)
    for num in reversed_card_num:
        num = int(num)
    print(reversed_card_num)
    for i in range(0, len(reversed_card_num), 2):
        reversed_card_num[i] *= 2
        if reversed_card_num[i] > 9:
            reversed_card_num[i] -= 9
    print(reversed_card_num)
    sum_of_list = sum(reversed_card_num)
    print(sum_of_list)
    second_digit_of_sum = sum_of_list[1]
    if second_digit_of_sum == check_digit:
        print("Valid!")
    else: 
        print("NOT Valid!")
    
        

credit_card_validation("123456789")