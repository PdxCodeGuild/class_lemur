"""for loops"""

# nums = [1, 2, 3]
# for num in nums:
# 	print(num)

# message = 'welcome to class lemur'
# for char in message:
# 	print(char)

# # looping over a dictionary gives you the keys
# instructor = { 'name': 'pete', 'city': 'portland', 'hobby': 'hiking' }
# for key in instructor:
# 	print(key)

# for i in range(100):
# 	print(i)

# for i in range(50, 100):
# 	print(i)

# print(range(10), type(range(10)))
# print(list(range(10)), type(list(range(10))))

"""while loops"""

# while True:
# 	print('hey')

# counter = 1

# while counter < 10:
# 	print(counter)
# 	counter += 1

stop_words = ['done', 'no', 'n', 'nah']
user_command = ''
while user_command not in stop_words:
    user_command = input(
        'have a nice day(hear message again, or type no to stop) ')

while True:
    user_command = input(
        'have a nice day(hear message again, or type no to stop) ')
    if user_command in stop_words:
        break
print('program done')

while True:
    user_command = input(
        'have a nice day(hear message again, or type no to stop) ')
    if user_command not in stop_words:
        continue
    break
print('program done')
