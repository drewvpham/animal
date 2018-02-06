from animal import Animal

class Dragon(Animal):

    def __init__(self, name, health=170):
        super(Dragon, self).__init__(name)
        self.health=health
    
    
  

    def fly(self):
        print 'I am flying!!!'
        self.health-=10
        print self.health
        
     

    def displayHealth(self):
        super(Dragon, self).displayHealth()
        print "I'm a fricken dragon!"
        return self

d=Dragon('digg')
d.fly()
d.displayHealth()
