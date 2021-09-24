from random import random
from time import sleep

class Cat:
    def __init__(self, name, color, lives=9):
        self.name = name
        self.color = color
        self.lives = lives 

    def meow(self):
        print('meow')
    
    def jump(self):
        if random() > 0.25:
            print(f'{self.name} jumped successfully')
        else:
            self.lives -= 1
            print(f'{self.name} didn\'t make it. {self.lives} lives remaining.')
        
        def __str__(self):
            return self.name

print(__name__)

if __name__ == '__main__':

    garfield = Cat('Garfield', 'orange')

    print(garfield)
    print(garfield.name)
    print(garfield.color)

    garfield.meow()

    for _ in range(10):
        # sleep(0.5)
        garfield.jump()
