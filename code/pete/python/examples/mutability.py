"""Strings, Integers & Floats are Immutable"""

x = 10
print(id(x))
x += 5
# x = x + 5
print(id(x))

"""Dictionaries & Lists are Mutable"""

nums = [1, 2, 3]
print(nums)
print(id(nums))
nums.append(4)
print(nums)
print(id(nums))

x = ['apples', 'bananas', 'pears']
y = x
# y = x.copy()
y.append('cherries')
print(x, id(x))  # ['apples', 'bananas', 'pears', 'cherries']
print(y, id(y))  # ['apples', 'bananas', 'pears', 'cherries']
