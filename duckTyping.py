#duck typing - different objects have same the methods

class Cathedral():
    def build(self):
        print('building a cathedral......')
    def visit(self):
        print('welcome to our Cathedral')

class Cafe():
    def build(self):
        print('building a cafe..')
    def visit(self):
        print('welcome to our cafe')

def create(building):
    building.build()    #works for any object that has those method
    building.visit()

not_dame = Cathedral()
java_house = Cafe()

things = not_dame, java_house #tuple

for the_thing in (things):  #iterate over tuple
    create(the_thing)
    print()