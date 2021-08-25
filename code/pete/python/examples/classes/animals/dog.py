class Dog:

    # variable defined here are `class attributes`
    # they are accessible to every object and
    # are shared amongst every instance
    species = 'dog'
    speak_dict = {
        'small': 'yip',
        'medium': 'bark',
        'large': 'woof'
    }
    
    # the __init__ is a special method that runs to instantiate
    # an object of the class 
    def __init__(self, name, breed, size):
        # these are all `instance attributes`
        # they are specific to each instance of the `Dog` class
        self.name = name
        self.breed = breed
        self.size = size
    
    # `speak` is a method of the dog class
    def speak(self):
        """dog will speak according to its size"""
        print(self.speak_dict[self.size])
        # if self.size == 'small':
        #     print('yip')
        # elif self.size == 'medium':
        #     print('bark')
        # elif self.size == 'large':
        #     print('woof')
        # # print('bark')
    
    # some other magic or dunder (double underscore) methods
    # include __eq__ for the `==` operator
    # this runs under the hood when you use that operator
    # self is this object (a Dog) and other is the object on the other
    # side of the `==` operator (hopefully, another Dog object)
    def __eq__(self, other):
        """method for == operator"""
        if type(other) != type(self):
            raise TypeError('both objects must be dogs!')
        if self.size == other.size: # using dog.size for == comparison
            return True
        return False

    # __gt__ is like __eq__, but for > or "is greater than"
    def __gt__(self, other):
        """method for > operator"""
        if type(other) != type(self):
            raise TypeError('both objects must be dogs!')
        if self.size == 'medium' and other.size == 'small':
            return True
        if self.size == 'large' and (other.size in ['small', 'medium']):
            return True
        return False

    # __lt__ is for the < operator: less than
    def __lt__(self, other):
        """method for < operator"""
        if type(other) != type(self):
            raise TypeError('both objects must be dogs!')
        if self.size == 'medium' and other.size == 'large':
            return True
        if self.size == 'small' and (other.size in ['large', 'medium']):
            return True
        return False
    

    # __str__ is a very common dunder method... if the object needs to be
    # included in a string, (printed, included in an f-string), the __str__
    # method will run and return a user-readable string representing the dog
    def __str__(self):
        return self.name

    
if __name__ == '__main__':
    kirby = Dog('Kirby', 'Havanese', 'small')
    # print(kirby)
    # print('the dog is ' + str(kirby))
    # print(f'the dog is {kirby}')
    # print('123' + str(4))
    # print(f'123{4}')

    kirby.speak()

    whiskey = Dog('Whiskey', 'Husky', 'medium')

    # print(whiskey)
    whiskey.speak()

    pax = Dog('Pax', 'Greyhound', 'large')
    pax.speak()
    # print(kirby.species, whiskey.species, pax.species)

    pax.speak_dict.update({'xl': 'WUF'})
    # print(pax.speak_dict)

    # print(kirby.speak_dict)

    # print(kirby + whiskey)
    # print(kirby.name, kirby.breed, kirby.size, kirby.species)

    kora = Dog('Kora', 'Husky', 'medium')

    print(kora == whiskey)
    
    print(pax > kora)
    print(kirby > whiskey)

    print(pax < kora)
    print(kirby < whiskey)

    print(kora < whiskey)
    print(kora > whiskey)

    # print(kirby == pax)
    # print(whiskey == kirby)
    # print(type(pax), type('this is a dog'))
    # print(pax == 'this is a dog, right?')
    