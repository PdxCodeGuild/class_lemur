'''
create a jackalope population
Scott Cormack
Mark Dziuban
David Brunken
'''


#set variables for population, years, population goal, death age

year = 0
population = [0,0] #age 0 jacks
jack_age = 0
breed_age = [4, 9]
death_age = 10
# spawn =
pop_goal = 1000 #population goal



while len(population) < pop_goal:
    num_of_breeders = 0
    baby_jacks = 0

    while death_age in population:
        population.remove(death_age)
    

    for jack in population:
        if jack < breed_age[1] and jack > breed_age[0]:
            num_of_breeders += 1

    baby_jacks = num_of_breeders // 2 * 2
    for baby in baby_jacks:
        population.append(0)

# print(population)
