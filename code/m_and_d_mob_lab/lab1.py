"""
The goal is to calculate how many years it will take for two age 0 jackalopes to create a population of 1000.

Jackalopes are reproductive from ages 4-8 and die at age 10.
Gestation is instantaneous. Each gestation produces two offspring.
Jackalopes are hermaphrodites, it takes a pair to reproduce, but any pair will do
With these conditions in mind, we can represent our population as a list of ints.
"""
#h="hermafrodite"                           #V2
#population_list=[[h,0],[h,0]]              #V2
age_list=[0,0]
years=0
while len(age_list)<1000:
    i=0 
    for age in age_list:           #create new jackalope
        if age in range(4,9):
            age_list.append(0)
        print(len(age_list))
    i=0
    for age in age_list:                #time passes       
        if age ==10:
            age_list.remove(age)
    for age in age_list:        
        age_list[i]=age+1
        i+=1
    years+=1
print(years, len(age_list))