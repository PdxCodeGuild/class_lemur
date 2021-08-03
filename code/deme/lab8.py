def credit(user_input):
    #convert input string into a list of ints
    user_input = list(user_input)
    user_input = [int(num) for num in user_input]
    #slice off the last digit and make check digit
    check_digit = user_input.pop()

    #reverse the digits
    user_input.reverse()
    print("reverse",user_input)
   
    #double every other element in the reversed list and subtract 9 from number if number > 9
    for i in range(len(user_input)):
        if i % 2 == 0:
            num = user_input[i] * 2
            if num > 9:
                num = num - 9
            user_input[i] = num

    print(user_input)

    #sum all values
    total = 0
    for num in user_input:
        total += num
  
    print(total)
    #compare second digit of total with check digit
    if total % 10 == check_digit:
        print("Valid!")
    else:
        print("invalid")
card = input("Enter your credit card number: ")
credit(card)
