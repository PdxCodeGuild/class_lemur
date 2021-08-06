from random import random
from time import sleep

# python uses snake_case
# javascirpt uses camelCase
# html uses kebab-case
# classes are in PascalCase

class Cat:
    """Class representing a cat"""
    def __init__(self, name, color, lives=9): # the init method runs when you first create an object –– instantiation
        """cat init method"""
        self.name = name # these are attributes
        self.color = color # they are like key/value pairs in a dictionary
        self.lives = lives # they can be accessed and updated via dot notation
    
    def meow(self):
        print('meow')
    
    def jump(self):
        if random() > 0.25:
            print(f'{self.name} jumped successfully')
        else:
            self.lives -= 1
            print(f'{self.name} didn\'t jump so well...  {self.lives} lives remaining')
    
    def weather_forecast(self, temperature):
        self.meow()
        print(f"the current temperature is {temperature} degrees")
        self.meow()
    
    def __str__(self):
        return self.name

# print(__name__)

if __name__ == '__main__':

    garfield = Cat('Garfield', 'orange') # garfield is instantiated, he's an instance of the Cat class

    print(garfield.name, garfield.color, garfield.lives) # these are attributes of this cat object
    garfield.meow() # this is a method, it just prints 'meow'
    garfield.jump() # this is method has the cat jump with some random chance thrown in
    garfield.weather_forecast(65) # this method calls another method and prints out a message using the argument

    print()

    nermal = Cat('Nermal', 'gray', 10)

    print(nermal.name, nermal.color, nermal.lives) # these are attributes of this cat object
    nermal.meow() # this is a method, it just prints 'meow'
    nermal.jump() # this is method has the cat jump with some random chance thrown in
    nermal.weather_forecast(72) # this method calls another method and prints out a message using the argument


    # garfield.weather_forecast(90)

    # print(garfield.color)
    # garfield.color = 'orange and black'
    # print(garfield.color)

    # print(garfield)
    # print(garfield.name)
    # print(garfield.color)

    # heathcliff = {
    #     'name': 'Heathcliff',
    #     'color': 'orange',
    #     'lives': 9
    # }
    # print(heathcliff['name'])
    # print(heathcliff['color'])

    # garfield.meow()

    # for _ in range(15):
    #     garfield.jump()
    #     sleep(1.5)


    # def meow():
    #     print('meow')
    # meow()