def credit_card_validation(card_num_string):
    reversed_as_int = []
    card_num_list = list(card_num_string)
    check_digit = card_num_list.pop()
    reversed_card_num = card_num_list[::-1]
    #reversed_card_num = card_num_list
    for num in reversed_card_num:
        reversed_as_int.append(int(num))
    for i in range(0, len(reversed_as_int), 2):
        reversed_as_int[i] *= 2
        if reversed_as_int[i] > 9:
            reversed_as_int[i] -= 9
    sum_of_list = sum(reversed_as_int)
    sum_of_list = str(sum_of_list)
    second_digit_of_sum = sum_of_list[1]
    if second_digit_of_sum == check_digit:
        print("Valid!")
    else: 
        print("NOT Valid!")
    
        

credit_card_validation("4556737586899855")