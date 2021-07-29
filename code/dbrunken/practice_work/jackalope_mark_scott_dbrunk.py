'''
create a jackalope population
Scott Cormack
Mark Dziuban
David Brunken
'''
import random
from string import ascii_letters

#set variables for population, years, population goal, death age

year = 0
# population = [0,0] #age 0 jacks
jack_age = 0
breed_age = [4, 8]
death_age = 10
# spawn =
pop_goal = 1000 #population goal


def jack_creation():
    jack_dict = { }
    list_letters = list(ascii_letters)
    jack_dict['name'] = random.choice(list_letters)
    jack_dict['age'] = 0
    jack_dict['sex'] = random.choice(['m','f'])
    jack_dict['pregnant'] = False
    return jack_dict

def jack_pop(population, year):
    while len(population) < pop_goal:
        num_of_breeders = 0
        baby_jacks = 0
        
        while death_age in population:
            population.remove(death_age)
        

        for jack in population:
            if jack <= breed_age[1] and jack >= breed_age[0]:
                num_of_breeders += 1

        baby_jacks = num_of_breeders // 2 * 2
        for i in range(baby_jacks):
            population.append(0)
            i += 1
        
        year += 1

        for i in range(len(population)):
            population[i] += 1
            
        
        #print(f"Number of years: {year} with a population of {population}")


    print(f"Number of years: {year} with a population of {len(population)}")

def add_pop(population, num_to_add):
    for i in range(num_to_add):
        population.append(jack_creation())
    return population


def main():
    population = []
    population = add_pop(population, 2)

jack_pop(population,year)
