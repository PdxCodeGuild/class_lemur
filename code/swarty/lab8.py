"""
Lab 7 David Swartwood
Let's write a function which returns whether a string containing a credit card number is valid as a boolean. The steps are as follows:

Convert the input string into a list of ints
Slice off the last digit. That is the check digit.
Reverse the digits.
Double every other element in the reversed list.
Subtract nine from numbers over nine.
Sum all values.
Take the second digit of that sum.
If that matches the check digit, the whole card number is valid.
"""



cc=input("Enter your Credit Card #: ")
#cc=("4556737586899855")
if len(cc) != 16:
    cc=input("Incorrect entry \nEnter your Credit Card #: ")
cc=list(cc)
ccintegers=[int(num) for num in cc]
cccheck=ccintegers.pop()
ccintegers.reverse()
for i in range(len(ccintegers)):
    if i%2 ==0:
        ccintegers[i]+=ccintegers[i]
ccsum=0
for num in ccintegers:
    if num>9:
        num-=9
    ccsum+=num
if ccsum%10 == cccheck:
    print("CC number is valid")
else:
    print("card not valid")