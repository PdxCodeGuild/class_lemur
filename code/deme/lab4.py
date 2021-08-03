tens = ['ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
ones = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens = ['ten','eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
hundreds = ['one-hundred', 'two-hundred', 'three-hundred', 'four-hundred', 'five-hundred', 'six-hundred', 'seven-hundred', 'eight-hundred', 'nine-hundred']
num = int(input("Enter a number: "))
# num = num - 1
# print(num, "checking num")
tens_place = num %100 // 10
ones_place = num % 10
hun_place = num // 100
teens_place = num % 10

if hun_place != 0 and ones_place != 0 and tens_place != 0: #huns place, tens place, ones place
    if tens_place == 1:
        print(hundreds[hun_place -1] +'-' + teens[tens_place], "a") 
    else:
        print(hun_place, tens_place, ones_place, "f")
        print(f"{hundreds[hun_place]} {tens[tens_place - 1]} - {ones[ones_place - 1]}")

elif hun_place !=0 and ones_place == 0 and tens_place == 0: #only hundreds
    print(hundreds[hun_place])

elif hun_place == 0 and tens_place == 0: # only ones
    print(ones[ones_place - 1])
elif tens_place == 1 and hun_place == 0:
    if tens_place > 1:
        print(tens[tens_place])
    elif tens_place == 1:
        print(teens[teens_place])
else:
    num = num - (hun_place * 100) 
    tens_place = num // 10
    ones_place = num % 10
    print(hun_place, tens_place, ones_place, "p")
    #if statement for 0 huns place
    print(f"{hundreds[hun_place - 1]} - {tens[tens_place - 1]} - {ones[ones_place - 1]}")

    # hun_place = num // 100
# if hun_place == 0:
#     tens_place = num // 10
#     ones_place = num % 10
#     print(tens_place, ones_place, "f")
#     print(f"{tens[tens_place - 1]} - {ones[ones_place - 1]}")

# else:
#     num = num - (hun_place * 100) 
#     tens_place = num // 10
#     ones_place = num % 10
#     print(hun_place, tens_place, ones_place, "p")
#     #if statement for 0 huns place
#     print(f"{hundreds[hun_place - 1]} - {tens[tens_place - 1]} - {ones[ones_place - 1]}")

# num_tens = (num % 100 // 10) -1
# num_hun = (num // 100) - 1
# num_ones = (num % 10) - 1
# num_teens = num % 10
# if num // 100 != 0:
    # num_hun = (num // 100) - 1
#     print(num_hun, "checking num_hum")
#     print(hundreds[num_hun], "checking hundreds")
#     #find tens
#     if num // 100 != 0 and num % 10 > 0:
#         num_ones = (num % 10) - 1
#         print(hundreds[num_hun] + "-" + ones[num_ones])
#     elif (num % 100) // 10 != 0:
#         # num_tens = (num % 100 // 10) -1
#         print(tens[num_tens])
#     elif num % 10 == 0:
#         print(hundreds[num_hun] + "-" + tens[num_tens])
#         print("no ones")
#     elif num % 100 >= 10:
#             num_teens = num % 100
#             print(hundreds[num_hun] + "-" + teens[num_teens])
#             print("hundreds and teens")
#     else:  
#             # num_ones = (num % 10) - 1
#             print(hundreds[num_hun] + "-" + tens[num_tens] + "-" + ones[num_ones])
#             print("hundreds, tens, ones")
# elif num % 10 == 0:
#     num_tens = (num % 100 // 10) -1
#     print(tens[num_tens])
#     print("tens")
# elif num // 10 == 1:
#     # num_teens = num % 10
#     print(teens[num_teens])
#     print("teens")
# else:  
#     num_ones = (num % 10) - 1
#     print(ones[num_ones])
#     print("ones")

# # tenss = tens[num]
# # print(tenss)
# # print(23 // 10)
# # oness = (ones[num[1]])
# # print(tenss + "-" + oness)

# # if num // 10 != 0 or num // 100 != 0:
# #     num_hun = num // 100
# #     print(hundreds[num_hun])
# #     num_tens = num // 10
# #     print(tens[num_tens])
# #     num_ones = num % 10
# #     print(tens[num_tens] + "-" + ones[num_ones])


# # tens = {
# #     2 : 'twenty-',
# #     3 : 'thirty-',
# #     4 : 'forty'
# # }
# # ones = {
# #     1 : 'one',
# #     2 : 'two',
# #     3 : 'three'
# #     }
# # tens = ['ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
# # ones = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
# # teens = ['ten','eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
# # hundreds = ['one-hundred', 'two-hundred', 'three-hundred', 'four-hundred', 'five-hundred', 'six-hundred', 'seven-hundred', 'eight-hundred', 'nine-hundred']
# # num = int(input("Enter a number: "))
# # # num = num - 1
# # print(num, "checking num")
# # if num // 100 != 0:
# #     num_hun = (num // 100) - 1
# #     print(num_hun, "checking num_hum")
# #     print(hundreds[num_hun])
# #     #find tens
# #     if num % 100 >= 10:
# #         num_teens = num % 10
# #         print(hundreds[num_hun] + "-" + teens[num_teens])
# #         print("hundreds and teens")
# #     elif num // 100 != 0 and num % 10 > 0 and num // 10 == 10:
# #         num_ones = (num % 10) 
# #         print(hundreds[num_hun] + "-" + ones[num_ones])
# #         print("hundreds and ones")
# #     elif (num % 100) // 10 != 0:
# #         num_tens = (num % 100 // 10) -1
# #         print(hundreds[num_hun] + "-" + tens[num_tens])
# #         print("hundreds and tens")
# #     elif num % 10 == 0:
# #         num_tens = (num % 100 // 10) -1
# #         print(hundreds[num_hun] + "-" + tens[num_tens])
# #         print("no ones")
# #     else:  
# #         num_ones = (num % 10) - 1
# #         num_tens = (num % 100 // 10) -1
# #         print(hundreds[num_hun] + "-" + tens[num_tens] + "-" + ones[num_ones])
# #         print("hundreds, tens, ones")
# # elif num % 10 == 0:
# #     num_tens = (num % 100 // 10) -1
# #     print(tens[num_tens])
# #     print("tens")
# # elif num // 10 == 1:
# #     num_teens = num % 10
# #     print(teens[num_teens])
# #     print("teens")
# # else:  
# #     num_ones = (num % 10) - 1
# #     print(ones[num_ones])
# #     print("ones")

# # # tenss = tens[num]
# # # print(tenss)
# # # print(23 // 10)
# # # oness = (ones[num[1]])
# # # print(tenss + "-" + oness)

# # # if num // 10 != 0 or num // 100 != 0:
# # #     num_hun = num // 100
# # #     print(hundreds[num_hun])
# # #     num_tens = num // 10
# # #     print(tens[num_tens])
# # #     num_ones = num % 10
# # #     print(tens[num_tens] + "-" + ones[num_ones])



