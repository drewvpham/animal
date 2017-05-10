from animal import Animal

class Dragon(Animal)

    def __init__(self, name, health):
        super(Dragon, self).__init__(name, health)

    def fly(self):

        self.health+=-10
        return self
