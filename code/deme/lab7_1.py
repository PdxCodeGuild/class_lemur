# jackalope = 0
# age = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# jackalope += 2
# for jackalope in range(0, 1000):
#     for jackalope in age [4:9]:
#         jackalope += 2
#         for jackalope in age[10]:
#             jackalope -= 1

# print(jackalope)
current = 0
years = 0
jackalopes = [0,0]
while len(jackalopes) < 1000:
    for i in range(len(jackalopes)):
        jackalopes[i] += 1
    for jackalope in jackalopes:      
        if current >= 4 and current <= 8:
    print(jackalopes)

# jackelopes = [0,0]
# for i in range(10):
#     if i >= 4 or i <= 8:
#         i += 1
#         jackelopes.append(0)
#         jackelopes.append(0)
#     if i == 10:
#         jackelopes.remove(i)
#         print(jackelopes)

#     for jackelopes[i] in jackelopes:
#         jackelopes[i] += 1
# print(jackelopes)

#git checkout -b mob_jack_megan_demetric
#git push
#git push --set-upstream origin main mob_jack_megan_demetric