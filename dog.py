from animal import Animal
#from current directory of animal (folder) import Animal class

class Dog(Animal):

    def __init__(self,name, health=150):
        super(Dog, self).__init__(name, health)


    def pet(self):
        print "Getting pet."
        self.health += 5

        return self
