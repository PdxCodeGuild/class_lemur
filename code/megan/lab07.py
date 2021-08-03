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