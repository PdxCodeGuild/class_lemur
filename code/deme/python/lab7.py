
age_list = [0,0]
years = 0
while len(age_list) < 1000:
    i = 0 
    for age in age_list: #reproduce jackelope in age range 4-8
        if age in range(4,9):
            age_list.append(0)
        print(len(age_list))
    i = 0
    for age in age_list: #subtract jackelopes at age 10   
        if age == 10:
            age_list.remove(age) 
            
    for age in age_list:        
        age_list[i] =age+1
        i += 1
    years += 1
print(years, len(age_list))