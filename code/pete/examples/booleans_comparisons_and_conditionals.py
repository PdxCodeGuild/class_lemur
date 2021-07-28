"""Booleans"""
# and
print(True and True and True) # True
print(True and False and True) # False

w = 6
x = 5
y = 5
z = 6

print(x == y and w == z) # True
print(x == y and w == z and y == z) # False

# or
print(True or True or True) # True
print(False or False or False or False or False or False or False or False or False or False or False or False or False or False or False or False or False or False or False or False or False or False or False or False or False or False or False or False or False or False or True) # True
print(False or False or False or False) # False

print(x == y or w == z) # True
print(x == y or w == z or y == z) # True
print(w == x or y == z) # False

# not
print(not True) # False
print(not False) # True

print(not x == y) # False
print(not x == z) # True

"""Comparisons"""
# == equals
# != not-equals
# < less-than
# <= less-than-or-equal-to
# > greater-than
# >= greater-than-or-equal-to

x = 1
y = 2
z = 3

# shorthands
print(x < y < z)
print(x < y and y < z)

print(5 == 5== 5) # True
print((5 == 5) == 5) # False
print(True == 5) # False

# in
trees = ['oak', 'maple', 'fir']
print('oak' in trees) # True
print('spruce' in trees) # False

print('oak' not in trees) # False
print('spruce' not in trees) # True

# is
x = []
y = []
print(x is y) # False
print(x == y) # True
print(id(x), id(y))

z = x
print(z is x) # True
print(id(x), id(z))

test = {'a': 1, 'b': 2, 'c': 3, 'f': 6, 'g': 7}
keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# for key in keys:
# 	value = test.get(key)
# 	if value is not None:
# 		print(f'The value for {key} is {value}')
# 	else:
# 		print(f'No value for key {key} ')

"""Conditionals"""

temperature = int(input("what's the temp? "))

if temperature < 60:
    print('cold')
elif temperature >= 60 and temperature < 70:
    print('warm')

 # can be re-written as...

if temperature < 60:
    print('cold')
elif temperature < 70:
    print('warm')

if temperature < 60:
    print('cold')
elif temperature < 70:
    print('warm')
elif temperature < 80:
    print('pretty warm')
elif temperature < 90:
    print('hot')
else:
    print("wow it's so hot!")

"""Short-Circuited Evaluation"""

# False on the first False
print(True and False and True and True and True) # False
# True on the first True
print(False or True or True or False or True or False) # True

"""Shorthand"""

x = 5
y = 7
print("yup") if y > x else print("nope") # yup

x = 7
y = 5
print("yup") if y > x else print("nope") # nope

if y > x:
	print("yup")
else:
	print("nope")

"""Truthy & Falsey"""
# Everything is Truthy except...
# '', [], {}, False, 0, 0.0 are Falsey


if 'banana':
	print('taco')
if '':
	print('taco')

if 1:
	print('number 1')
if 0:
	print('number 0')

if ['stuff in the list']:
	print("there's stuff in it")
if []:
	print('theres no stuff')
if [0]:
	print('something in it')

go_outside_bool = True # or False
if go_outside_bool:
	print('time to go outside')
else:
	print('time to stay inside')

# Be careful with Truth/Falsey
# this example won't print out the 0 for 'c'
test = {'a': 1, 'b': 2, 'c': 0}
keys = ['a', 'b', 'c', 'd', 'e']
for key in keys:
	# if test.get(key) is not None: # safer conditional
	if test.get(key):
		print(test.get(key))
