class Dog:

    def __init__(self, name):
        self.name = name

    def speak(self):
        return 'Woof!'


class Cat:

    def __init__(self, name):
        self.name = name

    def speak(self):
        return 'Mjau!'


def get_pet(pet='dog'):
    """ Factory method to create object"""
    pets = dict(dog=Dog(name='Hope'),
                cat=Cat(name='Peace'))

    return pets[pet]


d = get_pet('dog')
c = get_pet('cat')

print(d.speak())
print(c.speak())
