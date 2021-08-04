
def say_hello(first_name='Pete', last_name='Jones'):
    print('Hello ' + first_name + ' ' + last_name)

# fn = input('what is your first name? ')
# ln = input('what is your last name? ')
# say_hello(fn, ln)
# say_hello('pet', 'jones')
# say_hello()


def subtract(a, b, c):
    return a - b - c
# print(subtract(5, c=9, b=8)) # -12 (a=5, b=8, c=9)
# print(subtract(c=5, b=15, a=25))


"""
EXERCISE 1
Write an add function that returns the sum of two numbers
"""


def add(x, y):
    return x + y


print(add(1, 2))  # 3
print(add(3, 7))  # 10

"""
EXERCISE 2
Write a function that capitalizes the first letter of every word in a string
"""


def capitalize(message):
    return message.title()


print(capitalize('capitalize this message'))  # Capitalize This Message

test = 'here\'s a string'
print(test.capitalize())  # Here's a string

"""
EXERCISE 3
Write an add function that takes in *args and returns the sum of all numbers
"""


def add_plus(*nums):
    sum = 0
    for num in nums:
        sum += num
    return sum


print(add_plus(1, 2, 3, 4, 5, 6))  # 21

# args example


def args_example(*args):
    for arg in args:
        print(arg)

# args_example(1)
# print()
# args_example('hello', 4, 6.7)
# print()
# args_example(5, 2, 8,1,1,1,1,1,1,1,1,1,1,1,1,1,1)


"""returns"""


def weather_report(temperature):
    """from a given temperature (int) returns a string describing the weather"""
    if temperature < 60:
        return 'cold'
    if temperature < 70:
        return 'warm'
    if temperature < 80:
        return 'pretty warm'
    if temperature < 90:
        return 'hot'
    return "wow it's so hot!"


temperatures = [55, 65, 75, 85, 95]

# for temp in temperatures:
# 	print(temp, weather_report(temp))

"""Implicit Return"""


def gimme_none():
    print('this returns nothing!!')

# none = gimme_none()
# print(none)


def get_dimensions():
    return 500, 200


width, height = get_dimensions()
print(width)
print(height)

dimensions = get_dimensions()
print(dimensions)
print(dimensions[0], dimensions[1])

width, height = (500, 200)
print(width, height)


def crash_python(i=0):
    print(i)
    i += 1
    crash_python(i)
# crash_python()


def for_loop(i, sequence):
    print(sequence[i])
    i += 1
    if i == len(sequence):
        return
    for_loop(i, sequence)


colors = ['red', 'green', 'blue']
for_loop(0, colors)


def multiply(x, y): return x * y


def multiply(x, y):
    return x * y


print(multiply(2, 3))
