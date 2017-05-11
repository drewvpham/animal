from animal import Animal

class Dragon(Animal):

    def __init__(self, name, health=170):
        super(Dragon, self).__init__(name, health)


    def fly(self):
        print 'I am flying!!!'
        self.health-=10
        return self

    def displayHealth(self):
        print "I'm a fricken dragon!"

        super(Dragon, self).displayHealth()

        return self
