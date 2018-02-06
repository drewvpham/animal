class Animal(object):
    def __init__(self, name, health=100):
      self.name=name
      self.health=health
      return self
    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -=5
        return self

    def displayHealth(self):
        print self.health
