'''
create a jackalope population
Scott Cormack
Mark Dziuban
David Brunken
'''
import random
from string import ascii_letters


def jack_creation():
    name_list = []
    jack_dict = { }
    list_letters = list(ascii_letters)
    name_length = random.randint(4,9)
    for i in range(name_length):
        name_list.append(random.choice(list_letters))
    jack_dict['name'] = "".join(name_list)
    jack_dict['age'] = 0
    jack_dict['sex'] = random.choice(['m','f'])
    jack_dict['pregnant'] = False
    return jack_dict



def jack_pop(population, year, pop_goal):
    breed_age = [4, 8]
    death_age = 10
    
    while len(population) < pop_goal:
    #for i in range(20):
        num_of_breeders = 0
        baby_jacks = 0
        breeder_list = []
        random.shuffle(population)
        #for count,jack in enumerate(population):
        for i,jack in enumerate(population):
            if jack["age"] == death_age:
                print(f"{jack['name']} died :(")
                del jack
            elif jack["age"] <= breed_age[1] and jack["age"] >= breed_age[0] and jack["pregnant"] == False:
                jack["position"] = i
                breeder_list.append(population.pop(i))
                num_of_breeders += 1
                #print(f"Population after pop: {population}")
        if len(breeder_list) > 0:
            males_list, females_list = can_breed_list(breeder_list)
            population.extend(males_list)
            population.extend(females_list)
            print(population)
                #print(f"breeder list: {breeder_list}")


        baby_jacks = num_of_breeders // 2 * 2
        for i in range(baby_jacks):
            jack_made = jack_creation()
            #print(f"New Baby! {jack_made}")
            population.append(jack_made)
            i += 1

        for i in range(len(population)):
            age = population[i]["age"]
            population[i]["age"] = 1 + age
        year += 1
            
        
        i += 1
    #print(population)
    return year, len(population)

def can_breed_list(breeder_list):
    males_list = []
    male_position_list = []
    females_list = []
    females_position_list = []
    
    for breeder in breeder_list:
        if breeder['sex'] == "m":
            males_list.append(breeder)
        else:
            females_list.append(breeder)
    print(f"males: {males_list}, females: {females_list}")
    for male in males_list:
        male_position_list.append(male['position'])
    #print(f"Male positions: {male_position_list}")
    for female in females_list:
        females_position_list.append(female['position'])
    #print(f"Female positions: {females_position_list}")
    return males_list, females_list


    #print(position_list)

        
        

def add_pop(population, num_to_add):
    for i in range(num_to_add):
        population.append(jack_creation())
    return population


def main():
    pop_goal = 100
    year = 0
    inital_population = 2
    population = []
    population = add_pop(population, inital_population)
    years, pop_count = jack_pop(population,year, pop_goal)
    print(f"Years to 100: {years}, with population of: {pop_count}")

main()
