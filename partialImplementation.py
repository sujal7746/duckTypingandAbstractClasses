#base class with partial implementation, code reuse via __init__

class ThingToBuild():
    def __init__(self, name_of_thing = '[unknown]'):
        self.name_of_thing = name_of_thing

    def build(self):
        raise NotImplementedError('All subclasses have to implement this method')
    def visit(self):
        print('This thing cannot be visited')

class Cathedral(ThingToBuild):  #subclass inherit
    def build(self):
        print('building the cathedral....')
    def visit(self):
        print('Welcome to {}'.format(self.name_of_thing))

class Cafe(ThingToBuild):
    def build(self):
        print('building a cafe......')
    def visit(self):
        print('Welcome to {}'.format(self.name_of_thing))


class Car(ThingToBuild):
    def build(self):
        print('building a car......')

def create(building):
    building.build() #no more error for car object
    building.visit()

not_dame = Cathedral()
java_house = Cafe()
car = Car()

things = not_dame, java_house, car

for the_thing in (things):
    create(the_thing)
    print()