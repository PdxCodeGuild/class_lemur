tens = ['ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
ones = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens = ['ten','eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
hundreds = ['one-hundred', 'two-hundred', 'three-hundred', 'four-hundred', 'five-hundred', 'six-hundred', 'seven-hundred', 'eight-hundred', 'nine-hundred']
num = int(input("Enter a number: "))

tens_place = num %100 // 10
ones_place = num % 10
hun_place = num // 100
teens_place = num % 10

if hun_place != 0 and ones_place != 0 and tens_place != 0: #huns place, tens place, ones place
    if tens_place == 1:
        print(hundreds[hun_place -1] +'-' + teens[teens_place]) #huns, teens
    else:
        print(f"{hundreds[hun_place - 1]} - {ones[ones_place - 1]}") #huns, ones

elif hun_place !=0 and tens_place == 0:#huns, teens
     print(f"{hundreds[hun_place - 1]} - {ones[ones_place - 1]}")

elif hun_place == 0 and tens_place !=1 and tens_place != 0: #tens 20 +
    print(f"{tens[tens_place - 1]} - {ones[ones_place - 1]}")


elif hun_place !=0 and ones_place == 0 and tens_place == 0: #only hundreds
    print(hundreds[hun_place])

elif hun_place == 0 and tens_place == 0: # only ones
    print(ones[ones_place - 1])
elif tens_place == 1 and hun_place == 0: #tens only
    # if tens_place > 1:
    #     print(tens[tens_place])
    # elif tens_place == 1:
        print(teens[teens_place])
else:
    num = num - (hun_place * 100) 
    tens_place = num // 10
    ones_place = num % 10
    print(hun_place, tens_place, ones_place)
    #if statement for 0 huns place
    print(f"{hundreds[hun_place - 1]} - {tens[tens_place - 1]} - {ones[ones_place - 1]}")

   