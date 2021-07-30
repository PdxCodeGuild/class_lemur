# # Exercise 1
# teachers = [
#     {
#         'name': 'Pete',
#         'city': 'Portland',
#         'job': 'programmer',
#         'computer': 'Mac',
#     },
# 	{
# 		'name': 'Lisa',
# 		'city': 'Portland',
# 		'job': 'programmer',
# 		'computer': 'windows',
# 		'cat': 'Heather'
# 	}
# ]
# keys = ['name', 'city', 'job', 'computer', 'cat']
# for teacher in teachers:
# 	print()
# 	try:
# 		for key in keys:
# 			print(f'Their {key} is {teacher[key]}')
# 	except KeyError:
# 		print(f'They have no {key}')


# Exercise 2
def add(x, y):
    return int(x) + int(y)

test_inputs = [
    (2, 2),
    ('2', '2'),
    (2, '2'),
    ('two', 2),
]

for nums in test_inputs:
	try:
		result = add(nums[0], nums[1])
		print(result)
	except TypeError:
		print(f"cannot add {nums[0]} {type(nums[0])} and {nums[1]} {type(nums[1])}")
	except ValueError:
		print(f"Cannot convert {nums[0]} {type(nums[0])} or {nums[1]} {type(nums[1])}")