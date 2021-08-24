credit_card_number = '4556737586899855'


def credit_card_valid(credit_card_number):
    card_num_list = list(credit_card_number)

    i = 0
    while i < len(card_num_list):
        card_num_list[i] = int(card_num_list[i])
        i += 1

    check_digit = card_num_list.pop(-1)

    card_num_list.reverse()

    j = 0
    while j < len(card_num_list):
        card_num_list[j] = card_num_list[j] * 2
        if card_num_list[j] > 9:
            card_num_list[j] = card_num_list[j] - 9
        j += 2

    sum_of_nums = 0

    for num in card_num_list:
        sum_of_nums += num

    if sum_of_nums % 10 == check_digit:
        print("Valid")
    else:
        print("Invalid")


credit_card_valid(credit_card_number)
