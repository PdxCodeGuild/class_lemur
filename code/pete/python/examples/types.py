"""Types"""
# integers
print('\nintegers')
x = 4
y = 6
# z = x + y
print(x, type(x))
# print(z, type(z))
print(x + y, type(x + y))

# floats
print('\nfloats')
x = 1.43
y = 2
print(x, type(x))
print(x + y, type(x + y))

# floats are made of fractions of 1 / powers of 2
# 0.5 = 1 / 2
# 0.75 = 1 / 2 + 1 / 4

# strings
print('\nstrings')
x = 'hello'
y = ' world'
print(x, type(x))
print(x + y, type(x + y))

# TypeError
# x = '2'
# y = 4
# print(x, type(x))
# print(x + y, type(x + y))

# lists
print('\nlists')
x = [1, 2, 3]
y = ['a', 'b', 'c']
print(x, type(x))
print(x + y, type(x + y))

# dictionaries
print('\ndictionaries')
x = {'a': 1, 'b': 2}
# y = { 'c': 3 }
print(x, type(x))
# print(x.update(y), type(x.update(y)))

# booleans
print('\n')
x = True
y = False
print(x, type(x))
print(y, type(y))
