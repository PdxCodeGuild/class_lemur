# tens = {
#     2 : 'twenty-',
#     3 : 'thirty-',
#     4 : 'forty'
# }
# ones = {
#     1 : 'one',
#     2 : 'two',
#     3 : 'three'
#     }
tens = ['ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
ones = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens = ['ten','eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
hundreds = ['one-hundred', 'two-hundred', 'three-hundred', 'four-hundred', 'five-hundred', 'six-hundred', 'seven-hundred', 'eight-hundred', 'nine-hundred']
num = int(input("Enter a number: "))
# num = num - 1
print(num, "checking num")
if num // 100 != 0:
    num_hun = (num // 100) - 1
    print(num_hun, "checking num_hum")
    print(hundreds[num_hun])
    #find tens
    if num % 100 >= 10:
        num_teens = num % 10
        print(hundreds[num_hun] + "-" + teens[num_teens])
        print("hundreds and teens")
    elif num // 100 != 0 and num % 10 > 0 and num // 10 == 10:
        num_ones = (num % 10) 
        print(hundreds[num_hun] + "-" + ones[num_ones])
        print("hundreds and ones")
    elif (num % 100) // 10 != 0:
        num_tens = (num % 100 // 10) -1
        print(hundreds[num_hun] + "-" + tens[num_tens])
        print("hundreds and tens")
    elif num % 10 == 0:
        num_tens = (num % 100 // 10) -1
        print(hundreds[num_hun] + "-" + tens[num_tens])
        print("no ones")
    else:  
        num_ones = (num % 10) - 1
        num_tens = (num % 100 // 10) -1
        print(hundreds[num_hun] + "-" + tens[num_tens] + "-" + ones[num_ones])
        print("hundreds, tens, ones")
elif num % 10 == 0:
    num_tens = (num % 100 // 10) -1
    print(tens[num_tens])
    print("tens")
elif num // 10 == 1:
    num_teens = num % 10
    print(teens[num_teens])
    print("teens")
else:  
    num_ones = (num % 10) - 1
    print(ones[num_ones])
    print("ones")

# tenss = tens[num]
# print(tenss)
# print(23 // 10)
# oness = (ones[num[1]])
# print(tenss + "-" + oness)

# if num // 10 != 0 or num // 100 != 0:
#     num_hun = num // 100
#     print(hundreds[num_hun])
#     num_tens = num // 10
#     print(tens[num_tens])
#     num_ones = num % 10
#     print(tens[num_tens] + "-" + ones[num_ones])