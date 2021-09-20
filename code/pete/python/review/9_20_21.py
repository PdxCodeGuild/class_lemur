import random

# strings
## declaration
first_name = 'pete'
## access
print(first_name[0])
last_name = 'jones'
## concatenation
full_name = first_name + ' ' + last_name
print(full_name)
## methods
print(full_name.title())
print(len(full_name))

# ints
## declaration
number = 8
## int()
number = int('8')
number = int(248.2)
## operations
## floor division
hundreds = number // 100
print(hundreds)
## modulus
ones = number % 10
print(ones)
tens = number % 100 // 10
print(tens)

# floats
## declaration
number = 8.852
print(round(number, 2))
# print(type(number))
# # print(9 / 4.4)


# dictionaries
## declaration
instructor = {
    'first_name': 'Pete',
    'last_name': 'Jones',
    'jobs': ['instructor', 'frontend dev'],
    'age': 34,
    # 'city': 'Portland'
}
## access
print(instructor['age'])
print(instructor.get('city'))
print(instructor.get('jobs'))
# print(instructor['city'])
## methods
print(instructor.keys()) # a list-like object of the dictionary's keys
print(instructor.values()) # a list-like object of the dictionary's values
print(instructor.items()) # a list-like object of tuples of the dicionary's key-value pairs


# booleans
## declaration
var1 = True
var2 = False
if var1:
    print('hello')

if not var1:
    print('goodbye')

if var1 and var2:
    print('and')

if var1 or var2:
    print('or')

print((var1 == var1) == (var2 == var2))

# lists
## declaration
nums = [1, 2, 3, 4, 5]
## access
print(nums[-1])
## loops
for num in nums:
    print(num)
for i in range(len(nums)):
    print(nums[i])

# tuples
## declaration
letters = ('a', 'b', 'c', 'd')
## tuples are immutable, you cannot append, like al ist, etc.

# sets
## declaration
names = {'pete', 'lisa', 'david', 'david'}
print(names)

nums = []
for i in range(100):
    nums.append(random.randint(1, 10))

print(list(set(nums)))