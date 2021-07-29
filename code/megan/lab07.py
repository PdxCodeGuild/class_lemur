jackalopes = [0, 0]

age = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
years = 0


while len(jackalopes) < 1000:

    years += 1

    for i in range(len(jackalopes)):
        jackalopes[i] +=1  

    for jackalope in jackalopes:
        if jackalope >=4 and jackalope <= 8:
            jackalopes.append(0)

    for jackalope in jackalopes:
        if jackalope == 10:
            jackalopes.remove(jackalope)


            

print(len(jackalopes))
print(years)

       
# 2 jackalopes age 0 
# create 2 babies starting at age 4
# once a year, they'll create 2 babies
# each pair creates 2 babies at age 4 
# loop through jackalopes list and see if anybody is between the ages of 4 and 8
# if they're at the age of 10, remove them from the list 
# if two jackalopes are of breeding age, they'll create 2 jackalopes
# they'll age up by one year
# anybody not of breeding age will only age up 