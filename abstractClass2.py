# abstract class/ interface, enforcing implementation inheriting subclasses

from duckTyping import not_dame, java_house, things


class ThingToBuild():
    def build(self):
        raise NotImplementedError('All subclasses have to implement this method')

    def visit(self):
        raise NotImplementedError('All subclasses have to implement this method')

class Cathedral(ThingToBuild):  #subclass inherit
    def build(self):
        print('build the cathedral....')
    def visit(self):
        print('welcome to our cathedral')

class Cafe(ThingToBuild):
    def build(self):
        print('building a cafe......')
    def visit(self):
        print('welcome to our cafe')

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