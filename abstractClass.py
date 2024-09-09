#abstract class to be inherited
from duckTyping import not_dame, java_house, things


class ThingToBuild():
    def build(self): pass
    def visit(self): pass

class Cathedral(ThingToBuild):
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